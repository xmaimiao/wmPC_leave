from common.contants import rest_day_dir
from page.basepage import BasePage
from page.select_leave_type import Select_Leave_Type


class Rest_Day(BasePage):

    def edit_rest_day_staff_for_name(self,week):
        '''
        通過星期一定位 第X條數據，點擊”編輯“按鈕，編輯適用人群
        '''
        self._params["week"] = week
        self.step(rest_day_dir,"edit_rest_day_staff_for_name")
        return Select_Leave_Type(self._driver)

    def get_staff_for_name(self,week):
        '''
        通過星期一定位 第X條數據，獲取適用人群
        '''
        self._params["week"] = week
        return self.step(rest_day_dir,"get_staff_for_name")
