#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:对APP使用的流量进行监测统计
"""

import xlsxwriter
import os
import time
import string

class Controller(object):
    '''控制类'''
    def __init__(self,count):
        self.counter = count
        self.alldata = [('timestamp','traffic')]

    #单次测试过程
    def testprocess(self):
        #获取进程的PID
        result = os.popen('adb shell "ps|grep com.cloudy.linglingbang"')
        PID = result.readlines()[0].split()[1]

        #获取进程ID使用的流量
        result =os.popen( 'adb shell "cat /proc/%s/net/dev"'%PID).readlines()
        result = ''.join(result)
        print(result)
        traffic = result.strip('\n ').split('%')[0]
            #将所有空格换为#
            # # if 'eth0' in line:
            # line = '#'.join(line.split())
            # print(line)
            # 按#号拆分,获取收到和发出的流量
            # receive = line.split("#")[1]
            # transmit = line.split("#")[9]
            # elif "eth1" in line:
            #     # 将所有空行换成#
            #     line = "#".join(line.split())
            #     # 按#号拆分,获取收到和发出的流量
            #     receive2 = line.split("#")[1]
            #     transmit2 = line.split("#")[9]
        # print(receive2)
        # print(transmit2)
        # 计算所有流量的之和
        # alltraffic = string.atoi(receive) + string.atoi(transmit) + string.atoi(receive2) + string.atoi(transmit2)
        # 按kb计算流量值
        # alltraffic = alltraffic / 1024

        # currentTime = self.getCurrentTime()
        # self.alldata.append((currentTime,alltraffic))
        # print(self.alldata)

    #多次执行过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)

    #获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    #数据的存储
    def SaveDataToXLSX(self):
        workbook = xlsxwriter.Workbook('traffic.xlsx')
        worksheet = workbook.add_worksheet('流量')
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
    controller = Controller(1)
    controller.testprocess()
    # controller.run()
    # controller.SaveDataToXLSX()
