from common.contants import test_leave_application_dir, basepage_dir
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

class Test_Leave_Application:
    with open(test_leave_application_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_AL_application_datas = datas["test_AL_application"]
        test_get_days_available_datas = datas["test_get_days_available"]
        test_AL_application_over_a_day_datas = datas["test_AL_application_over_a_day"]
        test_cancel_the_first_leave_datas = datas["test_cancel_the_first_leave"]
        test_cancel_leave_number_datas = datas["test_cancel_leave_number"]

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

    @pytest.mark.parametrize("data", test_AL_application_datas)
    def test_AL_application(self, data):
        '''
        验证申請年假成功，謹一天
        '''
        result1 = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).\
            choice_startdate(data["leave_startyear"],data["leave_startmonth"],data["leave_startday"]).\
            remarks(data["remarks"]).cleck_save()
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
            remarks(data["remarks"]).cleck_save()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", test_get_days_available_datas)
    def test_get_days_available(self, data):
        '''
        验证假期可用天數的正確性
        '''
        result = self.main.goto_application_for_leaver().\
            get_days_available()
        assert result == data["expect"]


