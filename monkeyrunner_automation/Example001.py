#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:实现在搜索框中输入查询词，并截图
eclipse中编写的python脚本是无法直接执行的，只能在命令行下执行，因为Android SDK并未提供windows环境下的解释器，如果在Linux环境下是可以直接在eclips中运行脚本的
"""
from com.android.monkeyrunner import MonkeyRunner,MokneyDevice,MonkeyImage

#连接设备
device = MonkeyRunner.waitForConnection(3,'0c875323') #3秒为超时时间，第二个参数为设备的名称【通过adb devices查看】
#启动APP
device.startActivity('com.cloudy.linglingbang/com.cloudy.linglingbang/com.cloudy.linglingbang.activity.HomeActivity')
MonkeyRunner.sleep(2)#等待2秒
#进入搜索框
device.touch(500,250,'DOWN_ADN_UP')
MonkeyRunner.sleep(1)
#输入查询词
device.type('310')
MonkeyRunner.sleep(1)
#点击回车键
device.press('KEYCODE_ENTER','DOWN_AND_UP')#操作enter以及操作发送keycode的类型
MonkeyRunner.sleep(1)
#点击搜索按钮
device.touch(1000,250,'DOWN_ADN_UP')
MonkeyRunner.sleep(6)
#截屏
image = device.takeSnapshot()
image.writetoFile('./test.png','png')#存入路径和格式