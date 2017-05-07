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
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def testadd(self):
        time.sleep(5)
        print(self.driver.contexts)
        print(self.driver.current_context)

    def tearDown(self):
        self.driver.quit()

