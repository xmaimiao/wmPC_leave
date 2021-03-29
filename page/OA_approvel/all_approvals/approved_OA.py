from common.contants import approved_OA_dir
from page.basepage import BasePage


class Approved_OA(BasePage):
    def get_the_fir_status(self):
        '''
        返回第一條數據的狀態
        '''
        return self.step(approved_OA_dir,"get_the_fir_status")