#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
import time
from appium import webdriver
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '0c875323'
        desired_caps['appPackage'] = 'com.cloudy.linglingbang'
        desired_caps['appActivity'] = '.activity.welcome.WelcomeActivity'
        desired_caps["unicodeKeyboard"] = "True" #不会自动转码
        desired_caps["resetKeyboard"] = "True"  #输入完成后自动转为默认键盘
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def testadd(self):
        time.sleep(5)
        print(self.driver.contexts)
        print(self.driver.current_context)
        print(self.driver.current_activity)
        self.driver.find_element_by_id('owner_btn').click()
        print(self.driver.current_activity)
        time.sleep(2)
        self.driver.find_element_by_id('tv_login').click()
        print(self.driver.current_activity)
        # phone = self.driver.find_element_by_android_uiautomator("new UiSelector().resourceID('com.cloudy.linglingbang:id/login_et_phone')")
        phone = self.driver.find_element_by_xpath(r'//android.widget.RelativeLayout[@id="com.cloudy.linglingbang:id/login_et_phone"]/descendant::android.widget.EditText')
        phone.clear()
        phone.send_keys('15801006286')
        # mima = self.driver.find_element_by_android_uiautomator("new UiSelector().resourceID('com.cloudy.linglingbang:id/login_et_password')")
        mima = self.driver.find_element_by_xpath(r'//android.widget.RelativeLayout[@id="com.cloudy.linglingbang:id/login_et_password"]/descendant::android.widget.EditText')
        mima.clear()
        mima.send_keys('123456')
        time.sleep(2)
        # self.driver.find_element_by_xpath(r'//android.support.v4.view.ViewPager[3]/android.widget.LinearLayout[0]/android.widget.RelativeLayout[0]/android.widget.RelativeLayout[3]/android.widget.Button').click()
        self.driver.find_element_by_id(r'com.cloudy.linglingbang:id/btn_login').click()
        # self.driver.find_element_by_name('登录').click() 第一，appium1.5及之后的版本废弃了name属性(如name=账单，将不被支持用于定位)，name被废弃了，但是xpath的写法如//android.widget.TextView[@text="账单"]是被支持的
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

