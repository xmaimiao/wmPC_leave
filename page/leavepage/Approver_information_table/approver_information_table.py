from page.basepage import BasePage
import json
import shelve
from common.contants import approver_information_table_dir



class Approver_Information_Table(BasePage):

    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

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

    def get_the_fir_superior_and_supervisor(self):
        '''
        獲取第一行人員的上級、主管
        '''
        try:
            db = shelve.open("leave_approver")
            superior = self.step(approver_information_table_dir,"get_the_first_superior")
            supervisor = self.step(approver_information_table_dir, "get_the_first_supervisor")
            db["leave_approver"] = superior + "、" + supervisor
            db.close()
            print(f"上級和主管分別為：{superior}、{supervisor}")
            return True
        except Exception as e:
            return False

    def get_the_fir_information(self,user_list):
        '''
        1.传进来人员的数据
        2.查询该人员账号，定位每一个人员
        3.獲取第一行人員的上級、主管、休假類型、上一年度帶假、年假結余天數、入職日期、離職日期
        '''
        try:
            information = []
            for keywords in user_list:
                self._params["keywords"] = keywords
                user_info = {}
                self.step(approver_information_table_dir, "keywords_search")
                self.step(approver_information_table_dir, "click_search_button")
                self.wait_sleep(1)
                user_info["user"] = keywords
                user_info["superior"] = self.step(approver_information_table_dir, "get_the_first_superior")
                user_info["supervisor"] = self.step(approver_information_table_dir, "get_the_first_supervisor")
                user_info["leave_type"] = self.step(approver_information_table_dir, "get_the_first_leave_type")
                user_info["Leaves_of_previous"] = self.step(approver_information_table_dir, "get_Leaves_of_previous")
                user_info["Balance_days_of_AL"] = self.step(approver_information_table_dir, "get_Balance_days_of_AL")
                user_info["Date_of_entry"] = self.step(approver_information_table_dir, "get_the_first_day_ofentry")
                user_info["Date_of_resignation"] = self.step(approver_information_table_dir, "get_Date_of_resignation")
                information.append(user_info)
            print(json.dumps(information,indent=4,ensure_ascii=False))
            return True
        except Exception as e:
            return False




