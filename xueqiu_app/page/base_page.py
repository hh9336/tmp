#!/usr/bin/env python
# --coding:utf-8--
# @File: base_page.py
# @Author:ann
# @Time: 2021/8/2 9:37 PM
import json

import yaml
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

from xueqiu_app_hgwz.page.handle_black import handle_black


class BasePage:
    # 黑名单列表
    _black_list = [
        (By.ID, 'com.xueqiu.android:id/iv_close')
    ]
    _max_err_num = 3
    _err_num = 0

    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, by, locator=None):
        # 如果元素找到，就清空error计数
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        if locator is None:
            result = self.driver.find_elements(*by)
        else:
            result = self.driver.find_elements(by, locator)
        return result

    def set_implicitly_wait(self, second):
        """
        定义隐式等待
        """
        self.driver.implicitly_wait(second)

    def screenshot(self, path):
        self.driver.save_screenshot(path)

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)
        steps = json.loads(raw)
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 'send' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len>0' == action:
                    eles = self.finds(step['by'], step['locator'])
                    return len(eles) > 0
