import re

from common.contants import application_records_for_HR_dir
from page.basepage import BasePage
from page.leavepage.leave_approval_HR.cancellation_leave_details_HR import Cancellation_leave_Details


class Application_Records_For_HR(BasePage):

    def sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def order_by_submission_time(self):
        '''
        调整数据按照 提交时间 顺序显示
        '''
        self.step(application_records_for_HR_dir,"order_by_submission_time")
        return self

    def the_first_cancellation_of_leave(self):
        '''
        对第一条数据进行销假处理，点击销假
        '''
        self.step(application_records_for_HR_dir,"the_first_cancellation_of_leave")
        return Cancellation_leave_Details(self._driver)

    def get_the_first_days_of_leave(self):
        '''
        获取第一条数据的请假天数
        '''
        result = self.step(application_records_for_HR_dir,"get_the_first_days_of_leave")
        print(result)
        return re.search("^(\d+\.\d+).*", result).group(1)

    def get_the_leaveSn_for_cancellation(self,leaveSn):
        '''
        根据请假单编号获取数据，并点击销假
        '''
        self._params["leaveSn"] = leaveSn
        self.step(application_records_for_HR_dir,"get_the_leaveSn_for_cancellation")
        return Cancellation_leave_Details(self._driver)