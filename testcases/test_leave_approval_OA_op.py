from common.contants import test_leave_approval_OA_dir, basepage_dir
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

class Test_Leave_Approval_OA:
    with open(test_leave_approval_OA_dir, encoding="utf-8") as f:

        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_AL_application_datas = datas["test_AL_application"]
        test_get_days_available_datas = datas["test_get_days_available"]
        test_AL_application_over_a_day_datas = datas["test_AL_application_over_a_day"]

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

    @pytest.mark.parametrize("data", test_AL_application_datas)
    def test_OA_application(self, data):
        '''
        验证OA審批，HR審批通過成功
        '''
        result = self.main.goto_OA_Approval().\
            goto_ALL_approvals().\
            goto_pending_for_approval().\
            the_first_subject().approved().\
            goto_leave_application(data["application"]).\
            goto_my_leave().goto_leave_details().\
            get_first_object_status()
        assert result == data["expect"]

