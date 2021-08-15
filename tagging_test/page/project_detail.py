from mark_po.config.base_page import BasePage
from mark_po.page.add_task import AddTask


class ProjectDetail(BasePage):

    def click_add_task(self):
        """
        点击创建任务
        :return:
        """
        self.steps("page/project_detail.yaml", "click_add_task")

    def goto_add_task_page(self):
        """
        进入创建任务页
        :return:
        """
        return AddTask(self.driver)

    def click_query(self, condition_val):
        """
        点击查看,进入标注页
        :return:
        """

        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/project_detail.yaml", "click_query")

    def click_previous_page(self):
        """
        点击前一页
        :return:
        """
        pass

    def click_next_page(self):
        """
        点击后一页
        :return:
        """
        pass
