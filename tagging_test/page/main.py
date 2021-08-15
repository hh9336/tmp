from mark_po.config.base_page import BasePage
from mark_po.page.ds_manage import DsManage
from mark_po.page.enterprise_manage import EnterpriseManage
from mark_po.page.login import Login
from mark_po.page.mark_page import MarkPage
from mark_po.page.project_manage import ProjectManage
from mark_po.page.start_mark import StartMark
from mark_po.page.task_manage import TaskManage
from mark_po.page.user_manage import UserManage


class Main(BasePage):

    def goto_login(self):
        """
        进入登录页
        :return:
        """
        return Login(self.driver)

    def goto_enterprise_manage(self):
        """
        进入企业管理页面
        :return:
        """
        return EnterpriseManage(self.driver)

    def goto_start_mark(self):
        """
        进入开始标注页
        :return:
        """
        return StartMark(self.driver)

    def goto_task_manage(self):
        """
        进入任务管理页
        :return:
        """
        return TaskManage(self.driver)

    def goto_ds_manage(self):
        """
        进入数据集管理页
        :return:
        """
        return DsManage(self.driver)

    def goto_project_manage(self):
        """
        进入项目管理页
        :return:
        """
        return ProjectManage(self.driver)

    def goto_user_manage(self):
        """
        进入用户管理页面
        :return:
        """
        return UserManage(self.driver)










