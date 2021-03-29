import pytest

from common.contants import basepage_dir,test_leave_setting_dir
from page.basepage import _get_working
from page.main import Main
import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # 获取basepage.yaml中设置的环境变量
        wm_env =  datas["default"]
        # 根据环境变量取对应的账号和密码
        user_env = datas["user"][wm_env]
        # 根据环境变量取对应的睡眠时间
        sleep_env = datas["sleeps"][wm_env]
        return user_env,sleep_env

def get_data(option):
    '''
    获取yaml测试数据
    '''
    with open(test_leave_setting_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Leave_Setting:

    _setup_datas = get_env()
    _working = _get_working()
    if _working == "port":
        def setup(self):
            '''
            開啓調試端口啓用
            '''
            self.main = Main()
    else:
        def setup_class(self):
            '''
            非調試端口用
            '''
            self.main = Main().goto_login(). \
                username(self._setup_datas[0]["username"]).password(self._setup_datas[0]["password"]).save(). \
                goto_application(). \
                goto_leave(self._setup_datas[0]["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data",get_data("test_get_AL_rules"))
    def test_get_AL_rules(self, data):
        '''
        验证获取前5条有薪年假规则内容
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]). \
            get_AL_rules()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_delect_annual"))
    def test_delect_annual(self, data):
        '''
        验证删除休假设置-年假
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]). \
            delect_holiday(data["rule_name"]).\
            search_key(data["rule_name"]).get_current_data_total()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_add_annual"))
    def test_add_annual(self,data):
        '''
        验证添加休假设置-年假
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).add_holiday().rule_name(data["rule_name"]).\
            Annual_starting_point(data["annual_point"]).Maximum_days(data["maxTotal_days"]). \
            Minimum_leave(data["minDay"]).Annual_statistics(data["num"]).increment_rule().\
            for_people().add_leave_type(data["leave_type"]).click_save().goto_add_or_edit_holiday().\
            click_save().get_the_first_rule_name()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_annual_cumulative_rule"))
    def test_edit_annual_cumulative_rule(self,data):
        '''
        验证編輯休假设置-年假，不纍計
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            wait_sleep(1).cumulative_rule().click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_annual"))
    def test_edit_annual(self,data):
        '''
        验证編輯休假设置-年假，適用人群及不轉結
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            Annual_statistics(data["num"]).increment_rule(). \
            Annual_starting_point(data["annual_point"]).Maximum_days(data["maxTotal_days"]).\
            add_leave_type(data["leave_type"]).click_save().goto_add_or_edit_holiday().\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_annual_staff"))
    def test_edit_annual_staff(self,data):
        '''
        验证休假设置-年假，編輯適用人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).for_people().add_leave_type(data["leave_type"]). \
            click_save().goto_add_or_edit_holiday().click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_rest_day_staff"))
    def test_edit_rest_day_staff(self,data):
        '''
        验证休息日，編輯適用人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_rest_day(data["setting"]).edit_rest_day_staff_for_name(data["week"]).add_leave_type(data["leave_type"]). \
            click_save().goto_rest_day().get_staff_for_name(data["week"])
        for people in data["leave_type"]:
            pytest.assume(people in result)


    @pytest.mark.parametrize("data",get_data("test_add_public_holiday"))
    def test_add_public_holiday(self,data):
        '''
        验证添加公众假
        '''
        result = self.main.goto_leave_settings(). \
            goto_public_holiday(data["setting"]).create_rule().edit_name(data["rule_name"]).edit_Enname(data["rule_name"]).\
            edit_startday(data["startday"]).edit_endday(data["endday"]).for_people().\
            add_leave_type(data["leave_type"]).click_save().goto_public_holiday_details().click_save().get_ele_of_add()
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_add_public_holiday_half_day"))
    def test_add_public_holiday_half_day(self,data):
        '''
        验证添加公众假-半天
        '''
        result = self.main.goto_leave_settings(). \
            goto_public_holiday(data["setting"]).create_rule().edit_name(data["rule_name"]).edit_Enname(data["rule_name"]).\
            edit_startday(data["startday"]).edit_endday(data["endday"]).is_this_half_day_leave(data["half_day"]).for_people().\
            add_leave_type(data["leave_type"]).click_save().goto_public_holiday_details().click_save().get_ele_of_add()
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_edit_public_holiday_staff"))
    def test_edit_public_holiday_staff(self,data):
        '''
        验证修改公衆假例外人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_public_holiday(data["setting"]).edit_rule_for_name(data["rule_name"]).for_people().\
            add_leave_type(data["leave_type"]).click_save().goto_public_holiday_details().click_save(). \
            get_exceptional_group_for_name(data["rule_name"])
        for people in data["leave_type"]:
            pytest.assume(people in result)

    @pytest.mark.parametrize("data",get_data("test_edit_public_holiday_mandatory"))
    def test_edit_public_holiday_mandatory(self,data):
        '''
        验证修改公衆假例外人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_public_holiday(data["setting"]).edit_rule_for_name(data["rule_name"]).\
            mandatory_holiday().click_save().get_ele_of_add()
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_get_holiday_period"))
    def test_get_holiday_period(self,data):
        '''
        验证获取休假设置-全部假期周期内容
        '''
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting"]).\
            get_holiday_period_all()
        assert result == data["expect"]


    @pytest.mark.parametrize("data",get_data("test_edit_holiday_period"))
    def test_edit_holiday_period(self,data):
        '''
        验证編輯休假设置-假期周期,添加适用人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting"]).edit_holiday_period(data["period_name"]).\
            edit_for_people().add_leave_type(data["leave_type"]).click_save().goto_edit_holiday_period().\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_add_worktime_setting"))
    def test_add_worktime_setting(self,data):
        '''
        验证添加工作時間設置
        '''
        result = self.main.goto_leave_settings(). \
            goto_worktime_setting(data["setting"]).add_rule().\
            edit_rule_name(data["rule_name"]).edit_start_date(data["starttime"]).edit_end_date(data["endtime"]).for_people(). \
            add_leave_type(data["leave_type"]).click_save().goto_worktime_setting().\
            click_save().get_ele_of_add()
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_get_summer_date_and_for_people"))
    def test_get_summer_date_and_for_people(self, data):
        '''
        验证获取休假设置-暑期工作设置
        '''
        result = self.main.goto_leave_settings(). \
            goto_summer_workday_setting(data["setting"]). \
            get_summer_date_and_for_people(data["summer_name"])
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_edit_summer_setting"))
    def test_edit_summer_setting(self, data):
        '''
        验证編輯休假设置-暑期工作设置-修改适用人群
        '''
        result = self.main.goto_leave_settings().\
            goto_summer_workday_setting(data["setting"]).edit_summer_setting(data["summer_name"]).\
            edit_for_people().add_leave_type(data["leave_type"]).click_save().goto_edit_summer_setting().\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_summer_setting_of_date"))
    def test_edit_summer_setting_of_date(self, data):
        '''
        验证編輯休假设置-暑期工作设置-修改暑期日期
        '''
        result = self.main.goto_leave_settings().\
            goto_summer_workday_setting(data["setting"]).\
            edit_summer_setting(data["summer_name"]).\
            edit_start_date(data["start_date"]).edit_end_date(data["end_date"]).\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_get_all_HR"))
    def test_get_all_HR(self, data):
        '''
        验证獲取HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).get_all_HR()
        assert result == True

    @pytest.mark.parametrize("data",get_data("test_edit_approver_HR"))
    def test_edit_approver_HR(self, data):
        '''
        验证編輯審批人 HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_HR(data["rules_name"]).\
            click_select_approver().choise_staff(data["user"],self._setup_datas[1]["choice_staff"]).click_save().\
            goto_edit_HR_page().click_save().wait_sleep(1).get_all_HR()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_approver_check_HR"))
    def test_edit_approver_check_HR(self, data):
        '''
        验证編輯審批人 \審核人 HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_HR(data["rules_name"]).\
            click_select_approver().choise_staff(data["user"],self._setup_datas[1]["choice_staff"]).\
            click_save().goto_edit_HR_page().\
            click_select_check().choise_staff(data["user"],self._setup_datas[1]["choice_staff"]).\
            click_save().goto_edit_HR_page().\
            click_save().wait_sleep(1).get_all_HR()
        assert result == data["expect"]


    @pytest.mark.parametrize("data",get_data("test_del_approver_HR"))
    def test_del_approver_HR(self, data):
        '''
        验证刪除審批人 HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_HR(data["rules_name"]).\
            click_select_approver().delect_staff(data["users"]).click_save().\
            goto_edit_HR_page().click_save().wait_sleep(1).get_all_HR()
        assert result == data["expect"]


    @pytest.mark.parametrize("data",get_data("test_AL_rules_add_types"))
    def test_AL_rules_add_types(self,data):
        '''
        重新調整了選擇休假類型的UI，測試添加功能
        '''
        result = self.main.goto_leave_settings().\
            goto_paid_Annual_Leave(data["setting"]).search_holiday(data["rule_name"]). \
            edit_holiday(data["rule_name"]).for_people().add_leave_type(data["type_list"]).\
            click_save().goto_add_or_edit_holiday().click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_AL_rules_del_types"))
    def test_AL_rules_del_types(self,data):
        '''
        重新調整了選擇休假類型的UI，測試刪除功能
        '''
        result = self.main.goto_leave_settings().\
            goto_paid_Annual_Leave(data["setting"]).search_holiday(data["rule_name"]). \
            edit_holiday(data["rule_name"]).for_people().del_leave_type(data["type_list"]).\
            click_save().goto_add_or_edit_holiday().click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data",get_data("test_edit_person_type"))
    def test_edit_person_type(self,data):
        '''
        验证编辑教职工人員類型
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_person_type(data["person_type"]).\
            click_save().wait_sleep(1).get_user_information()
        assert result == str(data["expect"])
