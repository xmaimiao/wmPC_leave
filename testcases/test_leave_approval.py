from common.contants import basepage_dir, test_leave_approval_dir
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
    with open(test_leave_approval_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Leave_Approval:

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

    @pytest.mark.parametrize("data", get_data("test_leave_approval"))
    def test_leave_approval(self,data):
        '''
        验证審批通過
        '''
        result = self.main.goto_leave_approval().\
            goto_pending_for_approval().order_by_submission_time().\
            the_fir_approved()
        assert result == data["expect"]

    @pytest.mark.parametrize("data", get_data("test_leave_not_approval"))
    def test_leave_not_approval(self,data):
        '''
        验证審批不通過
        '''
        result = self.main.goto_leave_approval().\
            goto_pending_for_approval().order_by_submission_time().\
            the_fir_not_approved()
        assert result == data["expect"]
