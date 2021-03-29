from common.contants import leave_overview_dir
from page.basepage import BasePage


class Leave_OverView(BasePage):
    '''休假概覽'''
    def get_the_fir_status(self):
        return self.step(leave_overview_dir,"get_the_fir_status")