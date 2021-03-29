import pytest
from common.contants import test_leave_search_dir, basepage_dir
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

class Test_Leave_Search:
    with open(test_leave_search_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_get_leave_total_of_user_datas = datas["test_get_leave_total_of_user"]
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

    @pytest.mark.parametrize("data", test_get_leave_total_of_user_datas)
    def test_get_leave_total_of_user(self, data):
        '''
        验证查询用户的请假单数量
        '''
        result = self.main.goto_leave_search().\
            simple_search(data["user"]).click_search().\
            get_current_leave_total()
        assert result == data["expect"]
