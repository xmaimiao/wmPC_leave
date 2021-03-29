import re

from common.contants import leave_search_dir
from page.basepage import BasePage


class Leave_Search(BasePage):
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def simple_search(self,user):
        '''
        简易查询 老师账号
        '''
        self._params["user"] = user
        self.step(leave_search_dir,"simple_search")
        return self

    def click_search(self):
        self.step(leave_search_dir,"click_search")
        return self

    def get_current_leave_total(self):
        '''
        获取当前的请假数量，总数量
        '''
        total = self.step(leave_search_dir,"get_current_leave_total")
        print(total)
        return int(re.search("(\d+).*?(\d+).*", total).group(1))