import pytest
from page.main import Main
import shelve
from common.contants import test_edit_approver_information_dir, basepage_dir
from page.basepage import _get_working
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

class Test_Edit_Approver_Information:

    with open(test_edit_approver_information_dir, encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        test_clear_superior_supervisor_datas = datas["test_clear_superior_supervisor"]
        test_edit_leave_type_datas = datas["test_edit_leave_type"]
        test_edit_date_datas = datas["test_edit_date"]
        test_edit_date_of_entry_datas = datas["test_edit_date_of_entry"]
        test_get_superior_and_supervisor_datas = datas["test_get_superior_and_supervisor"]
        test_get_superior_datas = datas["test_get_superior"]
        test_edit_superior_and_supervisor_datas = datas["test_edit_superior_and_supervisor"]
        test_get_user_information_datas = datas["test_get_user_information"]
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



    @pytest.mark.parametrize("data", test_clear_superior_supervisor_datas)
    def test_clear_superior_supervisor(self, data):
        '''
        验证清空上级/主管
        '''
        result = self.main.goto_approver_information_table().\
            keywords_search(data["keywords"]).click_search_button().\
            wait_sleep(1).edit_the_first_approver().\
            edit_superior().click_clear_button().click_save().goto_approver_information_details().\
            edit_supervisor().click_clear_button().click_save().goto_approver_information_details().\
            click_save().wait_sleep(1).get_the_first_superior()
        assert result == data["expect"]

        result2 = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).get_the_first_supervisor()
        assert result2 == data["expect"]


    @pytest.mark.parametrize("data", test_edit_leave_type_datas)
    def test_edit_leave_type(self,data):
        '''
        验证编辑休假類型
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_vacation_type(data["vacation_type"]).\
            click_save().wait_sleep(1).get_the_first_day_ofentry()
        assert result == str(data["expect"])

    @pytest.mark.parametrize("data", test_edit_date_datas)
    def test_edit_date(self,data):
        '''
        验证编辑教职工入职、离职、合同开始、合同结束日期
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver().\
            edit_date_of_entry(data["entrydate"]).\
            edit_date_of_resignation(data["resignationdate"]).\
            edit_contract_start_date(data["contract_start_date"]).\
            edit_contract_end_date(data["contract_end_date"]).\
            click_save().wait_sleep(1).get_the_first_day_ofentry()
        assert result == str(data["expect"])

    @pytest.mark.parametrize("data", test_edit_date_of_entry_datas)
    def test_edit_date_of_entry(self,data):
        '''
        验证编辑教职工入职日期、休假類型
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver(). \
            edit_vacation_type(data["vacation_type"]).\
            edit_date_of_entry(data["entrydate"]).\
            click_save().wait_sleep(1).get_the_first_day_ofentry()
        assert result == str(data["expect"])

    @pytest.mark.parametrize("data", test_get_superior_and_supervisor_datas)
    def test_get_superior_and_supervisor(self,data):
        '''
        验证獲取員工的上級、主管
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).get_the_fir_superior_and_supervisor()
        assert result == True

    @pytest.mark.parametrize("data", test_get_superior_datas)
    def test_edit_superior(self,data):
        '''
        验证修改員工的上級
        '''
        result = self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver().\
            edit_superior().choise_staff(data["user"]).click_save().\
            goto_approver_information_details().click_save().\
            wait_sleep(1).get_the_fir_superior_and_supervisor()
        assert data["user"] in result

    @pytest.mark.parametrize("data", test_edit_superior_and_supervisor_datas)
    def test_edit_superior_and_supervisor(self,data):
        '''
        验证修改員工的上級和主管
        '''
        self.main.goto_approver_information_table(). \
            keywords_search(data["keywords"]).click_search_button(). \
            wait_sleep(1).edit_the_first_approver().\
            edit_superior().choise_staff(data["superior"]).click_save(). \
            goto_approver_information_details().\
            edit_supervisor().choise_staff(data["supervisor"]).click_save(). \
            goto_approver_information_details().click_save().\
            wait_sleep(1).get_the_fir_superior_and_supervisor()
        db = shelve.open("leave_approver")
        pytest.assume( data["superior"] in db["leave_approver"])
        pytest.assume( data["supervisor"] in db["leave_approver"])
        db.close()

    @pytest.mark.parametrize("data", test_get_user_information_datas)
    def test_get_user_information(self,data):
        '''
        验证获取员工的上級、主管、休假類型、上一年度帶假、年假結余天數、入職日期、離職日期
        '''
        result = self.main.goto_approver_information_table(). \
            get_the_fir_information(data["user_list"])
        assert result == True

