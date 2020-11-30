import json

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

    def get_the_fir_AL_infomation(self):
        '''
        獲取年假的基本信息
        '''
        try:
            AL_info = {}
            AL_info["历史结余天数"] = self.step(leave_balance_statement_dir,"get_the_first_Balance_days")
            AL_info["當年可休天數"] = self.step(leave_balance_statement_dir,
                                            "get_the_first_Days_Remaining_in_that_year")
            AL_info["當年已休天數"] = self.step(leave_balance_statement_dir,"get_the_first_rest_in_that_year")
            AL_info["年假結余天數"] = self.step(leave_balance_statement_dir,"get_the_first_Balance_days_AL")
            print(json.dumps(AL_info,indent=4,ensure_ascii=False))
            return True
        except Exception as e:
            return False
