from common.contants import basepage_dir,test_leave_setting_dir
from page.basepage import get_working
from page.main import Main
import pytest
import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        return yaml.safe_load(f)["default"]

class Test_Leave_Setting:
    with open(test_leave_setting_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_delect_annual_datas = datas["test_delect_annual"]
        test_add_annual_datas = datas["test_add_annual"]
        test_edit_annual_datas = datas["test_edit_annual"]
        test_edit_holiday_period_datas = datas["test_edit_holiday_period"]
        test_edit_summer_setting_datas = datas["test_edit_summer_setting"]

    working = get_working()
    if working:
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
                username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
                goto_application(). \
                goto_leave(self.setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

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

    @pytest.mark.parametrize("data", test_edit_annual_datas)
    def test_edit_annual(self,data):
        '''
        验证編輯休假设置-年假
        '''
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting"]).edit_holiday(data["rule_name"]).\
            Annual_statistics(data["num"]).increment_rule().\
            for_people(data["leave_type"]).click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_holiday_period_datas)
    def test_edit_holiday_period(self,data):
        '''
        验证編輯休假设置-假期周期
        '''
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting"]).\
            edit_holiday_period(data["period_name"]).\
            edit_for_people(data["leave_type"]).\
            click_save().get_ele_of_add()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_edit_summer_setting_datas)
    def test_edit_summer_setting(self, data):
        '''
        验证編輯休假设置-暑期工作设置
        '''
        result = self.main.goto_leave_settings().\
            goto_summer_workday_setting(data["setting"]).\
            edit_summer_setting(data["summer_name"]).\
            edit_for_people(data["leave_type"]).\
            click_save().get_ele_of_add()
        assert result == data["expect"]