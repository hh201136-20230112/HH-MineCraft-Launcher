from hh的小工具 import *
logs("Minecraft版本检测模块启动！",1)
import os
mc=[]
try:
    logs("错误跟踪开始！",2)
    mc=os.listdir(".minecraft//versions")
except:
    logs("程序读取时出现错误！",3)
logs("MC列表："+str(mc),1)
def downmcs():
    logs("获取mc列表",4)
    return mc

