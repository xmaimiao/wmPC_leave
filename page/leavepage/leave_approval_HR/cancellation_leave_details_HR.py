from common.contants import cancellation_leave_details_HR_dir
from page.basepage import BasePage


class Cancellation_leave_Details(BasePage):

    def choose_all(self):
        '''
        选择销假全部
        '''
        self.step(cancellation_leave_details_HR_dir,"choose_all")
        return self

    def click_save(self):
        self.step(cancellation_leave_details_HR_dir,"click_save")
        from page.leavepage.leave_approval_HR.application_records_for_HR import Application_Records_For_HR
        return Application_Records_For_HR(self._driver)
