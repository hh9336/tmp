#!/usr/bin/env python
# --coding:utf-8--
# @File: handle_black.py.py
# @Author:ann
# @Time: 2021/8/7 4:55 PM
import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    # 黑名单列表
    def wrapper(*args, **kwargs):
        # 因为装饰器的机制问题，self会作为第一个参数传递过来，所以通过args[0]获取即可
        # 避免出现循环导入的异常，需要在此处进行导入
        # self 就是一个实例的意思，当将self传递过来后，就可以用通过self调取主函数的方法
        from xueqiu_app_hgwz.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            # 添加日志
            logging.info("run " + func.__name__ + "\n arg: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            element = func(*args, **kwargs)
            _err_num = 0
            return element
        except Exception as e:
            # 当触发黑名单时，进行截图
            instance.screenshot('../result/tmp.png')
            # rb读取图片
            # rb读取图片
            with open('../result/tmp.png', "rb") as f:
                pic = f.read()
            # 将图片添加到allure报告中
            allure.attach(pic, attachment_type=allure.attachment_type.PNG)
            logging.error('element not found , handle black list')
            # 如果没找到，就进行黑名单处理
            if instance._err_num > instance._max_err_num:
                # 如果err0次数大于指定值，清空error次数，并报异常
                instance._err_num = 0
                raise e
            instance._err_num += 1
            for ele in instance._black_list:
                # 对黑名单进行点击, 使用finds是防止页面中有多个相同的黑名单点击元素，一般不会存在，所以点击时，取eles[0]即可
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return wrapper
