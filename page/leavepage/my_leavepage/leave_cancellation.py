from common.contants import leave_cancellation_dir
from page.basepage import BasePage


class Leave_Cancellation(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def choose_all(self):
        '''
        點擊“全選”
        '''
        self.step(leave_cancellation_dir,"choose_all")
        return self

    def leave_cancellation(self,date_type_list):
        '''
        非全選，傳進來銷假數據[{date:'2020/12/19',type:'全天'},]  [{銷假日期：xx,銷假類型:xx},]
        '''
        for date_type in date_type_list:
            self._params["date"] = date_type["date"]
            self._params["type"] = date_type["type"]
            self.step(leave_cancellation_dir,"leave_cancellation")
        return self

    def remark(self,remark):
        '''
        填寫備注
        '''
        self._params["remark"] = remark
        self.step(leave_cancellation_dir,"remark")
        return self

    def clcik_save(self):
        self.step(leave_cancellation_dir,"clcik_save")
        from page.leavepage.my_leavepage.leave_overview import Leave_OverView
        return Leave_OverView(self._driver)

    def clcik_save_backto_records(self):
        self.step(leave_cancellation_dir, "clcik_save")
        from page.leavepage.my_leavepage.substitute_leave_records import Substitute_Leave_Records
        return Substitute_Leave_Records(self._driver)