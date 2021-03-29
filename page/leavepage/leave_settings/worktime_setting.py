from common.contants import worktime_setting_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.worktime_setting_details import Worktime_Setting_Details


class Worktime_Setting(BasePage):
    def edit_the_fir(self):
        '''
        編輯第一條規則
        '''
        self.step(worktime_setting_dir,"edit_the_fir")
        return Worktime_Setting_Details(self._driver)

    def add_rule(self):
        '''
        添加規則
        '''
        self.step(worktime_setting_dir,"add_rule")
        return Worktime_Setting_Details(self._driver)

    def get_ele_of_add(self):
        '''
        獲取添加元素
        '''
        try:
            self.step(worktime_setting_dir,"get_ele_of_add")
            return True
        except Exception as e:
            return False