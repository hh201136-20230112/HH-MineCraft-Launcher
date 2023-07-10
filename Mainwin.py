# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

"""
这是一个用PYTHON编写的简易Minecraft启动器
作者：hh201136@126.com
出现问题发送至邮箱"hh201136@126.com"（尽量在1周内回复）
版本：0.0.1(内测)
"""
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from hh的小工具 import *

import files
import hhyhdq
import javahome
import mclist
import memory
import mcjson

# t1 = time.time()
logs("窗口文件已启动", 0)


class HHMCLError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == "程序退出":
            logs("程序退出")
            return 0
        else:
            logs("启动器错误:" + str(self.value))
        return repr(self.value)


class Ui_MainWindow(object):
    def __init__(self):
        logs("Ui_MainWindow类：变量初始化", 0)
        self.mclis = []
        self.dqmcl = ""
        self.javab = ""
        self.javalis = []
        self.dqjaval = ""
        self.errors = 0
        logs("变量初始化完成", 0)
        # self.setSty

    def setupUi(self, MainWindow):
        #uic.loadUi("style.qss", self)
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        logs("加载窗口组件信息", 0)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(590, 530)
        MainWindow.setMinimumSize(QtCore.QSize(590, 530))
        MainWindow.setMaximumSize(QtCore.QSize(590, 530))
        #logs("加载QSS样式表")
        #f=open("style.qss")
        #strs=f.readline()
        #f.close()
        #MainWindow.setStyleSheet(strs)
        logs("加载图标")
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("texture.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QGroupbox{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(0, 255, 255, 100));}")
        logs("加载QT组件")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 510))
        self.centralwidget.setMaximumSize(QtCore.QSize(620, 510))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 0, 581, 511))
        self.groupBox_8.setObjectName("groupBox_8")
        #self.groupBox_8.setStyleSheet(strs)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_2.setGeometry(QtCore.QRect(150, 20, 201, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 50, 121, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(70, 20, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_4.setGeometry(QtCore.QRect(150, 110, 201, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 60, 181, 71))
        self.groupBox_6.setObjectName("groupBox_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 20, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 20, 41, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_5.setGeometry(QtCore.QRect(360, 20, 211, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(13, 20, 181, 201))
        self.label_11.setObjectName("label_11")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 400, 571, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(190, 20, 16, 16))
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(130, 40, 431, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_4.setObjectName("label_4")
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_3.setEnabled(True)
        self.progressBar_3.setGeometry(QtCore.QRect(130, 80, 431, 16))
        self.progressBar_3.setProperty("value", 100)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(90, 20, 91, 16))
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(130, 60, 431, 16))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 250, 571, 151))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 20, 201, 16))
        self.lineEdit_2.setStatusTip("")
        self.lineEdit_2.setWhatsThis("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 40, 91, 16))
        self.lineEdit_3.setStatusTip("")
        self.lineEdit_3.setWhatsThis("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(170, 40, 54, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_7)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_15.setObjectName("label_15")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_4.setGeometry(QtCore.QRect(70, 60, 69, 16))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 54, 12))
        self.label_16.setObjectName("label_16")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 80, 491, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setGeometry(QtCore.QRect(10, 100, 551, 41))
        self.label_17.setObjectName("label_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 20, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_18 = QtWidgets.QLabel(self.groupBox_7)
        self.label_18.setGeometry(QtCore.QRect(170, 60, 61, 16))
        self.label_18.setObjectName("label_18")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox.setGeometry(QtCore.QRect(230, 60, 71, 16))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 141, 231))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 120, 120))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("zh.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 121, 51))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        logs("窗口组件信息加载完成！", 0)
        self.errors += 1
        self.retranslateUi(MainWindow)
        logs(jdt("准备加载版本信息和JAVA列表", 0, 4), 0)
        logs(jdt("准备JAVA列表", 1, 4), 0)
        data1 = javahome.downjavas()[1]
        logs(jdt("获取JAVA列表", 2, 4), 0)
        logs(jdt("准备版本列表", 3, 4), 0)
        data2 = mclist.downmcs()
        logs(jdt("获取版本列表", 4, 4), 0)
        for i in data2:
            self.comboBox.addItem(i)
        for i in data1:
            self.comboBox_2.addItem(i)
        logs(jdt("完成！", 4, 4), 0)
        self.pushButton.clicked.connect(self.slot1)
        logs("绑定信号/槽：slot1", 0)
        self.errors += 1
        self.comboBox.currentIndexChanged.connect(self.slot2)
        logs("绑定信号/槽：slot2", 0)
        self.errors += 1
        self.comboBox_2.currentIndexChanged.connect(self.slot3)
        logs("绑定信号/槽：slot3", 0)
        self.errors += 1
        self.pushButton_2.clicked.connect(self.down)
        logs("绑定信号/槽：down", 0)
        self.errors += 1
        self.pushButton_5.clicked.connect(self.exit)
        logs("绑定信号/槽：exit", 0)
        self.errors += 1
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        logs("加载窗口组件文字", 0)
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "HH的Minecraft启动器"))
        MainWindow.setWindowTitle(_translate("MainWindow", "HH MineCraft Launcher"))
        self.groupBox_8.setTitle(_translate("MainWindow", "HH MineCraft Launcher"))
        sj = hhyhdq.downyhsj()
        self.groupBox.setTitle(_translate("MainWindow", "用户设置"))
        self.lineEdit.setText(_translate("MainWindow", "hh"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "输入游戏名"))
        self.pushButton.setText(_translate("MainWindow", "启动Minecraft"))
        self.groupBox_2.setTitle(_translate("MainWindow", "启动设置"))
        self.label.setText(_translate("MainWindow", "版本选择："))
        self.label_3.setText(_translate("MainWindow", "JAVA选择："))
        self.groupBox_3.setTitle(_translate("MainWindow", "状态栏"))
        self.label_10.setText(_translate("MainWindow", "MB"))
        self.label_5.setText(_translate("MainWindow", "程序没有正在处理的任务"))
        self.label_6.setText(_translate("MainWindow", "当前正在处理的任务:"))
        self.label_4.setText(_translate("MainWindow", "当前任务总处理进度:"))
        self.progressBar_3.setToolTip(_translate("MainWindow", "当前任务进度"))
        self.label_8.setText(_translate("MainWindow", "当前任务处理进度:"))
        self.label_9.setText(_translate("MainWindow", "当前内存占用:"))
        self.label_7.setText(_translate("MainWindow", "当前内存"))
        self.progressBar.setToolTip(_translate("MainWindow", "当前任务进度"))
        self.groupBox_4.setTitle(_translate("MainWindow", "工具"))
        self.groupBox_6.setTitle(_translate("MainWindow", "下载版本"))
        self.pushButton_3.setText(_translate("MainWindow", "下载Minecraft"))
        self.pushButton_4.setText(_translate("MainWindow", "关于"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))
        self.groupBox_5.setTitle(_translate("MainWindow", "自定义内容"))
        self.label_11.setText(_translate("MainWindow", "此处会被替换为自定义内容\n"
                                                       "如果要自定义内容,请修改\n"
                                                       "“自定义主页.txt”中的内容"))
        self.groupBox_7.setTitle(_translate("MainWindow", "启动器设置"))
        self.lineEdit_2.setText(_translate("MainWindow", "0000000000003004998F501A96E01684"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "输入游戏UUID"))
        self.label_12.setText(_translate("MainWindow", "UUID:"))
        self.label_13.setText(_translate("MainWindow", "内存分配:"))
        self.lineEdit_3.setText(_translate("MainWindow", "自动"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "输入游戏UUID"))
        self.label_14.setText(_translate("MainWindow", "MB"))
        self.label_15.setText(_translate("MainWindow", "启动器QSS:"))
        self.label_16.setText(_translate("MainWindow", "JVM参数:"))
        self.lineEdit_4.setText(_translate("MainWindow", "自动"))
        self.label_17.setText(_translate("MainWindow", "编辑帮助:在选项中输入\"自动\"让启动器根据当前环境自动处理,如果要自定义,启动器会替换以下字符串\n"
                                                       " $当前内存 会替换为启动时的系统剩余内存  $当前目录 会替换为启动器工作目录"))
        self.pushButton_2.setText(_translate("MainWindow", "保存启动器设置"))
        self.label_18.setText(_translate("MainWindow", "调试模式:"))
        self.lineEdit.setText(_translate("MainWindow", sj["name"]))
        self.lineEdit_2.setText(_translate("MainWindow", sj["UUID"]))

        logs("窗口组件文字加载完成", 0)
        self.errors += 1

    def slot1(self):
        logs("程序slot1信号/槽被程序调用！", 0)
        try:
            _translate = QtCore.QCoreApplication.translate
            logs("Minecraft版本：" + str(self.dqmcl), 0)
            self.label_5.setText(_translate("MainWindow", "获取Minecraft版本"))
            self.progressBar.setProperty("value", 0)
            # for i in mcjson.jsonhq(str(self.dqmcl)):
            #    print(i,end="")
            self.progressBar.setProperty("value", 1)
            self.errors += 1
            yhm = self.lineEdit.text()
            if yhm == "":
                QMessageBox.information(self.pushButton, "输入错误！",
                                        "请输入用户名")
                return 0
            self.label_5.setText(_translate("MainWindow", "拼接用户名"))
            self.progressBar.setProperty("value", 2)
            self.errors += 1
            # logs("file:")
            # for i in files.downdate():logs(i,end="")
            libslens = files.downdate()
            self.label_5.setText(_translate("MainWindow", "获取Minecraft资源文件"))
            logs(libslens)
            self.errors += 1
            # -Dminecraft.launcher.brand=HML
            self.starjvm = f' -Xmx{memory.downmemory()}m "-Djava.library.path={os.getcwd()}\\.minecraft\\versions\\{self.dqmcl}\\{self.dqmcl}-natives" -cp "'
            logs(self.starjvm)
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "拼接JVM参数"))
            self.progressBar.setProperty("value", 5)
            self.star += self.starjvm
            self.errors += 1
            logs("JVM参数设置完成")
            # for i in libslens:
            #    self.star+=str(i)
            #    self.star+=";"
            self.progressBar.setProperty("value", 7)
            stago = mcjson.jsonhq(str(self.dqmcl))
            self.label_5.setText(_translate("MainWindow", "获取MinecraftJSON数据"))
            self.errors += 1
            # self.star=self.star[:-1]
            self.star += stago[-1]
            self.star += f'{str(os.getcwd())}\\.minecraft\\versions\\{self.dqmcl}\\{self.dqmcl}.jar'
            self.star += '"'
            logs("依赖库读取完成")
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "获取Minecraft依赖库"))
            self.progressBar.setProperty("value", 10)
            self.star += " " + stago[0]
            user = ''
            if stago[2]:
                for i in stago[1]:
                    user += i
                    user += " "
                user = user[:-1]
            else:
                user += stago[1]
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "设置用户配置"))
            self.progressBar.setProperty("value", 15)
            user = user.replace("${auth_player_name}", str(self.lineEdit.text()))
            user = user.replace("${version_name}", '"HML"')
            user = user.replace("${game_directory}", '"' + str(os.getcwd()) + '\\.minecraft"')
            user = user.replace("${assets_root}", '"' + str(os.getcwd()) + '\\.minecraft\\assets"')
            user = user.replace("${assets_index_name}", stago[3])
            user = user.replace("${auth_uuid}", self.lineEdit_2.text())
            user = user.replace("${auth_access_token}", self.lineEdit_2.text())
            user = user.replace("${user_properties}", "{}")
            user = user.replace("${user_type}", "legacy")
            # if int(list(str(self.dqmcl).split("."))[1])>=13:
            # user=user.replace("${version_type}","HH MineCraft Launch")
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "拼接用户配置"))
            logs("用户登入信息已处理:" + user)
            self.progressBar.setProperty("value", 20)
            self.star += " " + user
            self.errors += 1
            self.progressBar.setProperty("value", 30)
            logs("当前启动脚本")
            self.label_5.setText(_translate("MainWindow", "脚本生成完成"))
            logs(self.star)
            file = open("minecraftrun.bat", "w")
            file.write(self.star)
            file.write('\npause')
            file.close()
            self.errors += 1
            logs("指令写入完成")
            self.progressBar.setProperty("value", 50)
            inyes = 0
            if "java" in self.star:
                logs("检测JAVA:已检测", 2)
                inyes += 1
                if "-Djava.library.path=" in self.star:
                    logs("检测natives:已检测", 2)
                    inyes += 1
                    if "-cp " in self.star:
                        logs("检测classpath:已检测", 2)
                        inyes += 1
                        if f'{str(os.getcwd())}\\.minecraft\\versions\\{self.dqmcl}\\{self.dqmcl}.jar' in self.star:
                            logs("检测minecraft版本文件:已检测", 2)
                            inyes += 1
                            if f'{str(os.getcwd())}\\.minecraft\\versions\\{self.dqmcl}\\{self.dqmcl}.jar' in self.star:
                                logs("检测minecraft版本文件:已检测", 2)
                                inyes += 1
            if inyes == 5:
                pass
            else:
                raise HHMCLError("检测到启动脚本不完整！")
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "检测启动脚本完整"))
            logs("运行启动指令")
            # logs(os.system(self.star))
            os.startfile("minecraftrun.bat")
            self.errors += 1
            self.label_5.setText(_translate("MainWindow", "运行启动程序"))
            self.progressBar.setProperty("value", 75)
            logs("启动指令运行完成")
            self.progressBar.setProperty("value", 100)
            self.label_5.setText(_translate("MainWindow", "启动完成！"))
        except:
            QMessageBox.information(self.pushButton, "DEBUG",
                                    "程序出现错误！\n可能出现的问题：\n是否选择了游戏版本或JAVA")
            raise HHMCLError(
                f"程序在启动游戏时出现错误,可能未选择版本或JAVA/JDK,或者启动器不支持该版本 \n 错误代码:{self.errors}")

    def slot2(self):
        logs("程序slot2信号/槽被程序调用！", 0)
        try:
            self.mcb = self.comboBox.currentText()
            logs("MC版本列表选中：" + str(self.mcb), 0)
            self.mclis = mclist.downmcs()
            self.dqmcl = self.mclis[self.comboBox.currentIndex()]
            logs("选中版本：" + str(self.dqmcl), 0)
            self.errors += 1
        except:
            QMessageBox.information(self.pushButton, "DEBUG",
                                    "程序出现错误！\n可能出现的问题：\n是否选择了游戏版本或JAVA")
            raise HHMCLError(
                f"程序在启动游戏时出现错误,可能未选择版本或JAVA/JDK,或者启动器不支持该版本 \n 错误代码:{self.errors}")

    def slot3(self):
        logs("程序slot3信号/槽被程序调用！", 0)
        try:
            self.javab = self.comboBox_2.currentText()
            logs("JAVA版本列表选中：" + str(self.javab), 0)
            self.javalis = javahome.downjavas()[0]
            self.dqjaval = self.javalis + "\\" + javahome.downjavas()[1][
                self.comboBox_2.currentIndex()] + "\\bin\\java.exe"
            logs(self.dqjaval)
            self.star = ""
            # self.star +='"'+self.dqjaval+'"'
            self.star += '"' + self.dqjaval + '"'
            # logs("选中版本：" + str(self.dqjaval), 0)
            self.errors += 1
        except:
            QMessageBox.information(self.pushButton, "DEBUG",
                                    "程序出现错误！\n可能出现的问题：\n是否选择了游戏版本或JAVA")
            raise HHMCLError(
                f"程序在启动游戏时出现错误,可能未选择版本或JAVA/JDK,或者启动器不支持该版本 \n 错误代码:{self.errors}")

    def down(self):
        logs("程序信息保存程序调用！", 0)
        hhyhdq.filling(self.lineEdit_2.text(), self.lineEdit.text())

    def exit(self):
        logs("程序退出")
        self.down()
        raise HHMCLError("程序退出")
