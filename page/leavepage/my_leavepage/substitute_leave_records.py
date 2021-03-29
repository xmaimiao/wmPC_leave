from common.contants import substitute_leave_records_dir
from page.basepage import BasePage
from page.leavepage.my_leavepage.leave_cancellation import Leave_Cancellation


class Substitute_Leave_Records(BasePage):
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def get_ele_of_tab_title(self):
        return self.step(substitute_leave_records_dir,"get_ele_of_tab_title")

    def goto_the_fir_leave_cancellation_records(self):
        '''
        打開銷假頁面
        '''
        try:
            self.step(substitute_leave_records_dir, "goto_the_fir_leave_cancellation_records")
            return Leave_Cancellation(self._driver)
        except Exception as e:
            print("無銷假按鈕！")

    def get_the_fir_status(self):
        '''
        获取第一条数据的状态
        '''

        return self.step(substitute_leave_records_dir, "get_the_fir_status")
