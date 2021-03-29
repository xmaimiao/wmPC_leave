from common.contants import OA_leave_details_dir
from page.OA_approvel.all_approvals.pending_for_approval_OA import Pending_For_Approval_OA
from page.basepage import BasePage


class OA_Leave_Details(BasePage):
    def approved(self):
        '''
        點擊同意
        '''
        self.step(OA_leave_details_dir,"approved")
        return Pending_For_Approval_OA(self._driver)

    def not_approved(self):
        '''
        點擊不同意
        '''
        self.step(OA_leave_details_dir,"not_approved")
        return Pending_For_Approval_OA(self._driver)

    def remarks(self,remarks):
        '''
        填寫不批准意見
        '''
        self._params["remarks"] = remarks
        self.step(OA_leave_details_dir,"remarks")
        return self

    def reminder_of_supplement(self):
        '''
        点击“资料补充提醒”按钮,获取成功toast返回
        关闭详情页
        '''
        toast_tatus = self.step(OA_leave_details_dir,"reminder_of_supplement")
        self.sleep(3)
        self.step(OA_leave_details_dir, "close_page")
        return toast_tatus



