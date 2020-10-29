from common.contants import set_HR_approver_dir
from page.basepage import BasePage


class Set_HR_Approver(BasePage):
    '''
    HR审批人员设置主页面
    '''
    def goto_edit_xingzhen_HR(self):
        '''
        點擊編輯行政人員年假
        '''
        self.step(set_HR_approver_dir,"goto_edit_xingzhen_HR")
        return Edit_Xingzhen_HR(self._driver)


    def goto_edit_jiaoyan_HR(self):
        '''
        點擊編輯行政人員年假
        '''
        self.step()
        return Edit_Jiaoyan_HR(self._driver)