from common.contants import edit_holiday_period_dir
from page.basepage import BasePage
from page.select_leave_type import Select_Leave_Type


class Edit_Holiday_Period(BasePage):
    '''
    编辑假期周期页面
    '''
    def edit_for_people(self):
        '''
        編輯適用人群
        '''
        self.step(edit_holiday_period_dir,"edit_for_people")
        return Select_Leave_Type(self._driver)

    def click_save(self):
        self.step(edit_holiday_period_dir,"click_save")
        from page.leavepage.leave_settings.holiday_period import Holiday_Period
        return Holiday_Period(self._driver)