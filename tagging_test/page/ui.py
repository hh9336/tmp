#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from mark_po.config.base_page import BasePage
from mark_po.page.main import Main


class UI(BasePage):
    _driver = None
    _base_url = ""

    def start(self, driver: WebDriver = None):
        """
        启动UI
        :param driver:
        :return:
        """
        if driver is None:
            chrome_options = Options()
            # 和浏览器打开的调试端口进行通信
            # 浏览器要使用 --remote-debugging-port=9222 开启调试
            chrome_options.debugger_address = "127.0.0.1:9222"
            # self._driver = webdriver.Chrome(options=chrome_options)
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
        return self

    def goto_index(self):
        """
        进入首页
        :return:
        """
        return Main(self._driver)
