from common.contants import leave_approval_dir
from page.basepage import BasePage
from page.leavepage.leave_approval.approved import Approved
from page.leavepage.leave_approval.pending_for_approval import Pending_For_Approval


class Leave_Approval(BasePage):
    def goto_pending_for_approval(self):
        '''
        打开HR待审批页面
        '''
        self.step(leave_approval_dir, "goto_pending_for_approval")
        return Pending_For_Approval(self._driver)

    def goto_approved_HR(self):
        '''
        打开HR已审批页面
        '''
        self.step(leave_approval_dir, "goto_approved")
        return Approved(self._driver)
