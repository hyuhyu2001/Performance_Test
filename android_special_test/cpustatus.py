#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:对APP的CPU进行持续监测
"""
import xlsxwriter
import os
import time

class Controller(object):
    '''控制类'''
    def __init__(self,count):
        self.counter = count
        self.alldata = [('timestamp','cpustatus')]

    #单次测试过程
    def testprocess(self):
        result = os.popen('adb shell "dumpsys cpuinfo | grep com.cloudy.linglingbang"').readlines()
        result = ''.join(result)
        cupvalue = result.strip('\n ').split('%')[0]

        currentTime = self.getCurrentTime()
        self.alldata.append((currentTime,cupvalue))

    #多次执行过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(5)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToXLSX(self):
        workbook = xlsxwriter.Workbook('cpustatus.xlsx')
        worksheet = workbook.add_worksheet('CPU')
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
