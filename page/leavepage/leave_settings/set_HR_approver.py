import json
from common.contants import set_HR_approver_dir
from page.basepage import BasePage
from page.leavepage.leave_settings.edit_HR import Edit_HR


class Set_HR_Approver(BasePage):
    '''
    HR审批人员设置主页面
    '''
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def goto_edit_HR(self,rules_name):
        '''
        點擊編輯HR，根據規則名稱打開對應編輯頁面
        '''
        self._params["rules_name"] = rules_name
        self.step(set_HR_approver_dir,"goto_edit_HR")
        return Edit_HR(self._driver)

    def get_all_HR(self):
        '''
        獲取所有HR人員
        '''
        try:
            HR_list = []
            for i in range(1,5):
                HR = {}
                self._params["i"] = i
                HR["規則名稱"] = self.step(set_HR_approver_dir,"get_rule_name")
                HR["審核人員"]= self.step(set_HR_approver_dir,"get_check")
                HR["審批人員"] = self.step(set_HR_approver_dir,"get_approver")
                HR_list.append(HR)
            print(json.dumps(HR_list, indent=4, ensure_ascii=False))
            return True
        except Exception as e:
            return False

