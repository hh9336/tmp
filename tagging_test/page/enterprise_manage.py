from mark_po.config.base_page import BasePage


class EnterpriseManage(BasePage):

    def click_add_enterprise(self):
        """
        点击新增企业
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_add_enterprise')

    def add_enterprise(self, add_enterprise):
        """
        新增企业
        :return:
        """
        self._params['enterprise_name'] = add_enterprise['enterprise_name']
        self._params['enterprise_account'] = add_enterprise['username']
        self._params['enterprise_pwd'] = add_enterprise['password']
        self._params['confirm_pwd'] = add_enterprise['confirm_pwd']
        self.steps("page/enterprise_manage.yaml", 'add_enterprise')

    def assert_add_enterprise(self, assert_v):
        """
        通过企业全称断言是否新增成功
        :param assert_v:
        :return:
        """
        self._params['assert_v'] = assert_v['enterprise_name']
        return self.steps("page/enterprise_manage.yaml", 'assert_add_enterprise')

    def update_enterprise_name(self, update_enterprise_name):
        """
        点击修改按钮，为企业名重新命名
        :return:
        """
        self._params['re_enterprise_name'] = update_enterprise_name['name']
        self.steps("page/enterprise_manage.yaml", 'update_enterprise_name')

    def assert_upload_enterprise(self, assert_v):
        """
        通过修改的企业全称断言是否修改成功
        :param assert_v:
        :return:
        """
        self._params['assert_v'] = assert_v['name']
        return self.steps("page/enterprise_manage.yaml", 'assert_add_enterprise')

    def click_cancel(self):
        """
        点击取消
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_cancel')

    def click_submit(self):
        """
        点击确定
        :return:
        """
        self.driver.save_screenshot('result/add_enterprise.png')
        self.steps("page/enterprise_manage.yaml", 'click_submit')

    def click_cancel_upload(self):
        """
        点击取消修改按钮
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_submit_upload')

    def click_submit_upload(self):
        """
        点击确认修改按钮
        :return:
        """
        self.driver.save_screenshot('result/upload_enterprise.png')
        self.steps("page/enterprise_manage.yaml", 'click_submit_upload')

    def click_stop_or_start(self):
        """
        停用企业
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_stop_or_start')

    def click_cancel_stop_or_start(self):
        """
        点击取消停用或启动
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_cancel_stop_or_start')

    def click_submit_stop_or_stat(self):
        """
        点击确定停用或启动
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'click_submit_stop_or_stat')

    def quit_login(self):
        """
        退出登录
        :return:
        """
        self.steps("page/enterprise_manage.yaml", 'quit_login')
