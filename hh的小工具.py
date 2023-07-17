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


class HHError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        logs("程序错误:" + str(self.value),True)
        return repr(self.value)

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
logsopen=True
def logsinit(tf):
    global logsopen
    logsopen=tf

def logs(log, lx=0,tf=False):
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
        dj = "[HH Code]"
    elif lx == 7:
        dj = "[Launch]"
    elif lx == 8:
        dj = "[HH Code RUNNING]"
    else:
        dj = ""
    """
    if logsopen or tf:
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
            dj = "[HH Code]"
        elif lx == 7:
            dj = "[Launch]"
        elif lx == 8:
            dj = "[HH Code RUNNING]"
        else:
            dj = ""
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


class HH_Code():
    """
    帮助文档：
    该类参数：（要加载的HHCODE文件，当前程序名）
    用于加载HH Code代码
    HH Code代码
    HH201136@126.com基于python开发的编程语言
    可以用于创建配置文件
    执行简单的PYTHON脚本
    在代码文件前应添加以下文本：
    #HH Code#
    #HH Code - (代码版本，应为：（主版本名.副版本名）)
    #HH Code - (代码名称，可以随便写)
    #HH Code - (代码应在什么程序中运行，就是类的“当前程序名”参数)
    #HH Code - (代码作者)
    """
    def __init__(self,openfile,mainclass,DEBUG=False):
        logsinit(DEBUG)
        logs("开始处理代码",6,True)
        self.bllist= {}
        self.forlin=0
        self.file=open(str(openfile))
        self.files=self.file.read()
        logs(self.files,6)
        self.files=self.files.split("\n")
        self.file.close()
        logs(self.files,6)
        self.head=self.files[:5]
        self.body=self.files[5:]
        logs(self.head,6)
        #self.head[0].replace("#HH Code#")
        for i in range(1,5):
            self.head[i]=self.head[i].replace("#HH Code - ","")
        self.hhcodev=float(self.head[1])
        self.hhcodename=self.head[2]
        self.hhcoderunning=self.head[3]
        self.hhcodeopen=self.head[4]
        self.nowhhcodev=0.1
        logs(f"""
        代码head信息
        {self.head[0]}
        使用的HH_CODE执行程序版本：{float(self.head[1])}
        程序自定义名称：{self.head[2]}
        应在{self.head[3]}上运行
        作者：{self.head[4]}
        """,6,True)
        if self.hhcodev>self.nowhhcodev:
            raise HHError("加载的代码使用的HHCODE版本过高！")
        if self.hhcoderunning != mainclass and self.hhcoderunning != "all" :
            raise  HHError(f"代码应被{self.hhcoderunning}加载")
        logs("代码处理完成",6)
    def __onecode__(self,codes,run):
        codes=str(codes).split(" ")
        #print(codes,len(codes))
        """特殊代码行处理"""
        if codes[0]=="结束":
            logs("代码结束",6)
            return "结束"
        if codes[0]=="来到":
            """跳转处理位置代码行"""
            #print(1)
            #print(codes[-1])
            if len(codes)<3:
                logs(f"跳转至第{int(codes[1])}行代码",6)
                return int(codes[1])
            else:
                if self.forlin>=int(codes[2]):
                    self.forlin=0
                    if len(self.body)-1 != run:
                        return run+1
                    else:
                        return "结束"
                logs(f"跳转至第{int(codes[1])}行代码\n当前循环次数：{self.forlin}",6)
                self.forlin+=1
                return int(codes[1])
        else:
            """=====普通代码行处理"""
            if codes[0]=="变量":
                """=====“变量设置”代码行类型判断"""
                if codes[2]=="int":
                    self.bllist[str(codes[1])]=int(codes[3])
                elif codes[2]=="str":
                    self.bllist[str(codes[1])]=str(codes[3])
                elif codes[2]=="float":
                    self.bllist[str(codes[1])]=float(codes[3])
            elif codes[0]=="输出":
                """文本输出  114514！ （"""
                logs(self.bllist[str(codes[1])],114514,True)
            elif codes[0]=="日志":
                """日志输出  判断是否定义类型"""
                if len(codes) > 2:
                    logs(self.bllist[str(codes[1])],int(codes[2]),True)
                else:
                    logs(self.bllist[str(codes[1])],8,True)
            elif codes[0]=="等待":
                """等待"""
                sleep(float(codes[1]))
            """=====下一个代码行判断"""
            if len(self.body)-1 != run:
                return run+1
            else:
                return "结束"
    def runing(self):
        logs("代码开始运行……",6,True)
        #for i in self.body:
        i=0
        logs(len(self.body),6)
        while True:
            i=self.__onecode__(self.body[i],i)
            #print(i)
            if i=="结束":
                logs("代码运行完成", 6, True)
                return 0

    def bldown(self):
        logs("获取代码中的变量",6,True)
        return self.bllist
#a=HH_Code("C:\\Users\\Administrator\\Desktop\\mc启动器\\code.txt","HHMCL")
#a.runing()
#print(a.bldown())
