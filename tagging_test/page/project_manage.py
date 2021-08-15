from mark_po.config.base_page import BasePage
from mark_po.page.add_project import AddProject
from mark_po.page.project_detail import ProjectDetail


class ProjectManage(BasePage):

    def click_project_manage(self):
        """
        点击项目管理，进入项目管理页面
        :return:
        """
        self.steps("page/project_manage.yaml", "into_project_manage")

    def click_add_project(self):
        """
        点击新增项目
        :return:
        """
        self.steps("page/project_manage.yaml", "click_add_project")

    def goto_add_project_page(self):
        """
        进入新增项目页
        :return:
        """
        return AddProject(self.driver)

    def click_detail(self):
        """
        点击详情
        :return:
        """
        self.steps("page/project_manage.yaml", "click_detail")

    def goto_project_detail(self):
        """
        进入项目详情页
        :return:
        """
        return ProjectDetail(self.driver)

    def update_project_name(self, project_name):
        """
        点击修改
        :return:
        """
        self._params['re_project_name'] = project_name['re_project_name']
        self.steps("page/project_manage.yaml", "update_project_name")

    def click_previous_page(self):
        """
        点击前一页
        :return:
        """
        pass

    def click_next_page(self):
        """
        点击下一页
        :return:
        """
        pass
