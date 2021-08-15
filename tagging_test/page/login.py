from mark_po.config.base_page import BasePage


class Login(BasePage):

    def login(self, user_pwd, pic_name):
        self._params['username'] = user_pwd['username']
        self._params['password'] = user_pwd['password']
        self.steps("page/login.yaml", "login")
        self.driver.save_screenshot(f'result/{pic_name}.png')

    def is_right(self, user_pwd):
        """
        通过是否存在企业管理断言是否登录成功
        :return:
        """
        self._params['assert_v1'] = user_pwd['assert_v1']
        return self.steps("page/login.yaml", "assert_right")

    def assert_value(self, assert_v):
        """
        断言企业管理员是否登录成功
        :param assert_v:
        :return:
        """
        self._params['assert_v'] = assert_v
        return self.steps("page/enterprise_manage.yaml", 'assert_add_enterprise')

    def init_yaml_date(self, yaml_file_path):
        """
        修改YAML文件中已经使用过的数据
        :return:
        """
        self.update_init_date(yaml_file_path)
