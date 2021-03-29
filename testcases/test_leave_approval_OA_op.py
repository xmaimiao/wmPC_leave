from common.contants import test_leave_approval_OA_dir, basepage_dir
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
    with open(test_leave_approval_OA_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)[option]
        return datas

class Test_Leave_Approval_OA:

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
                username(self._setup_datas[0]["username"]).password(self._setup_datas[0]["password"]).save()

        def teardown_class(self):
            '''
            非調試端口啓用
            '''
            self.main.close()

    @pytest.mark.parametrize("data", get_data("test_OA_approval"))
    def test_OA_approval(self, data):
        '''
        验证OA審批，HR審批通過成功
        '''
        result = self.main.goto_OA_Approval().\
        goto_ALL_approvals_OA().goto_pending_for_approval_OA().\
        the_first_subject().approved().goto_approved_OA().get_the_fir_status()
        assert result != data["expect"]

    def test_OA_reminder_of_supplement(self):
        '''
        验证OA提醒资料补充
        '''
        result = self.main.goto_OA_Approval(). \
            goto_ALL_approvals_OA().goto_pending_for_approval_OA(). \
            the_first_subject().reminder_of_supplement()
        assert result == True

    @pytest.mark.parametrize("data", get_data("test_OA_approval"))
    def test_OA_approval(self, data):
        '''
        验证OA審批，HR審批拒绝成功
        '''
        result = self.main.goto_OA_Approval().\
        goto_ALL_approvals_OA().goto_pending_for_approval_OA().\
        the_first_subject().not_approved().goto_approved_OA().get_the_fir_status()
        assert 3 <= len(result) <=6

