from common.contants import select_staff_dir
from page.basepage import BasePage


class Select_Staff(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def click_clear_button(self):
        '''
        清空已选择人员
        '''
        self.step(select_staff_dir,"click_clear_button")
        return self

    def click_save(self):
        '''
        点击保存按钮
        '''
        self.step(select_staff_dir,"click_save")
        return self

    def choise_staff(self,user,sleeps):
        '''
        选择人员
        :param user: 人员账号账号
        '''
        self._params["user"] = user
        self.step(select_staff_dir,"search_staff")
        # 等待人員出現，dev需要>30s
        self.sleep(sleeps)
        eles = self.step(select_staff_dir,"choise_staff")
        eles[0].click()
        return self

    def delect_staff(self,users):
        '''
        刪除人员
        :param users: 人员账号账号list
        '''
        try:
            for user in users:
                self._params["user"] = user
                # 實現為點擊選人組件右側刪除人員，不足之處沒加滾動定位
                self.step(select_staff_dir,"delect_staff")

                # 先用查詢人員，不足之處查詢人員會很久
                # self.step(select_staff_dir, "search_staff")
                # 等待人員出現，dev需要>30s
                # self.sleep(5)
                # eles = self.step(select_staff_dir, "delect_staff")
                # eles[0].click()

        except Exception as e:
            print("該人員可能不存在！")
        return self


    def goto_staff_application_for_Leave_HR(self):
        '''
        打開HR帶請假頁面
        '''
        from page.leavepage.staff_application_for_Leave_HR.staff_application_for_Leave_HR import \
            Staff_Application_For_Leave_HR
        return Staff_Application_For_Leave_HR(self._driver)

    def goto_approver_information_details(self):
        '''
        打開人員信息表-詳情頁面
        '''
        from page.leavepage.Approver_information_table.approver_information_details import Approver_Information_Details
        return Approver_Information_Details(self._driver)

    def goto_edit_HR_page(self):
        '''
        打開休假設置-HR行政人元編輯頁面
        '''
        from page.leavepage.leave_settings.edit_HR import Edit_HR
        return Edit_HR(self._driver)
