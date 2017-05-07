#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:性能专项-获取APP冷启动时间和热启动时间的脚本
后续再实现时间戳差值的脚本：App Class包含方法：LaunchApp，StopApp，CalculateTime,TimeBeforeLaunch,TimeAfterLaunch
"""
import xlsxwriter
import os
import time

class App(object):
    '''启动类'''
    def __init__(self):
        self.content = ''
        self.startTime = 0

    #启动APP
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.cloudy.linglingbang/.activity.welcome.WelcomeActivity'
        self.content = os.popen(cmd)

    # 停止APP
    def StopApp(self):
        cmd = 'adb shell am force-stop com.cloudy.linglingbang' #冷启动停止
        # cmd = 'adb shell input keyevent 3 #热启动停止
        os.popen(cmd)

    #获取启动时间
    def GetLaunchTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.startTime = line.split(':')[1]
                break
        return self.startTime


class Controller(object):
    '''控制类'''
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.alldata = [('timestamp','elapsedtime')]

    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(10)
        elapsedtime = self.app.GetLaunchTime()
        self.app.StopApp()
        time.sleep(3)
        currentTime = self.getCurrentTime()
        self.alldata.append((currentTime,elapsedtime))

    #多次执行过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToXLSX(self):
        workbook = xlsxwriter.Workbook('startTime.xlsx')
        worksheet = workbook.add_worksheet('启动时间')
        worksheet.set_column('A:B',20)
        row = 0
        col = 0
        for x, y in (self.alldata):
            worksheet.write(row, col, x)
            worksheet.write(row, col + 1, y)
            row += 1
        # worksheet.write(row, 0, 'AVERAGE')
        # BN = ''.join(['B', '%d' % (int(row))])
        # worksheet.write(row, 1, '=AVERAGE(B2:%s)'%BN)

        workbook.close()

if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.SaveDataToXLSX()

