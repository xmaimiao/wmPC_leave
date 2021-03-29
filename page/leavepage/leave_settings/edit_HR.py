from common.contants import edit_HR_dir
from page.basepage import BasePage
from page.select_staff import Select_Staff


class Edit_HR(BasePage):

   def click_select_check(self):
       '''
       點擊審核人員“請選擇”按鈕，打開選擇人員的抽屜
       :return:
       '''
       self.step(edit_HR_dir,"click_select_check")
       return Select_Staff(self._driver)

   def click_select_approver(self):
       '''
       點擊審批人員“請選擇”按鈕，打開選擇人員的抽屜
       :return:
       '''
       self.step(edit_HR_dir,"click_select_approver")
       return Select_Staff(self._driver)

   def click_save(self):
       '''
       點擊“確認”按鈕，保存HR設置
       '''
       self.step(edit_HR_dir,"click_save")
       from page.leavepage.leave_settings.set_HR_approver import Set_HR_Approver
       return Set_HR_Approver(self._driver)