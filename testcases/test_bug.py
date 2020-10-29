from common.contants import basepage_dir, test_bug_dir
from page.basepage import _get_working
from page.main import Main
import pytest
import yaml

def get_env():
    '''
    获取环境变量：uat、dev、mo正式站
    '''
    with open(basepage_dir, encoding="utf-8") as f:
        return yaml.safe_load(f)["default"]

class Test_Bug:
    with open(test_bug_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_AL_application_pre_datas = datas["test_AL_application_pre"]
        test_AL_application_datas = datas["test_AL_application"]

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
                username(self.setup_datas["username"]).password(self.setup_datas["password"]).save(). \
                goto_application(). \
                goto_leave(self.setup_datas["application"])

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", test_AL_application_pre_datas)
    def test_AL_application_pre(self, data):
        '''
        前提条件
        1.DC设置test309岗位为20181229岗位一级、入职日期为2020-07-01，合同期為2020/07/01~2021/07/30，休假类型为博士後（DC处理）
        2.休假设置，假期周期7/1~6/30，添加“博士後”类型  完成
        3.休假设置，年假设置添加“按假期周期”类型，适用人群选择“1201测试”，基础天数12天，最高可请天数12天 完成
        4.休假设置，暑期设置（已存在），编辑添加适用人群“1201测试” 完成
        验证申請年假成功，謹一天
        '''
        # 1.人員信息表設置test309 休假類型為博士後()
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            edit_the_first_approver(). \
            edit_vacation_type(data["leave_type"]).\
            click_save().get_the_first_day_ofentry()
        assert result == str(data["expect1"])

        # 2.编辑 假期周期7/1~6/30，添加“博士後”类型
        result = self.main.goto_leave_settings(). \
            goto_holiday_period(data["setting2"]). \
            edit_holiday_period(data["period_name"]). \
            edit_for_people(data["leave_type"]). \
            click_save().get_ele_of_add()
        assert result == data["expect2"]

        # 4.编辑暑期设置（暑期週三為工作日的教師適用），编辑添加适用人群“博士後”
        result = self.main.goto_leave_settings().\
            goto_summer_workday_setting(data["setting3"]).\
            edit_summer_setting(data["summer_name"]).\
            edit_for_people(data["leave_type"]).\
            click_save().get_ele_of_add()
        assert result == data["expect3"]

        # 3.休假设置，年假设置添加“按假期周期”类型，适用人群选择“博士後”，基础天数12天，最高可请天数12天
        result = self.main.goto_leave_settings(). \
            goto_paid_Annual_Leave(data["setting4"]).add_holiday().rule_name(data["rule_name"]).\
            Annual_starting_point(data["annual_point"]).Maximum_days(data["maxTotal_days"]). \
            Minimum_leave(data["minDay"]).Annual_statistics(data["num"]).increment_rule().\
            for_people(data["leave_type"]).click_save().get_the_first_rule_name()
        assert result == data["expect4"]

    @pytest.mark.parametrize("data", test_AL_application_datas)
    def test_AL_application(self,data):
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).\
            choice_over_a_day().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            choice_enddate(data["enddate"]).chocie_enddate_type(data["leave_endtype"]).\
            remarks(data["remarks"]).cleck_save()
        assert result == data["expect1"]

        result = self.main.goto_leave_balance_statement(). \
            keywords_search(data["keywords"]).click_search(). \
            get_the_first_rest_in_that_year()
        assert data["expect2"] == result


