from common.contants import leave_approval_HR_dir
from page.basepage import BasePage
from page.leavepage.leave_approval_HR.application_records_for_HR import Application_Records_For_HR
from page.leavepage.leave_approval_HR.approved_HR import Approved_HR


class Leave_Approval_HR(BasePage):
    def goto_pending_for_approval_HR(self):
        '''
        打开HR待审批页面
        '''
        self.step(leave_approval_HR_dir,"goto_pending_for_approval_HR")
        from page.OA_approvel.pending_for_approval_OA import Pending_For_Approval
        return Pending_For_Approval(self._driver)

    def goto_approved_HR(self):
        '''
        打开HR已审批页面
        '''
        self.step(leave_approval_HR_dir,"goto_approved_HR")
        return Approved_HR(self._driver)

    def goto_application_records_for_HR(self):
        '''
        打开HR代请假记录页面
        '''
        self.step(leave_approval_HR_dir,"goto_application_records_for_HR")
        return Application_Records_For_HR(self._driver)