import re

from common.contants import approved_HR_dir
from page.basepage import BasePage


class Approved_HR(BasePage):
    def get_the_first_days_of_leave_Apppage(self):
        '''
        获取第一条数据的请假天数
        '''
        result = self.step(approved_HR_dir, "get_the_first_days_of_leave_Apppage")
        return re.search("^(\d+\.\d+).*", result).group(1)
