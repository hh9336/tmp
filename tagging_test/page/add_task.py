from mark_po.config.base_page import BasePage
from mark_po.page.mark_style import MarkStyle


class AddTask(BasePage):

    def input_task_name(self, input_task_name):
        """
        输入任务名称
        :return:
        """
        self._params['task_name'] = input_task_name['task_name']
        self.steps("page/add_task.yaml", "input_task_name")

    def select_pri(self):
        """
        选择优先级
        :return:
        """
        self.steps("page/add_task.yaml", "select_pri")

    def select_dateset_pic(self, condition_val):
        """
        选择数据集 - 图片集
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self.steps("page/add_task.yaml", "select_dateset_pic")

    def select_dateset_video(self):
        """
        选择数据集 - 视频集
        :return:
        """
        self.steps("page/add_task.yaml", "select_dateset_video")

    def select_assign_way(self):
        """
        选择分配方式
        :return:
        """
        pass

    def select_marker(self):
        """
        选择标注员
        :return:
        """
        self.steps("page/add_task.yaml", "select_marker")

    def select_mark_style(self, condition_val):
        """
        选择标注样式
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/add_task.yaml", "select_mark_style")

    def click_add_temple(self, condition_val):
        """
        选择标注样式
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.steps("page/add_task.yaml", "click_add_temple")

    def goto_mark_style_page(self):
        """
        进入标注样式页
        :return:
        """
        return MarkStyle(self.driver)

    def input_task_explain(self, input_task_explain):
        """
        输入任务说明
        :return:
        """
        self._params['task_explain'] = input_task_explain['task_explain']
        self.steps("page/add_task.yaml", "input_task_explain")

    def click_add_task(self, condition_val, img_name):
        """
        点击创建任务
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)
        self.driver.save_screenshot(f'result/{img_name}.png')
        self.steps("page/add_task.yaml", "click_add_task")

    def return_task_detail(self):
        """
        返回任务详情页
        :return:
        """
        self.steps("page/add_task.yaml", "return_task_detail")
