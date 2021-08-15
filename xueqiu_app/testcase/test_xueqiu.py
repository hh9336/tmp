#!/usr/bin/env python
# --coding:utf-8--
# @File: test_xueqiu.py
# @Author:ann
# @Time: 2021/8/2 9:38 PM
import pytest
import yaml
from xueqiu_app_hgwz.page.app import App

with open('test_xueqiu.yaml', encoding="utf-8") as f:
    result = yaml.safe_load(f)['stock_name']


class TestCase:
    def setup(self):
        self.app = App()

    @pytest.mark.parametrize('stock_name', result)
    def test_market(self, stock_name):
        # 伪造黑名单
        basic = self.app.start().goto_main()
        basic.goto_attention().click_black()

        search = basic.goto_market().goto_search()
        search.search(stock_name)
        assert search.is_choose()
