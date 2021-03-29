from page.basepage import BasePage
from common.contants import leavepage_dir
from page.leavepage.Approver_information_table.approver_information_table import Approver_Information_Table
from page.leavepage.leave_application.application_for_leave import Application_For_Leaver
from page.leavepage.leave_approval.leave_approval import Leave_Approval
from page.leavepage.leave_approval_HR.leave_approval_HR import Leave_Approval_HR
from page.leavepage.leave_balance_statement.leave_balance_statement import Leave_Balance_Statement
from page.leavepage.leave_search.leave_search import Leave_Search
from page.leavepage.leave_settings.leave_settings import Leave_Settings
from page.leavepage.my_leavepage.may_leavePage import My_Leave
from page.leavepage.staff_application_for_Leave_HR.staff_application_for_Leave_HR import Staff_Application_For_Leave_HR


class LeavePage(BasePage):

    def goto_application_for_leaver(self):
        '''
        打開申請休假頁面
        '''
        self.step(leavepage_dir,"goto_application_for_leaver")
        return Application_For_Leaver(self._driver)

    def goto_my_leave(self):
        '''
        打開我的休假菜單
        '''
        self.step(leavepage_dir,"goto_my_leave")
        return My_Leave(self._driver)

    def goto_staff_application_for_leave_HR(self):
        '''
        打開HR代申请页面
        '''
        self.step(leavepage_dir,"goto_staff_application_for_leave_HR")
        return Staff_Application_For_Leave_HR(self._driver)

    def goto_leave_approval_HR(self):
        '''
        打開休假审批HR页面
        '''
        self.step(leavepage_dir,"goto_leave_approval_HR")
        return Leave_Approval_HR(self._driver)

    def goto_leave_approval(self):
        '''
        打開休假审批页面
        '''
        self.step(leavepage_dir,"goto_leave_approval")
        return Leave_Approval(self._driver)

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
