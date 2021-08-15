#!/usr/bin/env python
# --coding:utf-8--
# @File: app.py
# @Author:ann
# @Time: 2021/8/2 9:37 PM
from appium import webdriver
from AppiumCwechat_hgwz.page.basepage import BasePage
from xueqiu_app_hgwz.page.main import Main


class App(BasePage):
    def start(self):
        """
        启动app
        """
        if self.driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "noReset": True,  # 不清理上一次的操作数据
                # 设置完成后支持中文
                "unicodeKeyBoard": True,
                "resetKeyBoard": True,
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(20)
        else:
            self.driver.launch_app()
        return self

    def goto_main(self):
        """
        进入首页
        """
        return Main(self.driver)
