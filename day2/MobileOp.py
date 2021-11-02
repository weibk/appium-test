#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/02 16:45


class MobileOP(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, account, password):
        el1 = self.driver.find_element_by_id(
            "com.android.permissioncontroller:id/permission_allow_button1")
        el1.click()
        el2 = self.driver.find_element_by_accessibility_id("我")
        el2.click()
        el3 = self.driver.find_element_by_id(
            "com.sina.weibo:id/et_login_view_phone")
        el3.send_keys(account)
        el4 = self.driver.find_element_by_id(
            "com.sina.weibo:id/tv_login_view_resent")
        el4.click()
        el5 = self.driver.find_element_by_id(
            "com.sina.weibo:id/et_login_view_sms")
        el5.send_keys(password)
        el7 = self.driver.find_element_by_id(
            "com.sina.weibo:id/iv_login_view_protocol")
        el7.click()
        el8 = self.driver.find_element_by_id(
            "com.sina.weibo:id/btn_login_view_sms")
        el8.click()

    def login_success(self):
        return "登录成功"

    def login_failed(self):
        return "账号或密码错误"
