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
        wm_env = datas["default"]
        setup_datas = datas[wm_env]
        return setup_datas

class Test_Leave_Setting:
    with open(test_leave_setting_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_get_AL_rules_datas = datas["test_get_AL_rules"]
        test_delect_annual_datas = datas["test_delect_annual"]
        test_add_annual_datas = datas["test_add_annual"]
        test_edit_annual_datas = datas["test_edit_annual"]
        test_edit_annual_cumulative_rule_datas = datas["test_edit_annual_cumulative_rule"]
        test_edit_holiday_period_datas = datas["test_edit_holiday_period"]
        test_get_holiday_period_datas = datas["test_get_holiday_period"]
        test_edit_summer_setting_datas = datas["test_edit_summer_setting"]
        test_edit_summer_setting_of_date_datas = datas["test_edit_summer_setting_of_date"]
        test_get_summer_date_and_for_people_datas = datas["test_get_summer_date_and_for_people"]
        test_get_xingzheng_AL_HR_datas = datas["test_get_xingzheng_AL_HR"]
        test_get_jiaoyan_AL_HR_datas = datas["test_get_jiaoyan_AL_HR"]
        test_edit_xingzheng_AL_HR_datas = datas["test_edit_xingzheng_AL_HR"]
        test_del_xingzheng_AL_HR_datas = datas["test_del_xingzheng_AL_HR"]

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

    @pytest.mark.parametrize("data", test_get_AL_rules_datas)
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
            for_people(data["leave_type"]).click_save().get_the_first_rule_name()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_annual_cumulative_rule_datas)
    def test_edit_annual_cumulative_rule(self,data):
        '''
        验证編輯休假设置-年假，不纍計
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            wait_sleep(1).cumulative_rule().click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_annual_datas)
    def test_edit_annual(self,data):
        '''
        验证編輯休假设置-年假，適用人群及不轉結
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            Annual_statistics(data["num"]).increment_rule().\
            for_people(data["leave_type"]).click_save().get_ele_of_add()
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
            goto_holiday_period(data["setting"]).\
            edit_holiday_period(data["period_name"]).\
            edit_for_people(data["leave_type"]).\
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
            goto_summer_workday_setting(data["setting"]).\
            edit_summer_setting(data["summer_name"]).\
            edit_for_people(data["leave_type"]).\
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

    @pytest.mark.parametrize("data", test_get_xingzheng_AL_HR_datas)
    def test_get_xingzheng_AL_HR(self, data):
        '''
        验证獲取刑偵人員年假的HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).get_xingzheng_AL_HR()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_jiaoyan_AL_HR_datas)
    def test_get_jiaoyan_AL_HR(self, data):
        '''
        验证獲取教研人員年假的HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).get_jiaoyan_AL_HR()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_xingzheng_AL_HR_datas)
    def test_edit_xingzheng_AL_HR(self, data):
        '''
        验证編輯教研人員年假的HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_xingzheng_AL_HR().\
            click_select_staff().choise_staff(data["user"]).click_save().\
            goto_edit_xingzheng_AL_HR_page().click_save().get_xingzheng_AL_HR()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_del_xingzheng_AL_HR_datas)
    def test_del_xingzheng_AL_HR(self, data):
        '''
        验证刪除教研人員年假的HR。刪除某個人員
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_xingzheng_AL_HR().\
            click_select_staff().wait_sleep(22).delect_staff(data["users"]).click_save().\
            goto_edit_xingzheng_AL_HR_page().click_save().get_xingzheng_AL_HR()
        assert result == data["expect"]

