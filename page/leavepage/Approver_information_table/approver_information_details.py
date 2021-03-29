import re

from common.contants import approver_information_details_dir
from page.basepage import BasePage
from page.leavepage.Approver_information_table.approver_information_table import Approver_Information_Table
from page.select_staff import Select_Staff


class Approver_Information_Details(BasePage):

    def edit_vacation_type(self,vacation_type):
        '''
        修改休假類型
        '''
        try:
            self._params["vacation_type"] = vacation_type
            results = self.step(approver_information_details_dir,"edit_vacation_type")
            for result in results:
                print(f"result:{result}")
                result_text = re.search('(.*)(\(.*\))',result.text).group(1)
                print(f"result_text:{result_text}")
                if result_text == vacation_type:
                    result.click()
                    break
            return self
        except Exception as e:
            print("編輯的休假類型不存在！")
            raise e

    def edit_superior(self):
        '''
        修改上级
        '''
        self.step(approver_information_details_dir,"edit_superior")
        return Select_Staff(self._driver)


    def edit_supervisor(self):
        '''
        修改主管
        '''
        self.step(approver_information_details_dir,"edit_supervisor")
        return Select_Staff(self._driver)

    def edit_representative_for_leave(self):
        '''
        修改代請假人
        '''
        self.step(approver_information_details_dir,"edit_representative_for_leave")
        return Select_Staff(self._driver)

    def edit_person_type(self,person_type):
        '''
        編輯人員類型
        '''
        self._params["person_type"] = person_type
        self.step(approver_information_details_dir,"edit_person_type")
        return self

    def edit_date_of_entry(self,entrydate):
        '''
        編輯入職日期
        :param entrydate: 入職日期
        '''
        self._params["entrydate"] = entrydate
        self.step(approver_information_details_dir,"edit_date_of_entry")
        return self

    def edit_date_of_resignation(self,resignationdate):
        '''
        編輯離職日期
        :param resignationdate: 離職日期
        '''
        self._params["resignationdate"] = resignationdate
        self.step(approver_information_details_dir,"edit_date_of_resignation")
        return self


    def edit_contract_start_date(self,contract_start_date):
        '''
        編輯合同開始日期
        :param contract_start_date: 合同開始日期
        '''
        self._params["contract_start_date"] = contract_start_date
        self.step(approver_information_details_dir,"edit_contract_start_date")
        return self

    def edit_contract_end_date(self,contract_end_date):
        '''
        編輯合同結束日期
        :param contract_end_date: 合同結束日期
        '''
        self._params["contract_end_date"] = contract_end_date
        self.step(approver_information_details_dir,"edit_contract_end_date")
        return self

    def click_save(self):
        '''
        點擊保存表單
        '''
        self.step(approver_information_details_dir,"click_save")
        return Approver_Information_Table(self._driver)