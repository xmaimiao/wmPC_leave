from common.contants import my_leave_dir
from page.basepage import BasePage
from page.leavepage.my_leavepage.leave_details import Leave_Details
from page.leavepage.my_leavepage.leave_overview import Leave_OverView


class My_Leave(BasePage):
    def goto_leave_overview(self):
        '''
        打開休假概覽tab
        '''
        return Leave_OverView(self._driver)

    def goto_leave_details(self):
        '''
        打開休假明細tab
        '''
        self.step(my_leave_dir,"goto_leave_details")
        return Leave_Details(self._driver)