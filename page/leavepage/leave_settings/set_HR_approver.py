from common.contants import set_HR_approver_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.edit_xingzheng_AL_HR import Edit_Xingzheng_AL_HR


class Set_HR_Approver(BasePage):
    '''
    HR审批人员设置主页面
    '''
    def goto_edit_xingzheng_AL_HR(self):
        '''
        點擊編輯行政人員年假
        '''
        self.step(set_HR_approver_dir,"goto_edit_xingzheng_AL_HR")
        return Edit_Xingzheng_AL_HR(self._driver)

    def get_xingzheng_AL_HR(self):
        '''
        獲取行政人員年假HR
        '''
        try:
            HR = self.step(set_HR_approver_dir,"get_xingzheng_AL_HR")
            print(f"行政年假HR：{HR}")
            return True
        except Exception as e:
            return False


    def goto_edit_jiaoyan_AL_HR(self):
        '''
        點擊編輯教研人員年假
        '''
        self.step(set_HR_approver_dir,"goto_edit_jiaoyan_AL_HR")
        return Edit_Jiaoyan_AL_HR(self._driver)

    def get_jiaoyan_AL_HR(self):
        '''
        獲取教研人員年假HR
        '''
        try:
            HR = self.step(set_HR_approver_dir,"get_jiaoyan_AL_HR")
            print(f"教研年假HR：{HR}")
            return True
        except Exception as e:
            return False