import ctypes
import sys
import os
import getpass
import threading

from Settings import Closing
from Settings import Variables
from Settings import Ui_MainWindow

import webbrowser
import shutil
import winreg as reg
import win32api
import tkinter as tk
import pandas as pd
import json

from ctypes import windll

import time
import pystray

from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
    
class RegStart():    
    def add_to_startup(file_path=""):
        USER_NAME = getpass.getuser()
        selfpath=str(os.path.dirname(os.path.realpath(__file__)))
        finalpath=str(selfpath+r"\Web Widget.exe")
        
        if file_path == "":
            file_path =finalpath
            print(file_path)
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "WebWidget.bat", "w+") as bat_file:
            bat_file.write(r'start "" "%s"' % file_path)

class MainVariables(object):
    DefaultPage='https://www.msn.com/pt-br/feed?ocid=winp2fptaskbar'
    Home='https://www.google.com/'
    TextColor='blue'
    BarColor='#bcccd6'

    UserSizeW=54
    UserSizeH=100
    Opacity=89

    AlwaysOnTop=0
    PeriodicallyReloadURL=2
    
    Display_offset=0
    Height_offset=0
    
    FisrtAccess=False
    toReload=False
    
    Data={}
    
    CurrentURL=''
    
    def openSaveFile():
        #cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        
        #cwd=str(str(cwd) + r'\Settings\Settings.json')
        
        try:
            cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings'))
                MainVariables.FisrtAccess=True
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\Setting": Access is denied.', 'Error')
        
        try:
            cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            cwd=cwd=str(str(cwd) + r'\Documents\WebWidget\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Settings\Settings.json')):
                print('')
            else:
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

                with open(cwd, 'w') as outfile:
                    json.dump(data, outfile)
                
                MainVariables.FisrtAccess=True                    
        except:
            win32api.MessageBox(0, r'Unable to create file "Settings.json": Access is denied.', 'Error')
        
        try:
            File= open(cwd)
            MainVariables.Data=json.load(File)
            
            MainVariables.UserSizeH=MainVariables.Data['UserSizeH']
            MainVariables.UserSizeW=MainVariables.Data['UserSizeW']
            MainVariables.Opacity=MainVariables.Data['Opacity']

            MainVariables.TextColor=MainVariables.Data['TextColor']
            MainVariables.BarColor=MainVariables.Data['BarColor']
            MainVariables.DefaultPage=MainVariables.Data['DefaultPage']
            MainVariables.Home=MainVariables.Data['Home']
            
            MainVariables.AlwaysOnTop=MainVariables.Data['AlwaysOnTop']
            MainVariables.Display_offset=MainVariables.Data['Display_offset']
            MainVariables.Height_offset=MainVariables.Data['Height_offset']
            MainVariables.PeriodicallyReloadURL=MainVariables.Data['PeriodicallyReloadURL']

        except:
            win32api.MessageBox(0, 'Unable to access settings: Access is denied or corrupted file.', 'Error')
        
            
class SetSettingsWindow():
    Q2SettingsWindow=None

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        pass

    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    @QtCore.pyqtSlot(QtCore.QUrl)
    def on_url_changed(self, url):
        page = self.sender()
        self.setUrl(url)
        page.deleteLater()
        
class CSettings(QMainWindow):
    def __init__(self, parent=None):
        super(CSettings, self).__init__(parent)
        
        Variables.AlwaysOnTop=MainVariables.AlwaysOnTop
        
        Variables.UserSizeH=MainVariables.UserSizeH
        Variables.UserSizeW=MainVariables.UserSizeW
        Variables.Opacity=MainVariables.Opacity

        Variables.TextColor=MainVariables.TextColor
        Variables.BarColor=MainVariables.BarColor
        Variables.DefaultPage=MainVariables.DefaultPage
        Variables.Home=MainVariables.Home
        
        Variables.Display_offset=MainVariables.Display_offset
        Variables.Height_offset=MainVariables.Height_offset
        
        Variables.PeriodicallyReloadURL=MainVariables.PeriodicallyReloadURL
        
        self.window = QtWidgets.QMainWindow()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    
class MWindow(QMainWindow):
    def __init__(self):
        super(MWindow, self).__init__()
        
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Cache')):
                shutil.rmtree((str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Cache')))
        except:
            #win32api.MessageBox(0, r'Unable to delete folder "\Documents\WebWidget\Cache": Access is denied.', 'Error')
            time.sleep(3)
           
        try:                
             if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Storage')):
                 shutil.rmtree((str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Storage')))
        except:
             #win32api.MessageBox(0, r'Unable to delete folder "\Documents\WebWidget\Storage": Access is denied.', 'Error')
            time.sleep(3)

        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropCache')):
                shutil.rmtree((str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropCache')))
        except:
            #win32api.MessageBox(0, r'Unable to delete folder "\Documents\WebWidget\DropCache": Access is denied.', 'Error')
            time.sleep(3)
            
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropStorage')):
                shutil.rmtree((str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropStorage')))
        except:
            #win32api.MessageBox(0, r'Unable to delete folder "\Documents\WebWidget\DropStorage": Access is denied.', 'Error') 
            time.sleep(3)
        
        MainVariables.openSaveFile()

        self.setWindowFlag(QtCore.Qt.Tool)

        self.browser = QWebEngineView()
                
        if MainVariables.AlwaysOnTop == 2:
            QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Cache')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Cache'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\Cache": Access is denied.', 'Error')
            
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Storage')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Storage'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\Storage": Access is denied.', 'Error')
            
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropCache')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropCache'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\DropCache": Access is denied.', 'Error')
            
        try:                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropStorage')):
                print('')
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropStorage'))
        except:
            win32api.MessageBox(0, r'Unable to create folder "\Documents\WebWidget\DropStorage": Access is denied.', 'Error')          
                
        profile = QWebEngineProfile("my_profile", self.browser)
        
        profile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)
        
        profile.defaultProfile().setCachePath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropCache'))
        profile.defaultProfile().setPersistentStoragePath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\DropStorage'))
        profile.defaultProfile().setDownloadPath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Downloads'))

        profile.setCachePath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Cache'))
        profile.setPersistentStoragePath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\WebWidget\Storage'))
        profile.setDownloadPath(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Downloads'))
        
        webpage = QWebEnginePage(profile, self.browser)
        webpage.settings().setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, True)
                
        self.setContentsMargins(0,1,0,0)
        
        self.Parent = QWidget()
        self.Parent.setAutoFillBackground(False)
        self.Parent.setContentsMargins(0,1,0,0)
        self.vbox = QVBoxLayout()
        self.vbox.setContentsMargins(0,1,0,0)
        self.vbox.setSpacing(0)
        self.Parent.setLayout(self.vbox)
                
        page = WebEnginePage(self.browser)
        self.browser.setPage(page)
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.browser.setStyleSheet("color: black; background-color: #aaaa7f;")
        self.setStyleSheet("color: black; background-color:"+MainVariables.BarColor+";")
        self.setWindowOpacity(MainVariables.Opacity/100)   
        
        #self.browser.setUrl(QUrl('https://www.google.com.br/'))
        #self.setCentralWidget(self.browser)
        self.setCentralWidget(self.Parent)
        
        #self.showMaximized()
        
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setContentsMargins(0,0,0,0)
        
        navbar.setMovable(False)
        navbar.setStyleSheet('color:'+MainVariables.TextColor+';')

        back_btn = QAction('⟵', self)
        back_btn.triggered.connect(self.browser.back)
        back_btn.setFont(QFont('Arial', 13))
        navbar.addAction(back_btn)

        forward_btn = QAction('⟶', self)
        forward_btn.triggered.connect(self.browser.forward)
        forward_btn.setFont(QFont('Arial', 13))
        navbar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        reload_btn.setFont(QFont('Arial', 14))
        navbar.addAction(reload_btn)

        home_btn = QAction('집', self)
        home_btn.triggered.connect(self.navigate_home)
        home_btn.setFont(QFont('Arial', 13))
        navbar.addAction(home_btn)
        
        newtab_btn = QAction('↑', self)
        newtab_btn.triggered.connect(self.new_tab)
        newtab_btn.setFont(QFont('Arial', 13))
        navbar.addAction(newtab_btn)

        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet("border : 1px solid grey")
        self.url_bar.setFont(QFont('Arial', 9))
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        Settings_btn = QAction('⌬', self)
        Settings_btn.setFont(QFont('Arial', 13))
        Settings_btn.triggered.connect(self.Settings)
        navbar.addAction(Settings_btn)
       
        Close_btn = QAction('❌', self)
        Close_btn.setFont(QFont('Arial', 13))
        Close_btn.triggered.connect(self.Close)
        navbar.addAction(Close_btn)

        self.browser.urlChanged.connect(self.update_url)
        
        ProgressBarsizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.Progressbar=QProgressBar()
        self.Progressbar.setObjectName("Progressbar")
        self.Progressbar.setValue(50)
        self.Progressbar.setTextVisible(False) 
        self.Progressbar.setMaximumHeight(2)
        #self.Progressbar.setStyleSheet("border-color: rgba(0, 0, 0, 0);")
        self.Progressbar.setSizePolicy(ProgressBarsizePolicy)
        
        #self.Spacer0=QSpacerItem(0,20,QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        #self.vbox.addSpacerItem(self.Spacer0)
        self.vbox.addWidget(self.Progressbar)
        self.vbox.addWidget(self.browser)
       
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Web Widget")
        self.setGeometry((50+MainVariables.Display_offset), (MainVariables.Height_offset+50), round(MainVariables.UserSizeW/105*width), round(MainVariables.UserSizeH/115*height))
        
        cwd = os.path.dirname(os.path.realpath(__file__)) # pasta atual
        cwd=cwd.replace('binaries', r'ico\ico32.ico')

        
        trayicon = QSystemTrayIcon(QIcon(cwd), parent=app)
        trayicon.setToolTip('Web Widget is running!')
        trayicon.show()
        
        menu = QMenu()
        
        SettingsAction = menu.addAction('Settings')
        SettingsAction.triggered.connect(self.Settings)

        exitAction = menu.addAction('Exit')
        exitAction.triggered.connect(self.Close)
        
        trayicon.setContextMenu(menu)
        
        self.browser.page().loadStarted.connect(lambda:
            self.loadStartedHandler())

        self.browser.load(QtCore.QUrl(MainVariables.DefaultPage))

        if MainVariables.FisrtAccess == True:
            RegStart.add_to_startup("")
            
        self.show()

    def loadStartedHandler(self):
        self.browser.page().loadStarted.disconnect()
        
        self.Progressbar.setValue(12)
        
        self.browser.page().loadProgress.connect(lambda:
            self.loadProgressHandler())
    
    def loadProgressHandler(self):
        if self.Progressbar.value() < 100:
            if self.Progressbar.value() + 25 >= 100:
                self.browser.page().loadProgress.disconnect()
                self.Progressbar.setValue(100)
            else:
                self.Progressbar.setValue(self.Progressbar.value()+25)
        else:
            self.browser.page().loadProgress.disconnect()

        self.browser.page().loadFinished.connect(lambda:
            self.loadFinishedHandler())

    def loadFinishedHandler(self):
        self.browser.page().loadFinished.disconnect()
        
        self.Progressbar.setValue(0)
        
        self.SaveCurrentURL(self.browser.page().url().toString())

        self.browser.page().loadStarted.connect(lambda:
            self.loadStartedHandler())
                               
    def SaveCurrentURL(self, x):
        MainVariables.CurrentURL=str(x)

    def navigate_home(self):
        self.browser.setUrl(QUrl(MainVariables.Home))
        
    def ResetProgressBar(self):
        self.Progressbar.setValue(0)

        self.SaveCurrentURL(self.browser.page().url().toString())
        
    def ReloadPage(self):
        if MainVariables.PeriodicallyReloadURL == 2:    
            self.browser.setUrl(QUrl(MainVariables.CurrentURL))
                
    def new_tab(self):
        try:
            webbrowser.open(MainVariables.CurrentURL, new=2)
        except:
            webbrowser.open(MainVariables.CurrentURL, new=1)

    def navigate_to_url(self):
        url = self.url_bar.text()
        
        if url.find(r".com") != -1 and (url.find(r"https://www.") == -1 or url.find(r"https://") == -1 or url.find(r"www.") == -1):
            url=str(r"https://{}").format(url)
            self.browser.setUrl(QUrl(url))

        elif url.find(r".com") == -1 or url.find(r"https://www.") == -1 or url.find(r"https://") == -1 or url.find(r"www.") == -1:
            url=str(r"https://www.google.com/search?q={}").format(url)
            self.browser.setUrl(QUrl(url))
            
        else:  
            self.browser.setUrl(QUrl(url))
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())
    
    def Settings(self):
        if SetSettingsWindow.Q2SettingsWindow == None:
            
            SetSettingsWindow.Q2SettingsWindow=CSettings(self)
            
        else:
            Closing.Close()
            
            SetSettingsWindow.Q2SettingsWindow=None
            
            time.sleep(0.25)
            
            self.Settings()
        
    def Close(self):
        self.close()
        quit()

time.sleep(1.0)

if __name__ == "__main__":    
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    cwd2 = os.path.dirname(os.path.realpath(__file__)) # pasta atual
    cwd2=cwd2.replace(r'binaries', r'ico\ico48.ico')
        
    app.setWindowIcon(QtGui.QIcon(cwd2))
    
    myappid = 'Suundumused.WebWidget.WebWidget.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
    QApplication.setApplicationName('Web Widget')
    
    window = MWindow()
    
    timer2 = QtCore.QTimer()
    timer2.timeout.connect(window.ResetProgressBar)
    timer2.start(30*1000)
    
    timer = QtCore.QTimer()
    timer.timeout.connect(window.ReloadPage)
    timer.start(900*1000)
    
    app.exec_()
