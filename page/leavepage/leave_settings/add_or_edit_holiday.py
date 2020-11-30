from common.contants import add_or_edit_holiday_dir
from page.basepage import BasePage


class Add_Or_Edit_Holiday(BasePage):
    '''
    编辑/添加有薪年假页面
    '''
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def rule_name(self,rule_name):
        '''
        编辑规则名称
        :param rule_name:
        '''
        self._params["rule_name"] = rule_name
        self.step(add_or_edit_holiday_dir,"rule_name")
        return self

    def Annual_starting_point(self,annual_point):
        '''
        编辑有薪年假起點
        :param rule_name:
        '''
        self._params["annual_point"] = annual_point
        self.step(add_or_edit_holiday_dir,"Annual_starting_point")
        return self

    def Maximum_days(self,maxTotal_days):
        '''
        编辑最高享用天數
        :param rule_name:
        '''
        self._params["maxTotal_days"] = maxTotal_days
        self.step(add_or_edit_holiday_dir,"Maximum_days")
        return self

    def Minimum_leave(self,minDay):
        '''
        编辑最小休假單位
        :param rule_name:
        '''
        self._params["minDay"] = minDay
        self.step(add_or_edit_holiday_dir,"Minimum_leave")
        return self

    def Annual_statistics(self,num):
        '''
        编辑年假統計方式
        :num :选择第N种统计方式，1.按假期周期；2.按合同期（总天数）
        3.按合同期（每年）；4.按合同期（每周）
        '''
        self._params["num"] = num
        self.step(add_or_edit_holiday_dir,"Annual_statistics")
        return self

    def increment_rule(self):
        '''
        编辑假期遞增規則,默认选择不递归
        '''
        self.step(add_or_edit_holiday_dir,"increment_rule")
        return self

    def cumulative_rule(self):
        '''
        编辑假期遞增規則,默认选择不纍計
        '''
        self.step(add_or_edit_holiday_dir,"cumulative_rule")
        return self

    def for_people(self,leave_type):
        '''
        编辑適用人群
        :param rule_name:
        '''
        if leave_type in self._driver.page_source:
            pass
        else:
            self._params["leave_type"] = leave_type
            self.step(add_or_edit_holiday_dir,"for_people")
        return self

    def click_save(self):
        self.step(add_or_edit_holiday_dir,"click_save")
        from page.leavepage.leave_settings.paid_Annual_Leave import Paid_Annual_Leave
        return Paid_Annual_Leave(self._driver)

