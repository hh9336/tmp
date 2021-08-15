from mark_po.config.base_page import BasePage
from mark_po.page.mark_page import MarkPage


class TaskManage(BasePage):

    def task_export(self):
        """
        任务查看
        :return:
        """
        self.steps("page/task_manage.yaml", "task_export")

    def task_del(self):
        """
        点击删除按钮
        :return:
        """
        self.steps("page/task_manage.yaml", "task_del")

    def task_del_cancel(self):
        """
        取消删除
        :return:
        """
        self.steps("page/task_manage.yaml", "task_del_cancel")

    def task_del_submit(self):
        """
        确定删除
        :return:
        """
        self.steps("page/task_manage.yaml", "task_del_submit")

    def click_task_id(self):
        """
        点击任务ID，查看子任务
        :return:
        """
        self.steps("page/task_manage.yaml", "click_task_id")

    def click_query(self):
        """
        点击查看，进入标注页
        :return:
        """
        self.steps("page/task_manage.yaml", "click_query")
        return MarkPage(self.driver)
