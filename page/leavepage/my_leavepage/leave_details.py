import re

from common.contants import leave_details_dir
from page.basepage import BasePage
from page.leavepage.my_leavepage.leave_cancellation import Leave_Cancellation


class Leave_Details(BasePage):
    def get_first_object_status(self):
        '''
        獲取第一行請假單的狀態，驗證審批成功
        '''
        return self.step(leave_details_dir,"get_first_object_status")

    def get_first_object_Sn(self):
        '''
        獲取第一行請假單的單號
        '''
        try:
            result = self.step(leave_details_dir,"get_first_object_Sn")
            print(f"申請單號：{result}")
            return True
        except Exception as e:
            print("獲取單號失敗！")
            return False

    def cancel_the_first_leave(self):
        '''
        撤銷第一單請假申請
        '''
        try:
            self.step(leave_details_dir,"cancel_the_first_leave")
            return self
        except Exception as e:
            print("第一行数据不可撤销，请检查！")
            raise e

    def cancel_leave_of_number(self,leave_num):
        '''
        根据请假单号撤销休假,并返回该条数据的状态文本：已撤销
        '''
        self._params["leave_num"] = leave_num
        try:
           return self.step(leave_details_dir, "cancel_leave_of_number")
        except Exception as e:
            print("数据不可撤销，请检查！")
            raise e

    def goto_the_fir_leave_cancellation(self):
        '''
        打開銷假頁面
        '''
        try:
            self.step(leave_details_dir, "goto_the_fir_leave_cancellation")
            return Leave_Cancellation(self._driver)
        except Exception as e:
            print("無銷假按鈕！")

    def get_leave_total(self):
        '''
        獲取休假申请单的数量
        '''
        total =  self.step(leave_details_dir,"get_leave_total")
        print(f"休假记录：{total}")
        return int(re.search("(\d+).*?(\d+).*", total).group(1))


