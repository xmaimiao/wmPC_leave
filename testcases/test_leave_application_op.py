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
    with open(test_leave_application_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Leave_Application:

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

    def application(self, mobile_no,Leave_type,startdate,leave_starttype,remarks,path):
        '''
        验证申請假期，謹一天
        '''
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(mobile_no).choice_Leave_type(Leave_type).\
            choice_startdate(startdate).chocie_startdate_type(leave_starttype).\
            remarks(remarks).upload_attachment(path).wait_sleep(2).cleck_save().get_first_object_Sn()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_application"))
    def test_application(self,data):
        self.application(data["mobile_no"],data["Leave_type"],data["startdate"],
                         data["leave_starttype"],data["remarks"],data["path"])


    @pytest.mark.parametrize("data", get_data("test_AL_application"))
    def test_AL_application(self, data):
        '''
        验证申請年假成功，謹一天
        '''
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            remarks(data["remarks"]).wait_sleep(2).cleck_save().get_first_object_Sn()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_AL_application_replace"))
    def test_AL_application_replace(self, data):
        '''
        验证代请假，申請年假成功，謹一天
        '''
        result = self.main.goto_application_for_leaver().\
            choice_createUser(data["createUser"]).send_mobile_no(data["mobile_no"]).\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            remarks(data["remarks"]).wait_sleep(2).cleck_save_backto_records().get_ele_of_tab_title()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_UL_application"))
    def test_UL_application(self, data):
        '''
        验证申請無薪假成功，謹一天
        '''
        result1 = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).choice_Unpaid_Leave().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            remarks(data["remarks"]).upload_attachment(data["path"]).wait_sleep(3).cleck_save().\
            get_first_object_Sn()
        assert result1 == data["expect1"]

    @pytest.mark.parametrize("data", get_data("test_cancel_the_first_leave"))
    def test_cancel_the_first_leave(self, data):
        '''
        验证取消休假明細，第一行的休假申請
        '''
        result = self.main.goto_my_leave().\
            goto_leave_details().\
            cancel_the_first_leave().\
            get_first_object_status()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_cancel_leave_number"))
    def test_cancel_leave_number(self, data):
        '''
        验证取消休假，根据休假订单号
        '''
        result = self.main.goto_my_leave(). \
            goto_leave_details(). \
            cancel_leave_of_number(data["leave_num"])
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_AL_application_over_a_day"))
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

    @pytest.mark.parametrize("data", get_data("test_UL_application_over_a_day"))
    def test_UL_application_over_a_day(self, data):
        '''
        验证申請無薪假成功，超過一天
        '''
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).choice_Unpaid_Leave().\
            choice_over_a_day().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            choice_enddate(data["enddate"]).chocie_enddate_type(data["leave_endtype"]).\
            remarks(data["remarks"]).upload_attachment(data["path"]).wait_sleep(2).cleck_save(). \
            get_first_object_Sn()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_ML_application_over_a_day"))
    def test_ML_application_over_a_day(self, data):
        '''
        验证申請婚假成功，超過一天
        '''
        result = self.main.goto_application_for_leaver().\
            send_mobile_no(data["mobile_no"]).choice_Marriage_Leave().\
            choice_over_a_day().\
            choice_startdate(data["startdate"]).chocie_startdate_type(data["leave_starttype"]).\
            choice_enddate(data["enddate"]).chocie_enddate_type(data["leave_endtype"]).\
            remarks(data["remarks"]).upload_attachment(data["path"]).wait_sleep(2).cleck_save(). \
            get_first_object_Sn()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_leave_cancellation"))
    def test_leave_cancellation(self, data):
        '''
        验证第一條數據銷假
        '''
        result = self.main.goto_my_leave().goto_leave_details().\
            goto_the_fir_leave_cancellation().wait_sleep(1).leave_cancellation(data["date_type_list"]).\
            wait_sleep(1).remark(data["remark"]).clcik_save().get_the_fir_status()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_leave_cancellation_replace"))
    def test_leave_cancellation_replace(self, data):
        '''
        验证第一條數據銷假-代请假用
        '''
        result = self.main.goto_my_leave().goto_substitute_leave_records().\
            goto_the_fir_leave_cancellation_records().wait_sleep(1).leave_cancellation(data["date_type_list"]).\
            wait_sleep(1).remark(data["remark"]).clcik_save_backto_records().get_the_fir_status()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_get_days_available"))
    def test_get_days_available(self, data):
        '''
        验证假期可用天數的正確性
        '''
        result = self.main.goto_application_for_leaver().\
            get_days_available()
        assert result == data["expect"]

    def test_leave_total(self):
        '''
        验证请假单的数量
        '''
        result = self.main.goto_my_leave().\
            goto_leave_details().get_leave_total()
        assert result == 0


