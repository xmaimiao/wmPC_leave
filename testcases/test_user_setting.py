import pytest
from common.contants import basepage_dir, test_user_setting_dir
from page.basepage import _get_working
from page.main import Main

import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        wm_env = datas["default"]
        setup_datas = datas[wm_env]
        return setup_datas

class Test_User_Setting:

    with open(test_user_setting_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_get_holiday_period_datas = datas["test_get_holiday_period"]
        test_edit_holiday_period_datas = datas["test_edit_holiday_period"]
        test_get_AL_rules_datas = datas["test_get_AL_rules"]
        test_edit_annual_datas = datas["test_edit_annual"]
        test_get_summer_date_and_for_people_datas = datas["test_get_summer_date_and_for_people"]
        test_edit_summer_setting_datas = datas["test_edit_summer_setting"]
        test_edit_summer_setting_of_date_datas = datas["test_edit_summer_setting_of_date"]
        test_get_leave_total_of_user_datas = datas["test_get_leave_total_of_user"]
        test_get_user_information_datas = datas["test_get_user_information"]
        test_edit_date_of_entry_datas = datas["test_edit_date_of_entry"]
        test_edit_person_type_datas = datas["test_edit_person_type"]

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
                username(self._setup_datas["username"]).password(self._setup_datas["password"]).save(). \
                goto_application(). \
                goto_leave(self._setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    # 请假环境参数设置

    @pytest.mark.parametrize("data", test_get_holiday_period_datas)
    def test_get_holiday_period(self,data):
        '''
        验证获取休假设置-全部假期周期内容
        '''
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting"]).\
            get_holiday_period_all()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_holiday_period_datas)
    def test_edit_holiday_period(self,data):
        '''
        验证編輯休假设置-假期周期,添加适用人群
        '''
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting"]).edit_holiday_period(data["period_name"]).\
            edit_for_people().add_leave_type(data["leave_type"]).click_save().goto_edit_holiday_period().\
            click_save().get_ele_of_add()
        assert result == data["expect"]


    @pytest.mark.parametrize("data", test_get_AL_rules_datas)
    def test_get_AL_rules(self, data):
        '''
        验证获取前5条有薪年假规则内容,查询的关键字为：全职
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).\
            search_key(data["rule_name"]).get_AL_rules()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_annual_datas)
    def test_edit_annual(self,data):
        '''
        验证編輯休假设置-年假,编辑适用人群
        num：选中第N种年假类型
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            Annual_statistics(data["num"]).increment_rule().\
            for_people().add_leave_type(data["leave_type"]).click_save().goto_add_or_edit_holiday().\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_summer_date_and_for_people_datas)
    def test_get_summer_date_and_for_people(self, data):
        '''
        验证获取休假设置-暑期工作设置
        '''
        result = self.main.goto_leave_settings(). \
            goto_summer_workday_setting(data["setting"]). \
            get_summer_date_and_for_people(data["summer_name"])
        assert result == True

    @pytest.mark.parametrize("data", test_edit_summer_setting_datas)
    def test_edit_summer_setting(self, data):
        '''
        验证編輯休假设置-暑期工作设置-修改适用人群
        '''
        result = self.main.goto_leave_settings().\
            goto_summer_workday_setting(data["setting"]).edit_summer_setting(data["summer_name"]).\
            edit_for_people().add_leave_type(data["leave_type"]).click_save().goto_edit_summer_setting().\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_summer_setting_of_date_datas)
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

    # 请假人员参数设置
    @pytest.mark.dependency(name="test_get_leave_total_of_user")
    @pytest.mark.parametrize("data", test_get_leave_total_of_user_datas)
    def test_get_leave_total_of_user(self, data):
        '''
        验证查询用户的请假单数量
        '''
        result = self.main.goto_leave_search().\
            simple_search(data["user"]).click_search().\
            get_current_leave_total()
        assert result == data["expect"]

    # @pytest.mark.skip
    @pytest.mark.parametrize("data", test_get_user_information_datas)
    def test_get_user_information(self,data):
        '''
        验证获取员工的上級、主管、休假類型、上一年度帶假、年假結余天數、入職日期、離職日期
        '''
        result = self.main.goto_approver_information_table(). \
            get_the_fir_information(data["user_list"])
        assert result == True

    # @pytest.mark.dependency(depends=["test_get_leave_total_of_user"])
    @pytest.mark.parametrize("data", test_edit_date_of_entry_datas)
    def test_edit_date_of_entry(self,data):
        '''
        验证编辑教职工入职日期、休假類型
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_vacation_type(data["vacation_type"]).\
            edit_date_of_entry(data["entrydate"]).\
            click_save().wait_sleep(1).get_the_first_day_ofentry()
        assert result == str(data["expect"])

    @pytest.mark.parametrize("data", test_edit_person_type_datas)
    def test_edit_person_type(self,data):
        '''
        验证编辑教职工人員類型
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_person_type(data["person_type"]).\
            click_save().wait_sleep(1).get_user_information()
        assert result == data["expect"]