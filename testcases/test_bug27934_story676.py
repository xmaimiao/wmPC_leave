import pytest
from common.contants import basepage_dir, test_bug27934_story676_dir
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

class Test_bug27934_story676:

    with open(test_bug27934_story676_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_edit_vacation_type_datas = datas["test_edit_vacation_type"]
        test_edit_approver_HR_datas = datas["test_edit_approver_HR"]
        test_AL_application_over_a_day_datas = datas["test_AL_application_over_a_day"]
        test_OA_approval_datas = datas["test_OA_approval"]
        test_leave_cancellation_datas = datas["test_leave_cancellation"]

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

    # 请假账号参数设置
    @pytest.mark.parametrize("data", test_edit_vacation_type_datas)
    def test_edit_vacation_type(self,data):
        '''
        验证编辑教职工休假類型、人員類型為行政人員
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_vacation_type(data["vacation_type"]). \
            edit_person_type(data["person_type"]). \
            click_save().wait_sleep(1).get_user_information()
        assert result == data["expect"]

    # 請假環境參數設置
    @pytest.mark.parametrize("data", test_edit_approver_HR_datas)
    def test_edit_approver_HR(self, data):
        '''
        验证編輯行政人員年假的HR
        '''
        result = self.main.goto_leave_settings().\
            goto_set_HR_approver(data["setting"]).goto_edit_HR(data["rules_name"]).\
            click_select_approver().choise_staff(data["user"]).click_save().\
            goto_edit_HR_page().click_save().wait_sleep(1).get_all_HR()
        assert result == data["expect"]

    # 申請假期
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

    #OA審批
    @pytest.mark.parametrize("data", test_OA_approval_datas)
    def test_OA_approval(self, data):
        '''
        验证OA審批，HR審批通過成功
        '''
        result = self.main.goto_OA_Approval().\
        goto_ALL_approvals_OA().goto_pending_for_approval_OA().\
        the_first_subject().approved().goto_approved_OA().get_the_fir_status()
        assert result != data["expect"]

    #銷假
    @pytest.mark.parametrize("data", test_leave_cancellation_datas)
    def test_leave_cancellation(self, data):
        '''
        验证第一條數據銷假
        '''
        result = self.main.goto_my_leave().goto_leave_details().\
            goto_the_fir_leave_cancellation().wait_sleep(1).leave_cancellation(data["date_type_list"]).\
            wait_sleep(1).remark(data["remark"]).clcik_save().get_the_fir_status()
        assert result == data["expect"]
