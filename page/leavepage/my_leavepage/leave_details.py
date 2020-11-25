import re

from common.contants import leave_details_dir
from page.basepage import BasePage


class Leave_Details(BasePage):
    def get_first_object_status(self):
        '''
        獲取第一行請假單的狀態，驗證審批成功
        '''
        return self.step(leave_details_dir,"get_first_object_status")


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

    def get_leave_total(self):
        '''
        獲取休假申请单的数量
        '''
        total =  self.step(leave_details_dir,"get_leave_total")
        print(f"休假记录：{total}")
        return int(re.search("(\d+).*?(\d+).*", total).group(1))

