from common.contants import paid_Annual_Leave_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.add_or_edit_holiday import Add_Or_Edit_Holiday


class Paid_Annual_Leave(BasePage):
    '''
    有薪年假主页面
    '''
    def add_holiday(self,):
        '''
        添加带薪年假
        '''
        self.step(paid_Annual_Leave_dir,"add_holiday")
        return Add_Or_Edit_Holiday(self._driver)

    def edit_holiday(self,rule_name):
        '''
        根据“规则名称”定位到要修改的年假，点击“编辑”
        '''
        self._params["rule_name"] = rule_name
        self.step(paid_Annual_Leave_dir,"edit_holiday")
        return Add_Or_Edit_Holiday(self._driver)

    def delect_holiday(self,rule_name):
        '''
        根据“规则名称”定位到要修改的年假，点击“删除”
        '''
        self._params["rule_name"] = rule_name
        self.step(paid_Annual_Leave_dir,"delect_holiday")
        return self

    def search_key(self,keywords):
        '''
        查询关键词并点击确认
        '''
        self._params["keywords"] = keywords
        self.step(paid_Annual_Leave_dir,"search_key")
        return self

    def get_current_data_total(self):
        '''
        获取当前页面数据量
        '''
        return self.step(paid_Annual_Leave_dir,"get_current_data_total")

    def get_the_first_rule_name(self):
        '''
        获取第一行数据的rulename，验证添加成功
        '''
        return self.step(paid_Annual_Leave_dir,"get_the_first_rule_name")

    def get_ele_of_add(self):
        '''
        获取”添加“元素，验证编辑成功，返回默认页面
        '''
        return self.step(paid_Annual_Leave_dir,"get_ele_of_add")