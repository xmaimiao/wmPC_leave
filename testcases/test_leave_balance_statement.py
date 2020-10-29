from common.contants import basepage_dir, test_leave_balance_statement_dir
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

class Test_Leave_Balance_Statement:

    with open(test_leave_balance_statement_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        setup_datas = datas[get_env()]
        test_get_the_first_rest_in_that_year_datas = datas["test_get_the_first_rest_in_that_year"]
        # test_cancellation_of_leave_of_HR_datas = datas["test_cancellation_of_leave_of_HR"]

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

    @pytest.mark.parametrize("data", test_get_the_first_rest_in_that_year_datas)
    def test_get_the_first_rest_in_that_year(self, data):
        '''
        验证HR代请假,result是Html页面，验证正确调整休假审批（HR）-代请假记录页面
        '''
        result = self.main.goto_leave_balance_statement().\
            keywords_search(data["keywords"]).click_search().\
            get_the_first_rest_in_that_year()
        assert data["expect"] == result
