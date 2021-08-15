from mark_po.config.base_page import BasePage


class AddProject(BasePage):
    def input_project_name(self, input_project_name, condition_val):
        """
        输入项目名
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0

        self.wait_for_condition(test_wait)

        self._params["project_name"] = input_project_name['project_name']
        self.steps("page/add_project.yaml", "input_project_name")

    def input_detail(self, input_detail):
        """
        输入备注
        :return:
        """
        self._params["project_detail"] = input_detail['project_detail']
        self.steps("page/add_project.yaml", "input_detail")

    def click_cancel(self):
        """
        点击取消
        :return:
        """
        self.steps("page/add_project.yaml", "click_cancel")

    def click_submit(self):
        """
        点击确定
        :return:
        """
        self.steps("page/add_project.yaml", "click_submit")
