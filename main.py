import os
import sys

from hh的小工具 import *

import javahome
import mclist
import time

t1 = time.time()
import Mainwin
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QMainWindow
print(r"""
|    |  |    |    /\    /\    /=====  |
|=== |  |=== |   /  \  /  \   |       |
|    |  |    |  /    \/    \  \=====  |=====

HH MineCraft Launcher

HH制作
邮箱:hh201136@126.com

参考教程:
https://blog.csdn.net/qq_35312082/article/details/115584661
https://www.runoob.com/python3/python3-tutorial.html
https://minecraft.fandom.com/zh/wiki/%E6%95%99%E7%A8%8B/%E7%BC%96%E5%86%99%E5%90%AF%E5%8A%A8%E5%99%A8
https://tieba.baidu.com/p/4563458950
https://tieba.baidu.com/p/5297508908
""")
logs(f"工作目录{os.getcwd()}", 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    appwin = QMainWindow()
    appui = Mainwin.Ui_MainWindow()
    appui.setupUi(appwin)
    appwin.show()
    logs(f"加载完成！用时{time.time() - t1}", 0)
    try:
        sys.exit(app.exec_())
    finally:
        appui.down()
