from common.contants import public_holiday_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.public_holiday_details import Public_Holiday_Details


class Public_Holiday(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def create_rule(self):
        '''
        创建公众假
        '''
        self.step(public_holiday_dir,"create_rule")
        return Public_Holiday_Details(self._driver)

    def get_ele_of_add(self):
        '''
        獲取”添加“元素
        '''
        try:
            self.step(public_holiday_dir,"get_ele_of_add")
            return True
        except Exception as e:
            return False

    def edit_rule_for_name(self,rule_name):
        '''
        通過傳入的規則名稱定位數據 ，點擊“編輯”按鈕
        '''
        self._params["rule_name"] = rule_name
        self.step(public_holiday_dir,"edit_rule_for_name")
        return Public_Holiday_Details(self._driver)

    def get_exceptional_group_for_name(self,rule_name):
        '''
        通過規則名稱定位數據，獲取例外人群
        '''
        self._params["rule_name"] = rule_name
        return self.step(public_holiday_dir,"get_exceptional_group_for_name")