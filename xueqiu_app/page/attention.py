#!/usr/bin/env python
# --coding:utf-8--
# @File: attention.py
# @Author:ann
# @Time: 2021/8/3 9:17 PM
from selenium.webdriver.common.by import By
from xueqiu_app_hgwz.page.base_page import BasePage


class Attention(BasePage):

    def click_black(self):
        self.steps('../page/attention.yaml', "click_black")
        # 伪造黑名单，点击后，会触发一个弹窗页
        # self.find(By.ID, 'com.xueqiu.android:id/iv_create').click()
