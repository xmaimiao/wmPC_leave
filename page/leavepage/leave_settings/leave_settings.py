from common.contants import leave_settings_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.holiday_period import Holiday_Period
from page.leavepage.leave_settings.paid_Annual_Leave import Paid_Annual_Leave
from page.leavepage.leave_settings.public_holiday import Public_Holiday
from page.leavepage.leave_settings.rest_day import Rest_Day
from page.leavepage.leave_settings.set_HR_approver import Set_HR_Approver
from page.leavepage.leave_settings.summer_workday_setting import Summer_Workday_Setting
from page.leavepage.leave_settings.worktime_setting import Worktime_Setting


class Leave_Settings(BasePage):
    '''
    休假设置主页面
    '''
    def goto_set_HR_approver(self,setting):
        '''
        打開HR審批人設置
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_set_HR_approver")
        return Set_HR_Approver(self._driver)

    def goto_rest_day(self,setting):
        '''
        打開休息日
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_rest_day")
        return Rest_Day(self._driver)

    def goto_public_holiday(self,setting):
        '''
        打開公衆假
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_public_holiday")
        return Public_Holiday(self._driver)

    def goto_worktime_setting(self,setting):
        '''
        打開工作時間設置
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_worktime_setting")
        return Worktime_Setting(self._driver)

    def goto_summer_workday_setting(self,setting):
        '''
        打開暑期設置
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_summer_workday_setting")
        return Summer_Workday_Setting(self._driver)

    def goto_paid_Annual_Leave(self,setting):
        '''
        打開有薪年假設置
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_paid_Annual_Leave")
        return Paid_Annual_Leave(self._driver)

    def goto_holiday_period(self,setting):
        '''
        打開假期周期設置
        :param setting: 設置的名稱
        '''
        self._params["setting"] = setting
        self.step(leave_settings_dir,"goto_holiday_period")
        return Holiday_Period(self._driver)