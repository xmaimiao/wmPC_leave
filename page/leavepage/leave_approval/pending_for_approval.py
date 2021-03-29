from common.contants import pending_for_approval_dir
from page.basepage import BasePage


class Pending_For_Approval(BasePage):
    def order_by_submission_time(self):
        '''
        選擇按“提交時間”倒序
        '''
        self.step(pending_for_approval_dir,"order_by_submission_time")
        return self

    def the_fir_approved(self):
        '''
        對第一行數據進行“批准”操作
        '''
        try:
            self.step(pending_for_approval_dir,"the_fir_approved")
            return True
        except Exception as e:
            return False


    def the_fir_not_approved(self):
        '''
        對第一行數據進行“不批准”操作
        '''
        try:
            self.step(pending_for_approval_dir, "the_fir_not_approved")
            return True
        except Exception as e:
            return False