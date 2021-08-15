#!/usr/bin/env python
# --coding:utf-8--
# @File: search.py
# @Author:ann
# @Time: 2021/8/2 9:46 PM
from selenium.webdriver.common.by import By

from xueqiu_app_hgwz.page.base_page import BasePage


class Search(BasePage):

    def search(self, search_value):
        """
        搜索功能：
            1.在输入搜索阿里巴巴
            2.点击阿里巴巴-SW
            3.点击阿里巴巴-SW后面的加自选
        """
        self._params['search_value'] = search_value
        self.steps('../page/search.yaml', "search")

        # self.find(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/listview"]/..//*[@text="阿里巴巴"]').click()
        # self.find(By.XPATH, '//*[@text="09988"]/../../..//*[@text="加自选"]').click()

    def is_choose(self):
        """
        断言：
            当可以发现"已添加"文本时，证明断言成功
        """
        result = self.steps('../page/search.yaml', "is_choose")
        # element = self.finds(By.XPATH, '//*[@text="09988"]/../../..//*[@text="已添加"]')
        return result
