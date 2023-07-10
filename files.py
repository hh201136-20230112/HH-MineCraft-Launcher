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
import pathlib,os
n=sorted(pathlib.Path().rglob("*.*"))
l=[]
for i in n:
    if ".minecraft\\libraries" in str(i):
        if ".jar" in str(i):
            j=str(os.getcwd())+"\\"+str(i)
            logs(j,2)
            #print(str(i))
            #for j in os.listdir(i):
            l.append(j)
logs("已读取"+str(len(l))+"项")
def downdate():
    return l