#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/02 17:15

from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test*.py")
runner = HTMLTestRunner.HTMLTestRunner(
    title="微博测试",
    description="微博登录测试报告",
    verbosity=1,
    stream=open('test.html', mode='w+', encoding='utf-8')
)
runner.run(tests)
