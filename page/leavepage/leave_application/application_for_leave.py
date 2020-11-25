import re

import win32con
import win32gui

from common.contants import application_for_leave_dir
from page.basepage import BasePage


class Application_For_Leaver(BasePage):

    def get_days_available(self):
        '''
        獲取可用天數
        '''
        result = self.step(application_for_leave_dir,"get_days_available")
        return int(re.search("(\d+).*?(\d+).*",result).group(1))


    def send_mobile_no(self,mobile_no):
        '''
        填写电话号码
        '''
        self._params["mobile_no"] = mobile_no
        self.step(application_for_leave_dir,"send_mobile_no")
        return self

    def choice_Sick_Leave(self):
        '''
        选择病假
        '''
        self.step(application_for_leave_dir,"choice_Sick_Leave")
        return self

    def choice_over_a_day(self):
        '''
        选择超过一天模式
        '''
        self.step(application_for_leave_dir,"choice_over_a_day")
        return self


    def choice_startdate(self,startdate):
        '''
        默认仅一天模式，输入开始日期
        '''
        self._params["startdate"] = startdate
        self.step(application_for_leave_dir, "choice_startdate")
        return self

    def chocie_startdate_type(self,leave_starttype):
        '''
        选择开始日期的类型为：全天/上午/下午/晚上
        leave_starttype: 傳入開始日期的类型
        '''
        self._params["leave_starttype"] = leave_starttype
        self.step(application_for_leave_dir, "chocie_startdate_type")

        return self

    def choice_enddate(self,enddate):
        '''
        输入結束日期
        '''
        self._params["enddate"] = enddate
        self.step(application_for_leave_dir, "choice_enddate")
        return self

    def chocie_enddate_type(self,leave_endtype):
        '''
        选择开始日期的类型为：全天/上午/下午/晚上
        leave_endtype: 傳入結束日期的类型
        '''
        self._params["leave_endtype"] = leave_endtype
        self.step(application_for_leave_dir, "chocie_enddate_type")
        return self


    def remarks(self,remarks):
        '''
        输入备注
        params: 傳入備注
        '''
        self._params["remarks"] = remarks
        self.step(application_for_leave_dir,"remarks")
        return self

    def upload_attachment(self,excel_path):
        '''
        上传附件,install  pywin32
        '''
        self._params["excel_path"] = excel_path
        self.step(application_for_leave_dir,"upload_attachment")
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", "打开")
        # 向下传递
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 二级

        # 输入文件的绝对路径，点击“打开”按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, excel_path)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        return self

    def cleck_save(self):
        '''
        保存表單，並返回“休假明細”text，驗證保存成功
        :return:
        '''
        return self.step(application_for_leave_dir,"cleck_save")