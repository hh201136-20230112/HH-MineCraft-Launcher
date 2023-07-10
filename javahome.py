from hh的小工具 import *
logs("JAVAHOME检测文件启动！",1)
import winreg,os
java=""
try:
    logs("错误跟踪开始！",2)
    opwi=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\JavaSoft\Java Runtime Environment")
    logs("成功打开JAVA注册表",1)
    powi=winreg.QueryValueEx(opwi,"CurrentVersion")
    logs("JAVA路径读取中",1)
    opwi=winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\JavaSoft\Java Runtime Environment\\"+powi[0])
    logs("拼接注册表路径",1)
    powi=winreg.QueryValueEx(opwi,"JavaHome")
    logs("JAVA路径读取成功",1)
    logs("JAVA路径："+powi[0],1)
    java=powi[0]
except:
    logs("程序读取时出现错误！",3)
logs("处理java路径信息",1)
java=java[:-13]
logs("处理后路径："+java,1)
logs("获取所有JAVA……",1)
try:
    logs("错误跟踪开始！",2)
    javas=os.listdir(java)
    logs("JAVA列表："+str(javas),1)
except:
    logs("程序读取时出现错误！",3)
def downjavas():
    logs("获取java列表",4)
    return java,javas
