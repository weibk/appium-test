#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# time:2021/11/01 20:36

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "10"
caps["appium:deviceName"] = "oppor17"
caps["appium:appPackage"] = "com.sina.weibo"
caps["appium:appActivity"] = ".VisitorMainTabActivity"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                   "/android.widget.LinearLayout/android"
                                   ".widget.FrameLayout/android.widget"
                                   ".TabHost/android.widget.LinearLayout"
                                   "/android.widget.FrameLayout[5]")
el1.click()
el2 = driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
el2.click()
el3 = driver.find_element_by_id("com.sina.weibo:id/iv_qq")
el3.click()
el4 = driver.find_element_by_accessibility_id("QQ授权登录")
el4.click()
el5 = driver.find_element_by_accessibility_id("发现")
el5.click()
el6 = driver.find_element_by_id("com.sina.weibo:id/btn_close")
el6.click()
el8 = driver.find_element_by_id("com.sina.weibo:id/ly_left")
el8.click()
el9 = driver.find_element_by_id("com.sina.weibo:id/tv_search_keyword")
el9.send_keys("胡歌")
el9.send_keys("胡歌\\n")

driver.quit()