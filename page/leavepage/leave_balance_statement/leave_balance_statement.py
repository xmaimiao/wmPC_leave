from common.contants import leave_balance_statement_dir
from page.basepage import BasePage


class Leave_Balance_Statement(BasePage):
    def keywords_search(self,keywords):
        '''
        关键词查询
        '''
        self._params["keywords"] = keywords
        self.step(leave_balance_statement_dir,"keywords_search")
        return self

    def click_search(self):
        '''
        点击查询按钮
        '''
        self.step(leave_balance_statement_dir,"click_search")
        return self

    def get_the_first_Balance_days(self):
        '''
        获取历史结余天数
        '''
        return self.step(leave_balance_statement_dir,"get_the_first_Balance_days")

    def get_the_first_Days_Remaining_in_that_year(self):
        '''
        获取當年可休天數
        '''
        return self.step(leave_balance_statement_dir,"get_the_first_Days_Remaining_in_that_year")

    def get_the_first_rest_in_that_year(self):
        '''
        获取當年已休天數
        '''
        return self.step(leave_balance_statement_dir,"get_the_first_rest_in_that_year")

    def get_the_first_Balance_days_AL(self):
        '''
        获取年假結余天數
        '''
        return self.step(leave_balance_statement_dir,"get_the_first_Balance_days_AL")