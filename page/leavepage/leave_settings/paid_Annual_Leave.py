import json

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

    def search_holiday(self,rule_name):
        '''
        1.查询规则名称，并点击“查询”按钮
        '''
        self._params["rule_name"] = rule_name
        self.step(paid_Annual_Leave_dir,"search_holiday")
        return self

    def edit_holiday(self,rule_name):
        '''
        根据“规则名称”定位到要修改的年假，点击“编辑”
        '''
        self._params["rule_name"] = rule_name
        # 查询规则名称，返回元素合集
        eles = self.step(paid_Annual_Leave_dir, "search_holiday")
        if len(eles) == 1:
            self._params["i"] = 1
            self.step(paid_Annual_Leave_dir,"edit_holiday")
        elif len(eles)>1:
        #     判断每一个规则名称，若和要编辑相同，则点击“编辑”按钮
            for i in range(1,len(eles)+1):
                self._params["i"] = i
                # 获取规则名称
                rule_n = self.step(paid_Annual_Leave_dir,"get_rule_name")
                if rule_n == rule_name:
                    self.step(paid_Annual_Leave_dir, "edit_holiday")
                    break
        else:
            print("暂无数据！")
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

    def get_AL_rules(self):
        '''
        获取前5条年假规则：年假起点、最高天数、假期递增规则、转结规则、适用人群
        '''
        try:
            AL_rules=[]
            get_current_data_total = self.step(paid_Annual_Leave_dir, "get_current_data_total")
            if int(get_current_data_total) >6:
                num = 6
            else:
                num = int(get_current_data_total)
            for i in range(1,num+1):
                self._params["i"] = i
                AL_rule = {}
                AL_rule["rule_name"] = self.step(paid_Annual_Leave_dir, "rule_name")
                AL_rule["start_point"] = self.step(paid_Annual_Leave_dir,"start_point")
                AL_rule["Maximum_days"] = self.step(paid_Annual_Leave_dir,"Maximum_days")
                AL_rule["increment_rule"] = self.step(paid_Annual_Leave_dir,"increment_rule")
                AL_rule["cumulative_rule"] = self.step(paid_Annual_Leave_dir,"cumulative_rule")
                AL_rule["for_people"] = self.step(paid_Annual_Leave_dir,"for_people")
                AL_rules.append(AL_rule)
            print(json.dumps(AL_rules,indent=4,ensure_ascii=False))
            return True
        except Exception as e:
            return False



