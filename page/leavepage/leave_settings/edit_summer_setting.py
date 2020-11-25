from common.contants import edit_summer_setting_dir
from page.basepage import BasePage


class Edit_Summer_Setting(BasePage):
    def edit_for_people(self,leave_type):
        '''
        编辑適用人群
        :param leave_type:传参，休假类型
        '''
        if leave_type in self._driver.page_source:
            pass
        else:
            self._params["leave_type"] = leave_type
            self.step(edit_summer_setting_dir,"edit_for_people")
        return self

    def click_save(self):
        self.step(edit_summer_setting_dir, "click_save")
        from page.leavepage.leave_settings.summer_workday_setting import Summer_Workday_Setting
        return Summer_Workday_Setting(self._driver)

    def edit_start_date(self,start_date):
        '''
        修改开始日期
        '''
        self._params["start_date"] = start_date
        self.step(edit_summer_setting_dir, "edit_start_date")
        return self

    def edit_end_date(self,end_date):
        '''
        修改结束日期
        '''
        self._params["end_date"] = end_date
        self.step(edit_summer_setting_dir, "edit_end_date")
        return self
