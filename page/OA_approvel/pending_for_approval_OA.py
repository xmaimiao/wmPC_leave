from common.contants import pending_for_approval_OA_dir
from page.basepage import BasePage
from page.leavepage.leavepage import LeavePage


class Pending_For_Approval(BasePage):
    def the_first_subject(self):
        '''
        打開第一行申請單詳情頁,請假詳情專用
        '''
        self.step(pending_for_approval_OA_dir,"the_first_subject")
        from page.OA_approvel.OA_leave_details import OA_Leave_Details
        return OA_Leave_Details(self._driver)


    def goto_leave_application(self,application):
        '''
        打開請假應用
        :return: 傳進來應用名稱，根據名稱定位
        '''
        self._params["application"] = application
        self.step(pending_for_approval_OA_dir,"goto_leave_application")
        return LeavePage(self._driver)