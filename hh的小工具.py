hh = """

      -----    -----    -----    -----
     /    /   /    /   /    /   /    /
    /    /   /    /   /    /   /    /
   /    /___/    /   /    /___/    /
  /    ___      /   /     ___     /
 /    /  /     /   /     /  /    /
/    /  /     /   /     /  /    /
-----    -----    -----   -----
hh的小工具 v1.0.1
作者：hh/hh201136@126.com
整合了hh制作的各种小工具
程序需要python标准库

"""

import random
import time

def uijm(a):
    """
    帮助文档：
    该函数参数：（模式）
    该函数返回值：
    加密模式：(加密后文本 解密码)
    解密模式：(解密后文本)
    用于解密和解密文本
    """
    import turtle
    nePym = turtle.Pen()
    nePym.clear()
    # 明文符号集
    print("正在加载明文符号集")
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
    print(alphabet)
    # 密文符号集
    print("正在加载密文符号集")
    h = random.randint(10, 35)
    cipher = alphabet[h:] + alphabet[:h]
    print(cipher)
    # a=input("加密:y\n解密:a\n退出:n\n:")
    if a == "y":
        nePym.clear()
        text = turtle.textinput("加密数据", "输入查找字符:")
        pit = ""
        print("正在查找字符")
        for i in text:
            if i in alphabet:
                ind = alphabet.index(i)
                pit += cipher[ind]
            else:
                pit += i
        print(pit)
        nePym.penup()
        nePym.goto(-5, 25)
        nePym.pendown()
        nePym.write("加密后数据:", font=("Arial", 10))
        nePym.penup()
        nePym.goto(0, 0)
        nePym.pendown()
        nePym.write(pit, font=("Arial", 20))
        nePym.penup()
        nePym.goto(-5, -25)
        nePym.pendown()
        # 这里是解密值生成，修改可能无法正常解密
        m = random.randint(1, 2)
        h = m * h
        print(str(h) + str(m))
        nePym.write("解密值：", font=("Arial", 10))
        nePym.penup()
        nePym.goto(-5, -50)
        nePym.pendown()
        nePym.write(str(h) + str(m), font=("Arial", 20))
        return pit + " " + str(h) + str(m)
    elif a == "a":
        nePym.clear()
        pit = turtle.textinput("解密数据", "输入解密字符:")
        d = turtle.textinput("解密数据", "输入解密值:")
        print("正在查找字符")
        jmm = d[2]
        d = d[0:2]
        d = int(d) / int(jmm)
        d = int(d)
        cipher_1 = alphabet[d:] + alphabet[:d]
        print(cipher_1)
        text = ""
        for i in pit:
            if i in cipher_1:
                ind = cipher_1.index(i)
                text += alphabet[ind]
            else:
                text += i
        print(text)
        nePym.clear()
        nePym.penup()
        nePym.goto(-5, 25)
        nePym.pendown()
        nePym.write("解密后数据:", font=("Arial", 10))
        nePym.penup()
        nePym.goto(0, 0)
        nePym.pendown()
        nePym.write(text, font=("Arial", 20))
        # nePym.penup()
        # nePym.goto(-5,-25)
        # nePym.pendown()
        return text
    else:
        nePym.clear()
        print("运行结束")


def nuijm(a, b, c=""):
    """
    帮助文档：
    该函数参数：（模式，加密/解密文本，仅解密模式：解密码）
    该函数返回值：
    加密模式：(加密后文本 解密码)
    解密模式：(解密后文本)
    用于解密和解密文本
    """
    # 明文符号集
    # print("正在加载明文符号集")
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
    # print(alphabet)
    # 密文符号集
    # print("正在加载密文符号集")
    h = random.randint(10, 35)
    cipher = alphabet[h:] + alphabet[:h]
    # print(cipher)
    # a=input("加密:y\n解密:a\n退出:n\n:")
    if a == "y":
        text = b
        pit = ""
        # print("正在查找字符")
        for i in text:
            if i in alphabet:
                ind = alphabet.index(i)
                pit += cipher[ind]
            else:
                pit += i
        # print(pit)
        # nePym.penup()
        """
        nePym.goto(-5,25)
        nePym.pendown()
        nePym.write("加密后数据:",font=("Arial",10))
        nePym.penup()
        nePym.goto(0,0)
        nePym.pendown()
        nePym.write(pit,font=("Arial",20))
        nePym.penup()
        nePym.goto(-5,-25)
        nePym.pendown()
        """
        # 这里是解密值生成，修改可能无法正常解密
        m = random.randint(1, 2)
        h = m * h
        # print(str(h)+str(m))
        """
        nePym.write("解密值：",font=("Arial",10))
        nePym.penup()
        nePym.goto(-5,-50)
        nePym.pendown()
        nePym.write(str(h)+str(m),font=("Arial",20))
        """
        return pit + " " + str(h) + str(m)
    elif a == "a":
        pit = b
        d = c
        # print("正在查找字符")
        jmm = d[2]
        d = d[0:2]
        d = int(d) / int(jmm)
        d = int(d)
        cipher_1 = alphabet[d:] + alphabet[:d]
        # print(cipher_1)
        text = ""
        for i in pit:
            if i in cipher_1:
                ind = cipher_1.index(i)
                text += alphabet[ind]
            else:
                text += i
        # print(text)
        """
        nePym.clear()
        nePym.penup()
        nePym.goto(-5,25)
        nePym.pendown()
        nePym.write("解密后数据:",font=("Arial",10))
        nePym.penup()
        nePym.goto(0,0)
        nePym.pendown()
        nePym.write(text,font=("Arial",20))
        #nePym.penup()
        #nePym.goto(-5,-25)
        #nePym.pendown()
        """
        return text


def tnum(num="help", size=5, colors="blue"):
    """
    帮助文档：
    该函数参数：(要绘制的数字，大小，颜色)
    该函数没有返回值
    用于绘制数字
    """
    import turtle
    p = turtle.Pen()
    if num == "help":
        # p.pensize(size)
        # p.pencolor(colors)
        print("包作者：（QQ）hh\nemail：hh201136@126.com")
    if num == "c":
        p.clear()
    if num == 0:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 4)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 4)
    if num == 1:
        p.pensize(size)
        p.pencolor(colors)
        p.right(90)
        p.forward(size * 4)
    if num == 2:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
    if num == 3:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        # p.right(-90)
        p.forward(-size * 2)
        p.left(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
    if num == 4:
        p.pensize(size)
        p.pencolor(colors)
        p.right(90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        # p.right(-90)
        p.forward(-size * 4)
        # p.right(-90)
        # p.forward(size*2)
    if num == 5:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(-size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
    if num == 6:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(-size * 2)
        p.right(90)
        p.forward(size * 4)
        p.right(-90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
    if num == 7:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 4)
        # p.right(-90)
        # p.forward(size*2)
        # p.right(-90)
        # p.forward(size*2)
        # p.right(-90)
        # p.forward(size*2)
    if num == 8:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 4)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 4)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(90)
        p.forward(size * 2)
    if num == 9:
        p.pensize(size)
        p.pencolor(colors)
        p.forward(-size * 2)
        p.right(90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        p.right(-90)
        p.forward(size * 2)
        # p.right(-90)
        p.forward(-size * 4)


def hh_help():
    print(hh)


def xyx():
    """
    帮助文档：
    该函数没有参数
    该函数没有返回值
    是一个小游戏
    """
    score = 0
    e = []
    print("进入秘境，沿着主路探索")
    print("------------------------")
    # 遇到野怪
    print("遇到野怪")
    h = input("是否消灭野怪?\ny=是,n=否")
    if h == "y" or h == "是":
        for i in range(5):
            print("消灭野怪，获得10个积分")
            score = score + 10
        print("你获得了解密器碎片*5！")
        if "解密器碎片*1" in e:
            a = e.index("解密器碎片*1")
            e[a] = "解密器碎片*6"
        else:
            e.append("解密器碎片*5")
    print("------------------------")
    print("你看见地上有一把钥匙\n你捡起了钥匙")
    print("你获得了一把钥匙！")
    e.append("钥匙*1#0201")
    print("------------------------")
    # 遇到宝藏
    print("遇到一扇门")
    # jmstr=jmxyx.jm("y","h o p y t n")
    print("好像门上了锁")
    if "钥匙*1#0201" in e:
        m = input("是否使用钥匙开锁（是/否）")
        if m == "是" or m == "y":
            print("得到宝藏,获得10个积分")
            print("箱子里好像还有什么?")
            print("你获得了解密器碎片*1！")
            if "解密器碎片*5" in e:
                e[e.index("解密器碎片*5")] = "解密器碎片*6"
            else:
                e.append("解密器碎片*1")
            print("你获得了碎片合成器*1！")
            e.append("碎片合成器*1")
        score = score + 10
    print("------------------------")
    # 遇到宝藏
    print("遇到宝藏")
    jmstr = nuijm("y", "python")
    print("单词密码为: ", jmstr[:11], "数字为：", jmstr[11:])
    print("这段密码好像加密了")
    h = input("是否使用解密器（是/否）")
    if h == "是" or h == "y":
        if "解密器" in e:
            mm = nuijm("a", input("输入加密字符："), input("输入数字："))
            print("解密中")
            print("解密后密码：", mm)
        elif "解密器" not in e and "解密器碎片*6" in e and "碎片合成器*1" in e:
            h = input("是否使用碎片合成器合成解密器（是/否）")
            if h == "是" or h == "y":
                e.remove("解密器碎片*6")
                e.append("解密器")
                h = input("是否使用解密器（是/否）")
                if h == "是" or h == "y":
                    if "解密器" in e:
                        mm = nuijm("a", input("输入加密字符："), input("输入数字："))
                        print("解密中")
                        print("解密后密码：", mm)
        else:
            print("我需要一个“解密器”")
    m = input("输入正确的密码")
    if m == "python":
        print("得到宝藏,获得10个积分")
        score = score + 10
    print("------------------------")
    # 遇到英雄或敌人
    print("遇到英雄或敌人")
    way = input("选择道路(A或B)")
    if way == "A" or way == "a":
        print("遇到英雄,获得10个积分")
        score = score + 10
        print("------------------------")
        print("你的积分是")
        print(score)
        if int(score) >= 50:
            print("闯关成功")
        else:
            print("闯关失败")
        print('到达秘境出口，离开秘境')
    elif way == "B" or way == "b":
        print("遇到敌人,损失10个积分")
        score = score - 10
        print("------------------------")
        print("你的积分是")
        print(score)
        if int(score) >= 50:
            print("闯关成功")
        else:
            print("闯关失败")
        print('到达秘境出口，离开秘境')
    else:
        print("你找到了隐藏的路")
        print("达成成就：卡出BUG了")
        print('到达秘境出口，离开秘境')
        print("闯关成功")


def myip():
    """
    帮助文档：
    该函数没有参数
    该函数返回值：(本机在局域网内的主机名,本机在局域网内的IP地址)
    用于查询本机内网IP和主机名
    """
    import socket
    wifiname = socket.gethostname()
    wifiip = socket.gethostbyname(wifiname)
    return wifiname, wifiip

from time import *
import os
if "logs" not in os.listdir(os.getcwd()):
    os.mkdir("logs")
file_neme = "logs\\log" + strftime("%Y%m%d%H%M%S") + ".txt"


def logs(log, lx=0):
    """
    帮助文档：
    该函数参数：（日志内容，日志等级）
    该函数没有返回值
    用于快速记录日志

    if lx == 0:
        dj = "[MAIN]"
    elif lx == 1:
        dj = "[logs]"
    elif lx == 2:
        dj = "[debug]"
    elif lx == 3:
        dj = "[!!!ERROR!!!]"
    elif lx == 4:
        dj = "[I/O]"
    elif lx == 5:
        dj = "[Start]"
    elif lx == 6:
        dj = "[Minecraft]"
    elif lx == 7:
        dj = "[Launch]"
    else:
        dj = "【未分类】"
    """
    if lx == 0:
        dj = "[MAIN]"
    elif lx == 1:
        dj = "[logs]"
    elif lx == 2:
        dj = "[debug]"
    elif lx == 3:
        dj = "[!!!ERROR!!!]"
    elif lx == 4:
        dj = "[I/O]"
    elif lx == 5:
        dj = "[Start]"
    elif lx == 6:
        dj = "[Minecraft]"
    elif lx == 7:
        dj = "[Launch]"
    else:
        dj = "【未分类】"
    file = open(file_neme, "a")
    print("[" + strftime("%Y/%m/%d,%H:%M:%S") + "]" + dj + " " + str(log))
    file.write("[" + strftime("%Y/%m/%d,%H:%M:%S") + "]" + dj + " " + str(log) + "\n")
    file.close()


def jdt(ts, dq, db=100):
    """
    帮助文档：
    该函数参数：（提示消息，当前进度，全部项）
    该函数返回值：
    进度条
    用于制作进度条
    """
    t = ""
    t += ts
    t += " "
    for i in range(dq):
        t += "#"
    for i in range(db - dq):
        t += "="
    t += f"(当前第{dq}项/共{db}项)"
    return t

class HMLauncher():
    """
    帮助文档：
    用于制作MC启动器（未完成）
    """
    def launcher(self,java="C:\\Program Files\\Java\\jre1.8.0_333\\bin\\java.exe",uuid="0000000000003004998F501A96E01684",name="HMLmc",version="1.19.3"):
        jvm="-Xmx "+str(1028)+"-Djava.library.path="+"连接库"

#class HM
if __name__ == "__main__":
    #hh_help()
    print("当前文件为主文件")
else:
    hh_help()
    #print(__name__)

def mppx(lists):
    """
    帮助文档：
    该函数参数：（待排序列表）
    该函数返回值：
    从大到小排序后的列表
    冒泡排序列表
    """
    a=lists
    n=len(a)
    for i in range(1,n):
        for j in range(n-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
