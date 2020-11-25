import json

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

    def get_holiday_period_all(self):
        '''
        获取所有的假期周期信息：週期名稱、開始日期、結束日期、	適用人群
        '''
        try:
            holiday_period_list=[]
            holiday_period_total = self.step(holiday_period_dir,"get_holiday_period_total")
            for i in range(1,int(holiday_period_total)+1):
                self._params["i"] = i
                holiday_period = {}
                holiday_period["Period_name"] = self.step(holiday_period_dir, "get_Period_name")
                holiday_period["start_date"] = self.step(holiday_period_dir,"get_start_date")
                holiday_period["end_date"] = self.step(holiday_period_dir,"get_end_date")
                holiday_period["for_people"] = self.step(holiday_period_dir,"get_for_people")
                holiday_period_list.append(holiday_period)
            print(json.dumps(holiday_period_list,indent=4,ensure_ascii=False))
            return True
        except Exception as e:
            return False