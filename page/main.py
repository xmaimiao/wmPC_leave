import yaml
from common.contants import leavepage_dir, main1_dir, basepage_dir
from page.OA_approvel.OA_approvalPage import OA_Approval
from page.basepage import BasePage, _get_working
from page.index import Index
from page.leavepage.Approver_information_table.approver_information_table import Approver_Information_Table
from page.leavepage.leave_approval_HR.leave_approval_HR import Leave_Approval_HR
from page.leavepage.leave_balance_statement.leave_balance_statement import Leave_Balance_Statement
from page.leavepage.leave_search.leave_search import Leave_Search
from page.leavepage.leave_settings.leave_settings import Leave_Settings
from page.leavepage.staff_application_for_Leave_HR.staff_application_for_Leave_HR import Staff_Application_For_Leave_HR
from page.loginpage import Login

class Main(BasePage):
    '''
    首頁面po
    '''
    _working = _get_working()

    with open(basepage_dir, encoding="utf-8") as f:
        env = yaml.safe_load(f)
        if _working != "port":
            _base_url = env["docker_env"][env["default"]]

    def goto_login(self):
        '''
        進去登錄頁面
        :return:
        '''
        return Login(self._driver)

    def goto_index(self):
        '''
        打開首頁
        '''
        return Index(self._driver)


    def goto_application_for_leaver(self):
        '''
        測試入口，打開申請休假菜單
        '''
        self.set_implicitly_wait(5)
        self.step(leavepage_dir,"goto_application_for_leaver")
        from page.leavepage.leave_application.application_for_leave import Application_For_Leaver
        return Application_For_Leaver(self._driver)

    def goto_OA_Approval(self):
        '''
        在請假中進入OA審批
        '''
        self.step(main1_dir,"goto_OA_Approval")
        return OA_Approval(self._driver)

    def goto_my_leave(self):
        '''
        打開我的休假菜單
        '''
        self.step(leavepage_dir,"goto_my_leave")
        from page.leavepage.my_leavepage.may_leavePage import My_Leave
        return My_Leave(self._driver)

    def goto_approver_information_table(self):
        '''
        打開人員信息表
        '''
        self.step(leavepage_dir,"goto_approver_information_table")
        return Approver_Information_Table(self._driver)

    def goto_leave_balance_statement(self):
        '''
        打开假期结余报表
        '''
        self.step(leavepage_dir,"goto_leave_balance_statement")
        return Leave_Balance_Statement(self._driver)

    def goto_staff_application_for_leave_HR(self):
        '''
        打開HR代申请页面
        '''
        self.step(leavepage_dir,"goto_staff_application_for_leave_HR")
        return Staff_Application_For_Leave_HR(self._driver)

    def goto_leave_approval_HR(self):
        '''
        打開HR审批页面
        '''
        self.step(leavepage_dir,"goto_leave_approval_HR")
        return Leave_Approval_HR(self._driver)


    def goto_leave_settings(self):
        '''
        打開休假設置
        '''
        self.step(leavepage_dir,"goto_leave_settings")
        return Leave_Settings(self._driver)

    def goto_leave_search(self):
        '''
        打開休假查询
        '''
        self.step(leavepage_dir,"goto_leave_search")
        return Leave_Search(self._driver)
