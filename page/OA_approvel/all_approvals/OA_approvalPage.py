from page.OA_approvel.all_approvals.all_approvals import ALL_Approvals_OA
from page.basepage import BasePage
from common.contants import OA_approvalPage_dir


class OA_Approval(BasePage):

    def goto_ALL_approvals_OA(self):
        '''
        打開全部審批菜單
        '''
        self.step(OA_approvalPage_dir,"goto_ALL_approvals_OA")
        return ALL_Approvals_OA(self._driver)

    def get_ele_of_ALL_approvals_OA(self):
        '''
        获取元素：全部審批菜單，验证跳转正确用
        '''
        return self.step(OA_approvalPage_dir,"get_ele_of_ALL_approvals_OA")

