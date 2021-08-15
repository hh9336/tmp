#!/usr/bin/env python
# --coding:utf-8--
# @File: market.py
# @Author:ann
# @Time: 2021/8/2 9:48 PM
from selenium.webdriver.common.by import By
from xueqiu_app_hgwz.page.base_page import BasePage
from xueqiu_app_hgwz.page.search import Search


class Market(BasePage):

    def goto_search(self):
        """
        点击搜索，进入搜索页
        """
        self.steps('../page/market.yaml', "goto_search")
        # self.find(By.ID, 'com.xueqiu.android:id/action_search').click()
        return Search(self.driver)
