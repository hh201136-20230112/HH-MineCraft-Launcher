"""

      -----    -----    -----    -----
     /    /   /    /   /    /   /    /
    /    /   /    /   /    /   /    /
   /    /___/    /   /    /___/    /
  /    ___      /   /     ___     /
 /    /  /     /   /     /  /    /
/    /  /     /   /     /  /    /
-----    -----    -----   -----
作者：hh
邮箱：hh201136@126.com
"""
from hh的小工具 import *
import psutil
memory_now=0
def lookmemory():
    global memory_now
    memory_info = psutil.virtual_memory()
    memory_total = int(memory_info.total / 1024 / 1024)
    memory_per = memory_info.percent
    logs("内存信息,内存总量,当前内存占用率 "+str(memory_info)+","+str(memory_total)+","+str(memory_per))
    memory_now=int(memory_total-(memory_total*(memory_per/100)))
    logs("内存总量,当前可用内存 "+str((memory_total/1000))+","+str(memory_now))
lookmemory()
def downmemory():
    lookmemory()
    return memory_now
def downmemorytike():
    memory_info = psutil.virtual_memory()
    memory_total = int(memory_info.total / 1024 / 1024)
    memory_per = memory_info.percent
    memory_now=int(memory_total-(memory_total*(memory_per/100)))
    return memory_now