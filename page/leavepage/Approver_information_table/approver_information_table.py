from common.contants import approver_information_table_dir
from page.basepage import BasePage


class Approver_Information_Table(BasePage):
    def keywords_search(self,keywords):
        '''
        關鍵詞查詢
        '''
        self._params["keywords"] = keywords
        self.step(approver_information_table_dir,"keywords_search")
        return self

    def click_search_button(self):
        '''
        點擊查詢按鈕
        '''
        self.step(approver_information_table_dir,"click_search_button")
        return self

    def edit_the_first_approver(self):
        '''
        點擊“編輯”按鈕，編輯第一個人員信息
        '''
        self.step(approver_information_table_dir,"edit_the_first_approver")
        from page.leavepage.Approver_information_table.approver_information_details import Approver_Information_Details
        return Approver_Information_Details(self._driver)

    def get_the_first_superior(self):
        '''
        获取第一个人员的上级，验证清空人员有效
        '''
        return self.step(approver_information_table_dir,"get_the_first_superior")

    def get_the_first_supervisor(self):
        '''
        获取第一个人员的主管，验证清空人员有效
        '''
        return self.step(approver_information_table_dir,"get_the_first_supervisor")

    def get_the_first_day_ofentry(self):
        '''
        获取第一个人员的入职日期，用于验证更改入职日期有效
        '''
        return self.step(approver_information_table_dir,"get_the_first_day_ofentry")
