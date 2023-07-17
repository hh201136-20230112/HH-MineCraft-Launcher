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
import pathlib,os,zipfile,mclist
n=sorted(pathlib.Path().rglob("*.*"))
l=[]
def openlibfiles(d):
    logs(f"当前解压{d}")
    zips = zipfile.ZipFile(d)
    zipss=zips.namelist()
    logs(f"文件内容：\n{zipss}")
    for i in zipss:
        for j in mclist.downmcs():
            lib="\\.minecraft\\versions\\"+str(j)
            filesname=str(j)+"-natives"
            logs("文件路径处理完成")
            print(os.listdir(str(os.getcwd())+lib))
            logs("目录文件读取完成")
            if filesname not in os.listdir(str(os.getcwd())+lib):
                os.mkdir(filesname)
                logs("目录已创建")
            logs(f"目录是否存在：{filesname in os.listdir(str(os.getcwd())+lib)}")
            if not filesname in os.listdir(str(os.getcwd())+lib):
                raise HHError("当前natives目录不存在！")
            lib=str(os.getcwd())+lib+"\\"+filesname
            logs(f"解压{d}中的{i}至{lib}")
            zips.extract(i,lib)
        logs(f"文件{i}解压完成")
    zips.close()
def ziplibraryfiles():
    for i in n:
        if ".minecraft\\libraries" in str(i):
            if ".jar" in str(i):
                j=str(os.getcwd())+"\\"+str(i)
                logs(j,2)
                if "-natives-windows" in str(i):
                    logs(f"库{str(i)}需要解压")
                    l.append(j)
                #print(str(i))
                #for j in os.listdir(i):
    logs("已读取依赖库"+str(len(l))+"项")
def downdate():
    return l