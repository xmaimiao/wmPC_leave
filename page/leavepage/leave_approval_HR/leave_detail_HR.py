from common.contants import leave_detail_HR_dir
from page.basepage import BasePage


class Leave_Detail_HR(BasePage):
    def wait_sleep(self,sleeps):
        self.sleep(sleeps)
        return self

    def reminder_of_supplement(self):
        '''
        点击“资料补充提醒”按钮,获取成功toast返回
        关闭详情页
        '''
        toast_tatus = self.step(leave_detail_HR_dir,"reminder_of_supplement")
        self.sleep(3)
        self.step(leave_detail_HR_dir, "close_page")
        return toast_tatus


