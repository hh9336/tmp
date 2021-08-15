#!/usr/bin/env python
# --coding:utf-8--
# @File: main.py
# @Author:ann
# @Time: 2021/8/2 9:42 PM
from selenium.webdriver.common.by import By
from xueqiu_app_hgwz.page.attention import Attention
from xueqiu_app_hgwz.page.base_page import BasePage
from xueqiu_app_hgwz.page.market import Market


class Main(BasePage):

    def goto_market(self):
        """
        进入自选页
        """
        self.steps('../page/main.yaml', "goto_market")
        # self.find(By.XPATH, '//*[@text="自选"]').click()
        return Market(self.driver)

    def goto_attention(self):
        """
        进入关注页
        """
        self.steps('../page/main.yaml', "goto_attention")
        # self.find(By.XPATH, '//*[@text="关注"]').click()
        # 将隐式等待从10s修改为3秒，优化黑名单取消的速度
        self.set_implicitly_wait(3)
        return Attention(self.driver)
