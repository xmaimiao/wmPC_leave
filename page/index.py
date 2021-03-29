from common.contants import index_dir
from page.OA_approvel.all_approvals.OA_approvalPage import OA_Approval
from page.application import Application
from page.basepage import BasePage


class Index(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def goto_application(self):
        self.step(index_dir,"goto_application")
        return Application(self._driver)

    def goto_OA_approval(self):
        '''
        在首頁中中進入OA審批
        '''
        self.step(index_dir,"goto_OA_approval")
        return OA_Approval(self._driver)


    def quit(self):
        '''
        推出當前登陸賬號
        :return:
        '''
        self.step(index_dir,"quit")

    def get_index_ele_fir(self):
        '''
        獲取應用-“首頁”元素，驗證登錄成功，一期
        '''
        return self.step(index_dir,"get_index_ele_fir")

    def get_index_ele_sec(self):
        '''
        獲取應用-“首頁”元素，驗證登錄成功，二期
        '''
        return self.step(index_dir,"get_index_ele_sec")

    def get_imformation_ele_index(self):
        '''
        獲取"系統消息"ele，驗證跳轉首頁正確
        '''
        try:
            return self.step(index_dir,"get_imformation_ele_index")
        except Exception as e:
            return False