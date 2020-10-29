from common.contants import test_leave_for_HR_dir, basepage_dir
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

class Test_Leave_For_HR:
    with open(test_leave_for_HR_dir, encoding="utf-8") as f:

        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_application_of_HR_datas = datas["test_application_of_HR"]
        test_cancellation_of_leave_of_HR_datas = datas["test_cancellation_of_leave_of_HR"]

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

    @pytest.mark.parametrize("data", test_application_of_HR_datas)
    def test_application_of_HR(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_staff_application_for_leave_HR().\
            applicant().choise_staff(data["user"]).\
            click_save().goto_staff_application_for_Leave_HR(). \
            choice_over_a_day(). \
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]). \
            choice_enddate(data["enddate"]).chocie_enddate_type(data["leave_endtype"]). \
            cleck_save()
        assert data["expect"] in result

    @pytest.mark.parametrize("data", test_cancellation_of_leave_of_HR_datas)
    def test_cancellation_of_leave_of_HR(self, data):
        '''
        验证HR代请假-销假
        '''
        result = self.main.goto_leave_approval_HR().\
            goto_application_records_for_HR().\
            order_by_submission_time().\
            the_first_cancellation_of_leave().\
            choose_all().click_save().\
            get_the_first_days_of_leave()
        assert result == data["expect"]

    def test_get_data(self):
        result = self.main.goto_leave_approval_HR().\
            goto_approved_HR(). \
            get_the_first_days_of_leave_Apppage()
        assert result == '1.0'

