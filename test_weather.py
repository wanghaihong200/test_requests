#!/usr/bin/env python
# encoding: utf-8
"""
@author: wang
@contact: 296701193@qq.com
@file: test_weather
@time: 2021/5/4 8:32 下午
@desc:
"""
import json

import allure
import requests
from jsonpath import jsonpath


class TestWeather:
    def setup(self):
        self.query_city = 'http://jisuweather.api.bdymkt.com/weather/city'
        self.query_weather = 'http://jisuweather.api.bdymkt.com/weather/query'
        self.headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Bce-Signature': 'AppCode/c95a88594e4b46518e8c6559aaddebfa'
        }

    def teardown(self):
        pass

    @allure.story("城市查询接口调用")
    def test_city(self):
        r = requests.request("GET", self.query_city, headers=self.headers)
        print(r.json())
        assert "上海" in jsonpath(r.json(), "$.result..city")

    def test_city_weather(self):
        params = {
            "cityid": 24,
            "citycode": "101020100",
            "city": "上海"
        }
        params = json.dumps(params)
        r = requests.request("POST", self.query_weather, headers=self.headers, json=params)
        print(r.json())

    def test_jenkins_buildWithParameters(self):
        """
        调用jenkins进行参数构建
        :return:
        """
        params = {
            "using_headless": True
        }
        url = "http://localhost:8080/job/jenkins_selenium/buildWithParameters"
        r = requests.request("POST", url=url, data=params, auth=("admin", "119dae9a29417768a93079338623f1d91f"))
        print(r.status_code)

    def test_jenkins_build(self):
        """
        调用jenkins进行构建
        :return:
        """
        url = "http://localhost:8080/job/test_request/build"
        r = requests.request("POST", url=url, auth=("admin", "119dae9a29417768a93079338623f1d91f"))
        print(r.status_code)

    def test_jenkins_build_lastNum(self):
        """
        调用jenkins进行查询buildNumber，及对应构建的状态
        :return:
        """
        url = "http://localhost:8080/job/test_request/lastBuild/buildNumber"
        r = requests.request("GET", url=url, auth=("admin", "119dae9a29417768a93079338623f1d91f"))
        print("最后一次构建的任务编号:" + r.text + "\n")

        url2 = f"http://localhost:8080/job/test_request/{r.text}/api/json"
        print(url2)
        r2 = requests.request("GET", url=url2, auth=("admin", "119dae9a29417768a93079338623f1d91f"))
        print("最后一次构建的状态: "+json.dumps(r2.json(), indent=2))
