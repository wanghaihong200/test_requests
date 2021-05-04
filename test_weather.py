#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_weather
@time: 2021/5/4 8:32 下午
@desc:
"""
import requests
from jsonpath import jsonpath


class TestWeather:
    def setup(self):
        self.url = 'http://jisuweather.api.bdymkt.com/weather/city'
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Bce-Signature': 'AppCode/c95a88594e4b46518e8c6559aaddebfa'
        }

    def teardown(self):
        pass

    def test_weather(self):
        r = requests.request("GET", self.url, headers=self.headers)
        print(r.json())
        assert "上海" in jsonpath(r.json(), "$.result..city")
