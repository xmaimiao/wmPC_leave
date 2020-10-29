from common.contants import edit_holiday_period_dir
from page.basepage import BasePage


class Edit_Holiday_Period(BasePage):
    '''
    编辑假期周期页面
    '''
    def edit_for_people(self,leave_type):
        '''
        編輯適用人群
        '''
        if leave_type in self._driver.page_source:
            pass
        else:
            self._params["leave_type"] = leave_type
            self.step(edit_holiday_period_dir,"edit_for_people")
        return self

    def click_save(self):
        self.step(edit_holiday_period_dir,"click_save")
        from page.leavepage.leave_settings.holiday_period import Holiday_Period
        return Holiday_Period(self._driver)