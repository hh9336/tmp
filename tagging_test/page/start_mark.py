from mark_po.config.base_page import BasePage
from mark_po.page.mark_page import MarkPage


class StartMark(BasePage):

    def click_mark(self):
        """
        点击开始标注
        :return:
        """
        self.steps("page/start_mark.yaml", "click_mark")

    def goto_mark(self):
        """
        进入开始标注页
        :return:
        """
        return MarkPage(self.driver)
