from common.contants import pending_for_approval_HR_dir
from page.basepage import BasePage
from page.leavepage.leave_approval_HR.leave_detail_HR import Leave_Detail_HR


class Pending_For_Approval_HR(BasePage):

    def order_by_submission_time(self):
        '''
        選擇按“提交時間”倒序
        '''
        self.step(pending_for_approval_HR_dir,"order_by_submission_time")
        return self

    def the_fir_approved_HR(self):
        '''
        對第一行數據進行“批准”操作
        '''
        try:
            self.step(pending_for_approval_HR_dir,"the_fir_approved_HR")
            return True
        except Exception as e:
            return False


    def the_fir_not_approved_HR(self):
        '''
        對第一行數據進行“不批准”操作
        '''
        try:
            self.step(pending_for_approval_HR_dir, "the_fir_not_approved_HR")
            return True
        except Exception as e:
            return False

    def view_the_fir_HR(self):
        '''
        對第一行數據進行“查看”操作
        '''
        self.step(pending_for_approval_HR_dir, "view_the_fir_HR")
        return Leave_Detail_HR(self._driver)

    def approve_all_items(self,Sn_list):
        '''
        批量批准，根據傳進來的單號數據
        '''
        try:
            for Sn in Sn_list:
                self._params["Sn"] = Sn
                # 根據單號勾選申請單
                self.step(pending_for_approval_HR_dir, "select_application_number")
            # 點擊“批量批准 按鈕
            self.step(pending_for_approval_HR_dir, "click_approve_all_items")
            return True
        except Exception as e:
            return False