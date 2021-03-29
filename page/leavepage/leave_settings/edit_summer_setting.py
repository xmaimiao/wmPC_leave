from common.contants import edit_summer_setting_dir
from page.basepage import BasePage
from page.select_leave_type import Select_Leave_Type


class Edit_Summer_Setting(BasePage):
    def edit_for_people(self):
        '''
        编辑適用人群
        '''
        self.step(edit_summer_setting_dir,"edit_for_people")
        return Select_Leave_Type(self._driver)

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
