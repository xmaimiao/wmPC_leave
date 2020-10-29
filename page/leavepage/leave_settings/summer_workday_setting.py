from common.contants import summer_workday_setting_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.edit_summer_setting import Edit_Summer_Setting


class Summer_Workday_Setting(BasePage):
    '''
    暑期设置主页面
    '''
    def edit_summer_setting(self,summer_name):
        '''
        编辑暑期设置，根据传进来的规则名称定位编辑的数据
        :return:
        '''
        self._params["summer_name"] = summer_name
        self.step(summer_workday_setting_dir,"summer_workday_setting")
        return Edit_Summer_Setting(self._driver)

    def get_ele_of_add(self):
        '''
        获取”添加“元素，验证编辑成功，返回默认页面
        '''
        return self.step(summer_workday_setting_dir, "get_ele_of_add")