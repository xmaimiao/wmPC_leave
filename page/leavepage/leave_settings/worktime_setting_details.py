from common.contants import worktime_setting_details_dir
from page.basepage import BasePage
from page.select_leave_type import Select_Leave_Type


class Worktime_Setting_Details(BasePage):

    def edit_rule_name(self,rule_name):
        self._params["rule_name"] = rule_name
        self.step(worktime_setting_details_dir,"edit_rule_name")
        return self

    def edit_start_date(self,starttime):
        '''
        修改開始時間
        '''
        self._params["starttime"] = starttime
        self.step(worktime_setting_details_dir,"edit_start_date")
        return self

    def edit_end_date(self,endtime):
        '''
        修改結束時間，僅修改小時
        '''
        self._params["endtime"] = endtime
        self.step(worktime_setting_details_dir,"edit_end_date")
        return self

    def for_people(self):
        '''
        修改適用人群
        '''
        self.step(worktime_setting_details_dir,"for_people")
        return Select_Leave_Type(self._driver)

    def click_save(self):
        self.step(worktime_setting_details_dir,"click_save")
        from page.leavepage.leave_settings.worktime_setting import Worktime_Setting
        return Worktime_Setting(self._driver)