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

#from hhSQL import *
from hh的小工具 import *
import os
logs("用户数据读取程序启动！", 1)
yhsj={"UUID": "0000000000003004998F501A96E01684", "name": "hwlMC"}
a=False
if "a.txt" not in os.listdir(os.getcwd()) and "b.txt" not in os.listdir(os.getcwd()):
    a=True
#openHHSQL()
    #fileopen(["date","a"])
    #filein(yhsj["UUID"])
    #filein(yhsj["name"])
    files1=open("a.txt","a")
    files1.close()
    files1=open("a.txt","r")
    if files1.readline()=="":
        files1.close()
        files1=open("a.txt","a")
        files1.write(yhsj["UUID"])
        files2=open("b.txt","a")
        files2.write(yhsj["name"])
        files2.close()
        files1.close()
    files1=open("a.txt","r")
    files2=open("b.txt","r")
    print(files1.readline(),files2.readline())
    yhsj["UUID"]=files1.readline()
    yhsj["name"]=files2.readline()

##    #b=filelook()
#    #print(b[0][0])
#   yhsj["UUID"]=b[0][0]
#    yhsj["name"]=b[1][0]

def downyhsj():
    logs("获取用户数据", 1)
    print(yhsj)

    return yhsj
def filling(uuid,name):
    files1=open("a.txt","w")
    files1.write(uuid)
    files2=open("b.txt","w")
    files2.write(name)
    files2.close()
    files1.close()