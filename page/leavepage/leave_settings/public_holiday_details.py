from common.contants import public_holiday_details_dir
from page.basepage import BasePage
from page.select_leave_type import Select_Leave_Type


class Public_Holiday_Details(BasePage):

    def edit_name(self,rule_name):
        self._params["rule_name"] = rule_name
        self.step(public_holiday_details_dir,"edit_name")
        return self

    def edit_Enname(self,rule_Enname):
        self._params["rule_Enname"] = rule_Enname
        self.step(public_holiday_details_dir,"edit_Enname")
        return self

    def edit_startday(self,startday):
        self._params["startday"] = startday
        self.step(public_holiday_details_dir,"edit_startday")
        return self

    def edit_endday(self,endday):
        self._params["endday"] = endday
        self.step(public_holiday_details_dir,"edit_endday")
        # 切換到iframe
        self._driver.switch_to.frame(0)
        self.step(public_holiday_details_dir, "click_perform")
        return self

    def is_this_half_day_leave(self,half_day):
        '''
        半天假
        '''
        self.step(public_holiday_details_dir, "is_this_half_day_leave")
        if half_day == "下午":
            self.step(public_holiday_details_dir,"half_day")
        return self

    def mandatory_holiday(self):
        '''
        强制性假期
        '''
        self.step(public_holiday_details_dir,"mandatory_holiday")
        return self

    def for_people(self):
        '''
        选择非适用人群
        '''
        self.step(public_holiday_details_dir,"for_people")
        return Select_Leave_Type(self._driver)

    def click_save(self):
        '''
        點擊”確認“
        '''
        self.step(public_holiday_details_dir,"click_save")
        from page.leavepage.leave_settings.public_holiday import Public_Holiday
        return Public_Holiday(self._driver)