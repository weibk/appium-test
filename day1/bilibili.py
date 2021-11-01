#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/01 15:21
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

params = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "PBME00",
    "appPackage": "tv.danmaku.bili",
    "appActivity": ".MainActivityV2",
    "noReset": False
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", params)

el1 = driver.find_element_by_id("tv.danmaku.bili:id/agree")
el1.click()
el2 = driver.find_element_by_xpath("//android.widget.FrameLayout["
                                   "@content-desc=\"我的\"]/android.view"
                                   ".ViewGroup/android.widget.FrameLayout"
                                   "/android.widget.ImageView")
el2.click()
el3 = driver.find_element_by_id("tv.danmaku.bili:id/tv_login")
el3.click()
el4 = driver.find_element_by_id("tv.danmaku.bili:id/btn_change_account")
el4.click()
el5 = driver.find_element_by_id("tv.danmaku.bili:id/log_reg_checkbox")
el5.click()
el6 = driver.find_element_by_id("tv.danmaku.bili:id/tv_submit")
el6.click()
