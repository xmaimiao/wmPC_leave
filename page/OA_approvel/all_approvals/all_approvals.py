from page.OA_approvel.all_approvals.approved_OA import Approved_OA
from page.OA_approvel.all_approvals.pending_for_approval_OA import Pending_For_Approval_OA
from page.basepage import BasePage
from common.contants import all_approvals_dir



class ALL_Approvals_OA(BasePage):

    def goto_pending_for_approval_OA(self):
        '''
        打開待審批頁面
        '''
        # self.step(all_approvals_dir,"goto_pending_for_approval_OA")
        return Pending_For_Approval_OA(self._driver)

    def goto_approved_OA(self):
        '''
        打開已審批頁面
        '''
        self.step(all_approvals_dir,"goto_approved_OA")
        return Approved_OA(self._driver)