from time import sleep

from mark_po.config.base_page import BasePage
from mark_po.page.add_ds import AddDs


class DsManage(BasePage):

    def click_dataset_manage(self):
        """
        点击数据集管理
        :return:
        """
        self.steps("page/ds_manage.yaml", "into_dataset_manage")

    def click_add_ds(self):
        """
        点击新增数据集
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_add_ds")

    def goto_add_ds(self):
        """
        进入新增数据集页面
        :return:
        """
        return AddDs(self.driver)

    def click_update_ds(self):
        """
        点击修改数据集按钮
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_update_ds")

    def update_ds_explain(self, update_value):
        """
        修改数据集的说明
        :return:
        """
        self._params["ds_explain"] = str(update_value['update_value'])
        self.steps("page/ds_manage.yaml", "click")
        self.steps("page/ds_manage.yaml", "control_a")
        self.steps("page/ds_manage.yaml", "update_ds_explain")

    def click_cancel(self):
        """
        修改数据集取消
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_cancel")

    def click_submit(self):
        """
        修改数据集，点击确定
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_submit")

    def click_previous_page(self):
        """
        点击前一页
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_previous_page")

    def click_next_page(self):
        """
        点击下一页
        :return:
        """
        self.steps("page/ds_manage.yaml", "click_next_page")
