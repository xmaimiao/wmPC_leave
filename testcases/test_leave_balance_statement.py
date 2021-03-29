from common.contants import basepage_dir, test_leave_balance_statement_dir
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

class Test_Leave_Balance_Statement:

    with open(test_leave_balance_statement_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_get_the_first_rest_in_that_year_datas = datas["test_get_the_first_rest_in_that_year"]
        test_get_the_first_AL_info_datas = datas["test_get_the_first_AL_info"]

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

    @pytest.mark.parametrize("data", test_get_the_first_rest_in_that_year_datas)
    def test_get_the_first_rest_in_that_year(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_leave_balance_statement().\
            keywords_search(data["keywords"]).click_search().\
            get_the_first_rest_in_that_year()
        assert data["expect"] == result

    @pytest.mark.parametrize("data", test_get_the_first_AL_info_datas)
    def test_get_the_first_AL_info(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_leave_balance_statement().\
            keywords_search(data["keywords"]).click_search().\
            get_the_fir_AL_infomation()
        assert data["expect"] == result
