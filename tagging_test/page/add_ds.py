from selenium.webdriver.common.by import By

from mark_po.config.base_page import BasePage


class AddDs(BasePage):

    def select_date_type_video(self):
        """
        选择数据类型
        :return:
        """
        self.steps("page/add_ds.yaml", "select_date_type_video")

    def input_dateset_name(self, input_dateset_name):
        """
        输入数据集名称
        :return:
        """
        self._params["input_name"] = input_dateset_name['input_name']
        self.steps("page/add_ds.yaml", "input_dateset_name")

    def select_enterprise_dataset(self):
        """
        选择公开性（企业数据集）
        :return:
        """
        self.steps("page/add_ds.yaml", "select_enterprise_dataset")

    def select_private_dataset(self):
        """
        选择公开性（私有数据集）
        :return:
        """
        pass

    def input_text(self, input_text):
        """
        输入数据集描述
        :return:
        """
        self._params["input_text"] = input_text['input_text']
        self.steps("page/add_ds.yaml", "input_text")

    def select_local_upload(self):
        """
        选择上传方式（本地上传）
        :return:
        """
        self.steps("page/add_ds.yaml", "select_local_upload")

    def select_service_upload(self):
        """
        选择上传方式（服务端上传）
        :return:
        """
        self.steps("page/add_ds.yaml", "select_service_upload")

    def drag_file(self, img_path):
        """
        点击上传或拖拽文件
        :return:
        """
        self._params["img_path"] = str(img_path['img_path'])
        self.steps("page/add_ds.yaml", "drag_file")

    def input_path_address(self, input_path):
        """
        选择服务器上的绝对路径地址
        :return:
        """
        self._params["input_path"] = input_path['input_path']
        self.steps("page/add_ds.yaml", "input_path_address")

    def click_reset(self):
        """
        点击重置
        :return:
        """
        self.steps("page/add_ds.yaml", "click_reset")

    def click_submit(self, img_name):
        """
        点击保存
        :return:
        """
        self.wait_for_click((By.XPATH, "//*[@class='ant-btn ant-btn-primary']"))
        self.steps("page/add_ds.yaml", "click_submit")
        self.driver.save_screenshot(f'result/{img_name}.png')

    def click_return(self):
        """
        返回到数据集管理页面
        :return:
        """
        self.steps("page/add_ds.yaml", "click_return")



