import sys
import os
import time
import json

import winreg as reg
import win32api
import shutil
import subprocess


#from main import MainVariables
import tkinter as tk
from ctypes import windll

from tkinter import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Variables(object):
    AlwaysOnTop=False

    UserSizeW=0.0
    UserSizeH=0.0
    Opacity=0.0

    TextColor=''
    BarColor=''
    DefaultPage=''
    Home=''
    
    Display_offset=0
    Height_offset=0
    PeriodicallyReloadURL=0
    
    needExit=False
    
    root = tk.Tk()
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()      
    
    def SaveWidth(val):
        if val <25:
             Variables.UserSizeW=25   
        else:   
             Variables.UserSizeW=val
                          
    def SaveHeigh(val):
        if val <25:
             Variables.UserSizeH=25   
        else:   
             Variables.UserSizeH=val
             
    def SaveOpacity(val):
        if val <33:
             Variables.Opacity=33   
        else:   
             Variables.Opacity=val
    
    def SaveTop(val):
        Variables.AlwaysOnTop=(val)
        
    def SaveTextColor(val):
        Variables.TextColor=val
    
    def SaveBarColor(val):
        Variables.BarColor=val

    def SaveDefaultUrl(val):
        Variables.DefaultPage=val
        
    def SaveHomeUrl(val):        
        Variables.Home=val
    
    def SavePeriodicallyReloadURL(val):
        Variables.PeriodicallyReloadURL=val
        
    def SaveALL():
        data={
                "DefaultPage": "{}".format(Variables.DefaultPage),
                "Home": "{}".format(Variables.Home),
                "TextColor": "{}".format(Variables.TextColor),
                "BarColor": "{}".format(Variables.BarColor),
                "UserSizeW": Variables.UserSizeW,
                "UserSizeH": Variables.UserSizeH,
                "Opacity": Variables.Opacity,
                "AlwaysOnTop": Variables.AlwaysOnTop,
                "Display_offset":Variables.Display_offset,
                "Height_offset":Variables.Height_offset,
                "PeriodicallyReloadURL":Variables.PeriodicallyReloadURL
        }
        
        #cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        #cwd=str(str(cwd) + r'\Settings\Settings.json')
        
        cwd=os.path.expanduser(os.getenv('USERPROFILE'))
        cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
        
        try:
            cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\Setting": Access is denied.', 'Error')

        try:
            with open(cwd, 'w') as outfile:
                json.dump(data, outfile)
        except:
            win32api.MessageBox(0, 'Unable to write to file: Access is denied.', 'Error')

        Variables.needExit=True

        cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        cwd=cwd.replace('binaries', r'binaries\Web Widget.exe')
        
        subprocess.Popen([cwd])
                
        Closing.Close()

        #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        
    def ResetALL():
        data={
                "DefaultPage": "https://www.msn.com/pt-br/feed?ocid=winp2fptaskbar",
                "Home": "https://www.google.com/",
                "TextColor": "blue",
                "BarColor": "#bcccd6",
                "UserSizeW": 54,
                "UserSizeH": 100,
                "Opacity": 89,
                "AlwaysOnTop": 0,
                "Display_offset":0,
                "Height_offset":0,
                "PeriodicallyReloadURL":2
        }
        
        print(data)
        
        #cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        #cwd=str(str(cwd) + r'\Settings\Settings.json')
        
        cwd=os.path.expanduser(os.getenv('USERPROFILE'))
        cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
        
        try:
            cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\Setting": Access is denied.', 'Error')

        try:
            with open(cwd, 'w') as outfile:
                json.dump(data, outfile)
        except:
            win32api.MessageBox(0, 'Unable to write to file: Access is denied.', 'Error')

        Variables.needExit=True
                
        cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        cwd=cwd.replace('binaries', r'binaries\Web Widget.exe')
        
        subprocess.Popen([cwd])
        
        Closing.Close()

        #os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #import main
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(520, 550)
        #MainWindow.resize(520, 491)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser_3.sizePolicy().hasHeightForWidth())
        self.textBrowser_3.setSizePolicy(sizePolicy)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout.addWidget(self.textBrowser_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 33))
        self.checkBox_2.setMaximumSize(QtCore.QSize(16777215, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox_2.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_2.setIconSize(QtCore.QSize(24, 24))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addWidget(self.checkBox_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(999999999, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacerItem_2 = QtWidgets.QSpacerItem(999999999, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addItem(spacerItem_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.horizontalLayout_7.addWidget(self.textBrowser_7, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textColor = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textColor.sizePolicy().hasHeightForWidth())
        self.textColor.setSizePolicy(sizePolicy)
        self.textColor.setMinimumSize(QtCore.QSize(330, 0))
        self.textColor.setMaximumSize(QtCore.QSize(300, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textColor.setFont(font)
        self.textColor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textColor.setOverwriteMode(True)
        self.textColor.setTabStopDistance(0.0)
        self.textColor.setObjectName("textColor")
        self.horizontalLayout_7.addWidget(self.textColor, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_9.sizePolicy().hasHeightForWidth())
        self.textBrowser_9.setSizePolicy(sizePolicy)
        self.textBrowser_9.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_9.setFont(font)
        self.textBrowser_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.horizontalLayout_9.addWidget(self.textBrowser_9, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.barColor = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.barColor.sizePolicy().hasHeightForWidth())
        self.barColor.setSizePolicy(sizePolicy)
        self.barColor.setMinimumSize(QtCore.QSize(330, 0))
        self.barColor.setMaximumSize(QtCore.QSize(300, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.barColor.setFont(font)
        self.barColor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.barColor.setAutoFillBackground(True)
        self.barColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.barColor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.barColor.setOverwriteMode(True)
        self.barColor.setTabStopWidth(0)
        self.barColor.setObjectName("barColor")
        self.horizontalLayout_9.addWidget(self.barColor, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.defaultUrl = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.defaultUrl.sizePolicy().hasHeightForWidth())
        self.defaultUrl.setSizePolicy(sizePolicy)
        self.defaultUrl.setMinimumSize(QtCore.QSize(330, 0))
        self.defaultUrl.setMaximumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.defaultUrl.setFont(font)
        self.defaultUrl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.defaultUrl.setAutoFillBackground(True)
        self.defaultUrl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.defaultUrl.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.defaultUrl.setOverwriteMode(True)
        self.defaultUrl.setTabStopWidth(0)
        self.defaultUrl.setObjectName("defaultUrl")
        self.defaultUrl.setVerticalScrollBarPolicy(1)
        self.horizontalLayout_3.addWidget(self.defaultUrl, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_10.sizePolicy().hasHeightForWidth())
        self.textBrowser_10.setSizePolicy(sizePolicy)
        self.textBrowser_10.setMaximumSize(QtCore.QSize(130, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_10.setFont(font)
        self.textBrowser_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.horizontalLayout_10.addWidget(self.textBrowser_10, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.homeUrl = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.homeUrl.sizePolicy().hasHeightForWidth())
        self.homeUrl.setSizePolicy(sizePolicy)
        self.homeUrl.setMinimumSize(QtCore.QSize(330, 0))
        self.homeUrl.setMaximumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.homeUrl.setFont(font)
        self.homeUrl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.homeUrl.setAutoFillBackground(True)
        self.homeUrl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homeUrl.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.homeUrl.setOverwriteMode(True)
        self.homeUrl.setTabStopWidth(0)
        self.homeUrl.setObjectName("homeUrl")
        self.homeUrl.setVerticalScrollBarPolicy(1)
        self.horizontalLayout_10.addWidget(self.homeUrl, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(131, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sWidth = QtWidgets.QSlider(self.centralwidget)
        self.sWidth.setStyleSheet("")
        self.sWidth.setOrientation(QtCore.Qt.Horizontal)
        self.sWidth.setObjectName("sWidth")
        self.horizontalLayout.addWidget(self.sWidth, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser_5.sizePolicy().hasHeightForWidth())
        self.textBrowser_5.setSizePolicy(sizePolicy)
        self.textBrowser_5.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_5.setMaximumSize(QtCore.QSize(131, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_5.setStyleSheet("")
        self.textBrowser_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_5.addWidget(self.textBrowser_5, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sHeigh = QtWidgets.QSlider(self.centralwidget)
        self.sHeigh.setOrientation(QtCore.Qt.Horizontal)
        self.sHeigh.setObjectName("sHeigh")
        self.horizontalLayout_5.addWidget(self.sHeigh, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser_6.sizePolicy().hasHeightForWidth())
        self.textBrowser_6.setSizePolicy(sizePolicy)
        self.textBrowser_6.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_6.setMaximumSize(QtCore.QSize(131, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_6.setStyleSheet("")
        self.textBrowser_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.horizontalLayout_6.addWidget(self.textBrowser_6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sOpacity = QtWidgets.QSlider(self.centralwidget)
        self.sOpacity.setOrientation(QtCore.Qt.Horizontal)
        self.sOpacity.setObjectName("sOpacity")
        self.horizontalLayout_6.addWidget(self.sOpacity, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        cwd=cwd.replace(r'binaries', r'ico\ico48.ico')
        
        MainWindow.setWindowIcon(QtGui.QIcon(cwd))

        self.checkBox.setCheckState(Variables.AlwaysOnTop)
        self.checkBox_2.setCheckState(Variables.PeriodicallyReloadURL)
        
        self.sWidth.setValue(round(Variables.UserSizeW))
        self.sHeigh.setValue(round(Variables.UserSizeH))
        self.sOpacity.setValue(round(Variables.Opacity))

        self.textColor.setText(Variables.TextColor)
        self.barColor.setText(Variables.BarColor)
        self.defaultUrl.setText(Variables.DefaultPage)
        self.homeUrl.setText(Variables.Home)
        
        self.checkBox.stateChanged.connect(lambda: Variables.SaveTop(self.checkBox.checkState()))
        self.checkBox_2.stateChanged.connect(lambda: Variables.SavePeriodicallyReloadURL(self.checkBox_2.checkState()))
        
        self.sWidth.valueChanged.connect(lambda: Variables.SaveWidth(self.sWidth.value()))
        self.sHeigh.valueChanged.connect(lambda: Variables.SaveHeigh(self.sHeigh.value()))
        self.sOpacity.valueChanged.connect(lambda: Variables.SaveOpacity(self.sOpacity.value()))
        
        self.textColor.textChanged.connect(lambda: Variables.SaveTextColor(self.textColor.toPlainText()))
        self.barColor.textChanged.connect(lambda: Variables.SaveBarColor(self.barColor.toPlainText()))
        self.defaultUrl.textChanged.connect(lambda: Variables.SaveDefaultUrl(self.defaultUrl.toPlainText()))
        self.homeUrl.textChanged.connect(lambda: Variables.SaveHomeUrl(self.homeUrl.toPlainText()))             
        
        self.pushButton.released.connect(lambda: Variables.SaveALL())
        
        self.pushButton_2.released.connect(lambda: Variables.ResetALL())

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Widget Settings"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aaff00;\">Web Widget Settings</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Always On Top               "))
        self.checkBox_2.setText(_translate("MainWindow", "Periodically Reload URL "))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text Color</p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bar Color</p></body></html>"))
        self.barColor.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Default Page URL</p></body></html>"))
        self.defaultUrl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Home Page URL</p></body></html>"))
        self.homeUrl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">App Width</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">App Heigh</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">App Opacity</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))

#if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #app.setQuitOnLastWindowClosed(False)
    #sys.exit(app.exec_())

class Closing(object):
    def Close():
        if Variables.needExit==True:
            for window in QApplication.topLevelWidgets():
                x=str(window.objectName)
                window.close()
                quit()
        else:
            for window in QApplication.topLevelWidgets():
                x=str(window.objectName)

                if 'MWindow' not in x:
                    #print(window.objectName)
                    window.close()
