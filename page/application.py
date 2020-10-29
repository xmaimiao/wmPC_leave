from common.contants import application_dir
from page.basepage import BasePage
from page.leavepage.leavepage import LeavePage


class Application(BasePage):

    def goto_leave(self, application):
        '''
        進入請假應用
        '''
        self._params["application"] = application
        self.step(application_dir, "goto_leave")
        return LeavePage(self._driver)


