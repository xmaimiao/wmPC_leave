from common.contants import holiday_period_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.edit_holiday_period import Edit_Holiday_Period


class Holiday_Period(BasePage):
    '''
    假期周期页面
    '''
    def edit_holiday_period(self,period_name):
        '''
        編輯假期周期，根據傳進來的“周期名稱”定位編輯的數據
        '''
        self._params["period_name"] = period_name
        self.step(holiday_period_dir,"edit_holiday_period")
        return Edit_Holiday_Period(self._driver)

    def get_ele_of_add(self):
        '''
        获取”添加“元素，验证编辑成功，返回默认页面
        '''
        return self.step(holiday_period_dir, "get_ele_of_add")