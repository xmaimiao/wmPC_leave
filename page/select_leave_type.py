from common.contants import select_leave_type_dir
from page.basepage import BasePage


class Select_Leave_Type(BasePage):


    def add_leave_type(self,type_list):
        '''
        添加休假類型
        '''
        # 獲取已有的適用人群
        for leave_type in type_list:
            self._params["leave_type"] = leave_type
            eles = self.step(select_leave_type_dir,"send_and_get_types")
            for ele in eles:
                if ele.text == leave_type:
                    self._params["ele_id"] = ele.get_attribute("id")
                    self.step(select_leave_type_dir,"add_leave_type")
        return self

    def del_leave_type(self,type_list):
        '''
        刪除休假類型
        '''
        for leave_type in type_list:
            self._params["leave_type"] = leave_type
            eles = self.step(select_leave_type_dir, "del_send_and_get_types")
            for ele in eles:
                if ele.text == leave_type:
                    self._params["ele_id"] = ele.get_attribute("id")
                    self.step(select_leave_type_dir, "del_leave_type")
        return self

    def click_save(self):
        self.step(select_leave_type_dir, "click_save")
        return self

    def goto_add_or_edit_holiday(self):
        '''
        返囘编辑/添加有薪年假页面
        '''
        from page.leavepage.leave_settings.add_or_edit_holiday import Add_Or_Edit_Holiday
        return Add_Or_Edit_Holiday(self._driver)

    def goto_edit_holiday_period(self):
        '''
        返回編輯假期周期頁面
        '''
        from page.leavepage.leave_settings.edit_holiday_period import Edit_Holiday_Period
        return Edit_Holiday_Period(self._driver)

    def goto_edit_summer_setting(self):
        '''
        返回編輯暑期設置頁面
        '''
        from page.leavepage.leave_settings.edit_summer_setting import Edit_Summer_Setting
        return Edit_Summer_Setting(self._driver)

    def goto_rest_day(self):
        '''
        返回休息日頁面
        '''
        from page.leavepage.leave_settings.rest_day import Rest_Day
        return Rest_Day(self._driver)

    def goto_public_holiday_details(self):
        '''
        返回公众假编辑頁面
        '''
        from page.leavepage.leave_settings.public_holiday_details import Public_Holiday_Details
        return Public_Holiday_Details(self._driver)

    def goto_worktime_setting(self):
        '''
        返回工作時間設置编辑頁面
        '''
        from page.leavepage.leave_settings.worktime_setting_details import Worktime_Setting_Details
        return Worktime_Setting_Details(self._driver)
