#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/02 17:04

from appium import webdriver
from ddt import ddt, data
from DataLogin import DataLogin
from MobileOp import MobileOp
from unittest import TestCase


caps = {"platformName": "Android", "appium:platformVersion": "10",
        "appium:deviceName": "oppor17", "appium:appPackage": "com.sina.weibo",
        "appium:appActivity": ".VisitorMainTabActivity", "appium:noReset": True,
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 0,
        "appium:connectHardwareKeyboard": True}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


@ddt
class TestLogins(TestCase):
    @data(*DataLogin.data_success)
    def test_logins(self, **data1):
        mo = MobileOp(driver)
        mo.login(data1['account'], data1['password'])
        result = mo.login_failed()
        self.assertEqual(data1['except'], result)