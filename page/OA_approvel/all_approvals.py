from common.contants import all_approvals_dir
from page.OA_approvel.pending_for_approval_OA import Pending_For_Approval
from page.basepage import BasePage


class ALL_Approvals(BasePage):

    def goto_pending_for_approval(self):
        '''
        打開待審批頁面
        '''
        return Pending_For_Approval(self._driver)

    def goto_approved(self):
        '''
        打開已審批頁面
        '''
        self.step(all_approvals_dir,"goto_approved")
        return