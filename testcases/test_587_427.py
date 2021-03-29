from common.contants import basepage_dir, test_587_427_dir
from page.basepage import _get_working
from page.main import Main
import pytest
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

class Test_587_427:
    with open(test_587_427_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_AL_application_datas = datas["test_AL_application"]
        test_UL_application_datas = datas["test_UL_application"]
        test_AL_application_over_a_day_datas = datas["test_AL_application_over_a_day"]
        test_cancel_the_first_leave_datas = datas["test_cancel_the_first_leave"]
        test_cancel_leave_number_datas = datas["test_cancel_leave_number"]
        test_get_the_first_AL_info_datas = datas["test_get_the_first_AL_info"]
        test_get_AL_rules_datas = datas["test_get_AL_rules"]
        test_delect_annual_datas = datas["test_delect_annual"]
        test_add_annual_datas = datas["test_add_annual"]
        test_edit_holiday_period_datas = datas["test_edit_holiday_period"]
        test_get_holiday_period_datas = datas["test_get_holiday_period"]
        test_edit_summer_setting_datas = datas["test_edit_summer_setting"]
        test_get_summer_date_and_for_people_datas = datas["test_get_summer_date_and_for_people"]
        test_get_user_information_datas = datas["test_get_user_information"]
        test_edit_date_of_entry_datas = datas["test_edit_date_of_entry"]

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
    # 環境配置
    def test_get_AL_rules(self, data):
        '''
        验证获取前5条有薪年假规则内容
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]). \
            get_AL_rules()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_delect_annual_datas)
    def test_delect_annual(self, data):
        '''
        验证删除休假设置-年假
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]). \
            delect_holiday(data["rule_name"]).\
            search_key(data["rule_name"]).get_current_data_total()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_add_annual_datas)
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

    # 賬號設置
    @pytest.mark.parametrize("data", test_get_user_information_datas)
    def test_get_user_information(self,data):
        '''
        验证获取员工的上級、主管、休假類型、上一年度帶假、年假結余天數、入職日期、離職日期
        '''
        result = self.main.goto_approver_information_table(). \
            get_the_fir_information(data["user_list"])
        assert result == True


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

    @pytest.mark.parametrize("data", test_AL_application_datas)
    def test_AL_application(self, data):
        '''
        验证申請年假成功，謹一天
        '''
        result1 = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            remarks(data["remarks"]).wait_sleep(2).cleck_save().get_first_object_Sn()
        assert result1 == data["expect1"]

    @pytest.mark.parametrize("data", test_UL_application_datas)
    def test_UL_application(self, data):
        '''
        验证申請年假成功，謹一天
        '''
        result1 = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).choice_Unpaid_Leave().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            remarks(data["remarks"]).upload_attachment(data["path"]).wait_sleep(3).cleck_save(). \
            get_first_object_Sn()
        assert result1 == data["expect1"]

    @pytest.mark.parametrize("data", test_cancel_the_first_leave_datas)
    def test_cancel_the_first_leave(self, data):
        '''
        验证取消休假明細，第一行的休假申請
        '''
        result = self.main.goto_my_leave().\
            goto_leave_details().\
            cancel_the_first_leave().\
            get_first_object_status()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_cancel_leave_number_datas)
    def test_cancel_leave_number(self, data):
        '''
        验证取消休假，根据休假订单号
        '''
        result = self.main.goto_my_leave(). \
            goto_leave_details(). \
            cancel_leave_of_number(data["leave_num"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_AL_application_over_a_day_datas)
    def test_AL_application_over_a_day(self, data):
        '''
        验证申請年假成功，超過一天
        '''
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).\
            choice_over_a_day().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            choice_enddate(data["enddate"]).chocie_enddate_type(data["leave_endtype"]).\
            remarks(data["remarks"]).wait_sleep(2).cleck_save().get_first_object_Sn()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_the_first_AL_info_datas)
    def test_get_the_first_AL_info(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_leave_balance_statement().\
            keywords_search(data["keywords"]).click_search().\
            get_the_fir_AL_infomation()
        assert data["expect"] == result
