from selenium.webdriver.common.by import By

from mark_po.config.base_page import BasePage
from mark_po.page.mark_page import MarkPage


class UserManage(BasePage):

    def click_user_manage(self):
        """
        点击用户管理，进入用户管理页面
        :return:
        """
        self.steps("page/user_manage.yaml", "into_user_manage")

    def add_user(self, add_user):
        """
        新增用户
        :return:
        """
        self._params['username'] = add_user['username']
        self._params['pwd'] = add_user['password']
        self._params['confirm_pwd'] = add_user['re_password']
        self.steps("page/user_manage.yaml", "add_user")

    def set_whether_manager(self):
        """
        设置是否为管理员
        :return:
        """
        self.steps("page/user_manage.yaml", "set_whether_manager")

    def assert_whether_manage(self, assert_v):
        self._params['assert_v'] = assert_v
        return self.steps("page/user_manage.yaml", 'assert_whether_manage')

    def click_cancel(self):
        """
        点击取消
        :return:
        """
        self.steps("page/user_manage.yaml", "click_cancel")

    def click_submit(self):
        """
        点击确定
        :return:
        """
        self.steps("page/user_manage.yaml", "click_submit")

    def click_update_button(self, condition_val):
        """
        点击更新按钮
        :return:
        """
        def test_wait(x):
            self._params['condition_val'] = condition_val
            element_len = self.steps("page/mark_page.yaml", "click_play_condition")
            if element_len == 'False':
                a = self.steps("page/mark_page.yaml", "click_play_condition")
            return element_len > 0
        self.wait_for_condition(test_wait)

        self.steps("page/user_manage.yaml", "click_update_button")

    def update_whether_manager(self):
        """
        修改是否为管理员
        :return:
        """
        self.wait_for_click((By.ID, 'coordinated_role'))
        self.steps("page/user_manage.yaml", "update_whether_manager")

    def click_cancel_upload(self):
        """
        取消修改
        :return:
        """
        self.steps("page/user_manage.yaml", "click_cancel_upload")

    def click_submit_upload(self):
        """
        确定修改
        :return:
        """
        self.steps("page/user_manage.yaml", "click_submit_upload")
        self.driver.save_screenshot('result/user_manage.png')

    def click_remove(self):
        """
        点击移除
        :return:
        """
        self.steps("page/user_manage.yaml", "click_remove")

    def click_cancel_remove_user(self):
        """
        点击取消移除用户
        :return:
        """
        self.steps("page/user_manage.yaml", "click_cancel_remove_user")

    def click_submit_remove_user(self):
        """
        点击确定移除用户
        :return:
        """
        self.steps("page/user_manage.yaml", "click_submit_remove_user")





