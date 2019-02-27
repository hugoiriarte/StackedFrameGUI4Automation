# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Hugo\Desktop\app.ui'
#

from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from tkinter import messagebox
import os
import csv
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import datetime
import os

class Ui_MarijuanaDoctorsV3(object):
    def setupUi(self, MarijuanaDoctorsV3):
        MarijuanaDoctorsV3.setObjectName("MarijuanaDoctorsV3")
        MarijuanaDoctorsV3.resize(560, 688)

        self.centralwidget = QtWidgets.QWidget(MarijuanaDoctorsV3)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 0, 541, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        
        #Page1 DONE
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.page1)
        self.label_3.setGeometry(QtCore.QRect(180, 60, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.page1)
        self.radioButton.setGeometry(QtCore.QRect(80, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.page1)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(self.page1)
        self.label_4.setGeometry(QtCore.QRect(230, 140, 101, 16))
        self.label_4.setObjectName("label_4")
        self.practiceName = QtWidgets.QTextEdit(self.page1)
        self.practiceName.setGeometry(QtCore.QRect(60, 180, 161, 31))
        self.practiceName.setObjectName("practiceName")
        self.doctorName = QtWidgets.QTextEdit(self.page1)
        self.doctorName.setGeometry(QtCore.QRect(340, 180, 161, 31))
        self.doctorName.setObjectName("doctorName")
        self.searchPractice = QtWidgets.QPushButton(self.page1)
        self.searchPractice.setGeometry(QtCore.QRect(240, 330, 75, 23))
        self.searchPractice.setObjectName("searchPractice")
        self.label_5 = QtWidgets.QLabel(self.page1)
        self.label_5.setGeometry(QtCore.QRect(150, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page1)
        self.label_6.setGeometry(QtCore.QRect(150, 270, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.startDate = QtWidgets.QTextEdit(self.page1)
        self.startDate.setGeometry(QtCore.QRect(230, 230, 121, 31))
        self.startDate.setObjectName("startDate")
        self.endDate = QtWidgets.QTextEdit(self.page1)
        self.endDate.setGeometry(QtCore.QRect(230, 270, 121, 31))
        self.endDate.setObjectName("endDate")
        self.label_7 = QtWidgets.QLabel(self.page1)
        self.label_7.setGeometry(QtCore.QRect(250, 320, 47, 13))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.page1)
        self.label_9.setGeometry(QtCore.QRect(230, 100, 101, 31))
        self.clearButton1 = QtWidgets.QPushButton(self.page1)
        self.clearButton1.setGeometry(QtCore.QRect(460, 40, 75, 23))
        self.clearButton1.setObjectName("clearButton")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pAnalyticsOut = QtWidgets.QTextBrowser(self.page1)
        self.pAnalyticsOut.setGeometry(QtCore.QRect(50, 370, 451, 261))
        self.pAnalyticsOut.setObjectName("pAnalyticsOut")
        self.pushButton_2 = QtWidgets.QPushButton(self.page1)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pageTwo)
        self.stackedWidget.addWidget(self.page1)
        self.searchPractice.clicked.connect(self.practiceSearchDateRange)
        self.clearButton1.clicked.connect(self.cleatPractice)

        #Page2 
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label_8 = QtWidgets.QLabel(self.page2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 121, 51))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.page2)
        self.label_10.setGeometry(QtCore.QRect(180, 60, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page2)
        self.label_11.setGeometry(QtCore.QRect(230, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.radioButton_3 = QtWidgets.QRadioButton(self.page2)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.page2)
        self.radioButton_4.setGeometry(QtCore.QRect(340, 140, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.clearButton2 = QtWidgets.QPushButton(self.page2)
        self.clearButton2.setGeometry(QtCore.QRect(460, 40, 75, 23))
        self.clearButton2.setObjectName("clearButton")        
        self.practiceName2 = QtWidgets.QTextEdit(self.page2)
        self.practiceName2.setGeometry(QtCore.QRect(60, 170, 161, 31))
        self.practiceName2.setObjectName("practiceName2")
        self.doctorName2 = QtWidgets.QTextEdit(self.page2)
        self.doctorName2.setGeometry(QtCore.QRect(330, 170, 161, 31))
        self.doctorName2.setObjectName("doctorName2")
        self.searchPractice2 = QtWidgets.QPushButton(self.page2)
        self.searchPractice2.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.searchPractice2.setMinimumSize(QtCore.QSize(75, 0))
        self.searchPractice2.setObjectName("searchPractice2")
        self.pAnalyticsOut2 = QtWidgets.QTextBrowser(self.page2)
        self.pAnalyticsOut2.setGeometry(QtCore.QRect(40, 250, 471, 381))
        self.pAnalyticsOut2.setObjectName("pAnalyticsOut2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page2)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pageThree)
        self.clearButton2.clicked.connect(self.clearPractice30Days) 
        self.searchPractice2.clicked.connect(self.practice30days)       
        self.stackedWidget.addWidget(self.page2)

        #Page3 DONE
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label_12 = QtWidgets.QLabel(self.page3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 121, 51))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page3)
        self.label_13.setGeometry(QtCore.QRect(220, 60, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page3)
        self.label_14.setGeometry(QtCore.QRect(180, 140, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.state = QtWidgets.QTextEdit(self.page3)
        self.state.setGeometry(QtCore.QRect(310, 150, 51, 31))
        self.state.setObjectName("state")
        self.label_15 = QtWidgets.QLabel(self.page3)
        self.label_15.setGeometry(QtCore.QRect(230, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.searchState = QtWidgets.QPushButton(self.page3)
        self.searchState.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.searchState.setObjectName("searchState")
        
        self.searchState.clicked.connect(self.searchState30Days)

        self.stateHitsOut = QtWidgets.QTextBrowser(self.page3)
        self.stateHitsOut.setGeometry(QtCore.QRect(40, 240, 471, 381))
        self.stateHitsOut.setObjectName("stateHitsOut")
        self.pushButton_4 = QtWidgets.QPushButton(self.page3)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.pageFour)
        self.clearButton = QtWidgets.QPushButton(self.page3)
        self.clearButton.setGeometry(QtCore.QRect(460, 40, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clearHits)    
        self.stackedWidget.addWidget(self.page3)

        #Page4
        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.label_16 = QtWidgets.QLabel(self.page4)
        self.label_16.setGeometry(QtCore.QRect(220, 60, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page4)
        self.label_17.setGeometry(QtCore.QRect(10, 20, 121, 51))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.page4)
        self.label_18.setGeometry(QtCore.QRect(220, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page4)
        self.label_19.setGeometry(QtCore.QRect(160, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.startDateState = QtWidgets.QTextEdit(self.page4)
        self.startDateState.setGeometry(QtCore.QRect(250, 160, 131, 31))
        self.startDateState.setObjectName("startDateState")
        self.label_20 = QtWidgets.QLabel(self.page4)
        self.label_20.setGeometry(QtCore.QRect(160, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.endDateState = QtWidgets.QTextEdit(self.page4)
        self.endDateState.setGeometry(QtCore.QRect(250, 210, 131, 31))
        self.endDateState.setObjectName("endDateState")
        self.searchState2 = QtWidgets.QPushButton(self.page4)
        self.searchState2.setGeometry(QtCore.QRect(240, 260, 75, 23))
        self.searchState2.setObjectName("searchState2")
        self.stateHitsOut2 = QtWidgets.QTextBrowser(self.page4)
        self.stateHitsOut2.setGeometry(QtCore.QRect(40, 300, 471, 331))
        self.stateHitsOut2.setObjectName("stateHitsOut2")
        self.textBrowser = QtWidgets.QTextEdit(self.page4)
        self.textBrowser.setGeometry(QtCore.QRect(420, 180, 31, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.page4)
        self.pushButton.setGeometry(QtCore.QRect(460, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pageOne)
        self.stackedWidget.addWidget(self.page4)
        MarijuanaDoctorsV3.setCentralWidget(self.centralwidget)

        #Menu bar
        self.menubar = QtWidgets.QMenuBar(MarijuanaDoctorsV3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MarijuanaDoctorsV3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MarijuanaDoctorsV3)
        self.statusbar.setObjectName("statusbar")
        MarijuanaDoctorsV3.setStatusBar(self.statusbar)
        self.actionPractice_Date_Range = QtWidgets.QAction(MarijuanaDoctorsV3)
        self.actionPractice_Date_Range.setObjectName("actionPractice_Date_Range")
        self.actionPractice_Last_30_Days = QtWidgets.QAction(MarijuanaDoctorsV3)
        self.actionPractice_Last_30_Days.setObjectName("actionPractice_Last_30_Days")
        self.actionState_Hits_Last_30_Days = QtWidgets.QAction(MarijuanaDoctorsV3)
        self.actionState_Hits_Last_30_Days.setObjectName("actionState_Hits_Last_30_Days")
        self.actionState_Hits_Date_Range = QtWidgets.QAction(MarijuanaDoctorsV3)
        self.actionState_Hits_Date_Range.setObjectName("actionState_Hits_Date_Range")
        self.menuMenu.addAction(self.actionPractice_Date_Range)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionPractice_Last_30_Days)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionState_Hits_Last_30_Days)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionState_Hits_Date_Range)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MarijuanaDoctorsV3)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MarijuanaDoctorsV3)

    def clearHits(self):
        self.stateHitsOut.clear()
    def cleatPractice(self):
       self.pAnalyticsOut.clear() 
    
    def clearPractice30Days(self):
        self.pAnalyticsOut2.clear()

    def practice30days(self):
        practiceNameEntry = self.practiceName2.toPlainText()
        doctorNameEntry = self.doctorName2.toPlainText()
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  
        if len(practiceNameEntry) == 0 and len(doctorNameEntry) == 0:
            self.dialog4 = QtWidgets.QErrorMessage()                        
            self.dialog4.showMessage('Enter Practice Name')            

        if len(practiceNameEntry) != 0:
            url = 'https://www.marijuanadoctors.com/user/login'
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            #Initate driver
            chromedriver = desktop + '/chromedriver'
            driver = webdriver.Chrome(chromedriver,chrome_options=options)
            #Get the URL
            driver.get(url)
            try:
                popUpRadio = driver.find_element_by_id('is21')
                popUpRadio.click()
                submit = driver.find_element_by_id('submitAgeGate')
                submit.click()
            except NoSuchElementException as exception:
                print("No pop up")
            try:
                userName = driver.find_element_by_id('qf_login_full__fields__email')
                userName.send_keys('ray@marijuanadoctors.com')
                pw = driver.find_element_by_id('qf_login_full__fields__password')
                pw.send_keys('Made2win$')
                logIn = driver.find_element_by_id('qf_login_full__submit')
                logIn.click()
                driver.implicitly_wait(5)
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
            try:
                mobileSuperAd = driver.find_element_by_css_selector('body > header > div.tab_header > div > ul > li:nth-child(1) > a')
                mobileSuperAd.click()
                time.sleep(5)
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")  
            
            #HITS last 30 days
            analytics = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(1) > a')
            analytics.click()
            time.sleep(3)
            searchIn = driver.find_element_by_css_selector('#practice_view_count_filter > label > input')
            searchIn.send_keys(practiceNameEntry)
            hundoHits = driver.find_element_by_css_selector('#practice_view_count_length > label > select > option:nth-child(4)')
            hundoHits.click
            try:
                aHits = driver.find_elements_by_css_selector('#practice_view_count > tbody > tr > td.sorting_1')
            except NoSuchElementException as exception:
                print('Error')
            hits = []
            for i in aHits:
                hits.append(int(i.text))
            totalHits = sum(hits)
            self.pAnalyticsOut2.append("Hits for the last 30 days is: " + str(totalHits))#text.insert(INSERT,)

            #APPT REQUEST
            clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
            clicks.click()
            time.sleep(3)
            appointmentRequestQuery = driver.find_elements_by_css_selector('#appointment_requests > div')
            appointmentRequestQuery[3].click()
            time.sleep(1)
            searchToday = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
            searchToday.send_keys(practiceNameEntry)#practiceEntry.get()
            time.sleep(1)
            apptReq = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
            lurksss = re.findall('\d+', apptReq)
            self.pAnalyticsOut2.append("\nAppointment requests for the last 30 days is: " + str(lurksss[2]))#text.insert(INSERT,)
            

            #Appt Booked        
            clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
            clicks.click()
            apptBooked = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(2) > div:nth-child(4)')
            apptBooked.click()
            apptBookedInput = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
            apptBookedInput.send_keys(practiceNameEntry)
            apptBook = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
            lurks = re.findall('\d+', apptBook)
            self.pAnalyticsOut2.append("\nAppointments Booked for the last 30 days is: " + str(lurks[2]))#text.insert(INSERT,)
            
            #TeleMedicine Appointments
            clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
            clicks.click()
            tele = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(3) > div:nth-child(4)')
            tele.click()
            teleInput = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
            teleInput.send_keys(practiceNameEntry)
            time.sleep(2)
            teleBook = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
            lurkss = re.findall('\d+', teleBook)
            self.pAnalyticsOut2.append("\nTelemedicine Appointments Booked for the last 30 days is: " + str(lurkss[2]))#text.insert(INSERT,)

            #CALLS
            practiceAppointments = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
            practiceAppointments.click()
            callsLast30Days = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(4) > div:nth-child(4)')
            callsLast30Days.click()
            time.sleep(4)
            search = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
            search.send_keys(practiceNameEntry)#practiceEntry.get()
            callsMade = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
            lurk = re.findall('\d+', callsMade)
            #trs = driver.find_elements_by_css_selector('#DataTables_Table_0 > tbody > tr')#length of trs holds last 30 day calls
            self.pAnalyticsOut2.append("\nCalls made for the last 30 days is: " + str(lurk[2]))
            self.practiceName2.clear()
            self.dialog3 = QtWidgets.QErrorMessage()
            self.dialog3.showMessage('Done') 

        if len(doctorNameEntry) != 0:
            print(' ')
            self.dialog4 = QtWidgets.QErrorMessage()                        
            self.dialog4.showMessage('This feature has been disabled. Switch to Practice Analytics By Date Range and give it a 30 day date range for now.') 
      

    def practiceSearchDateRange(self):
        practiceNameInput = self.practiceName.toPlainText()
        doctorNameInput = self.doctorName.toPlainText()
        pStartDate = self.startDate.toPlainText()
        pEndDate = self.endDate.toPlainText()

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu') 
        urlPracticeLog = 'https://www.marijuanadoctors.com/user/admin/user/practice/index'

        if  len(doctorNameInput) == 0 and len(practiceNameInput) == 0:          
            self.twoInputs = QtWidgets.QErrorMessage()
            self.twoInputs.showMessage('Please Enter Practice Name or First Last Name')

        if len(practiceNameInput) != 0:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            chromedriver = desktop + '/chromedriver'                                                                   
            driver = webdriver.Chrome(chromedriver,chrome_options=options)
            driver.get(urlPracticeLog)
            try:
                popUpRadio = driver.find_element_by_id('is21')
                popUpRadio.click()
                submit = driver.find_element_by_id('submitAgeGate')
                submit.click()
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
            try:
                userName = driver.find_element_by_id('qf_login_full__fields__email')
                userName.send_keys('ray@marijuanadoctors.com')
                pw = driver.find_element_by_id('qf_login_full__fields__password')
                pw.send_keys('Made2win$')
                logIn = driver.find_element_by_id('qf_login_full__submit')
                logIn.click()
                driver.implicitly_wait(5)
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
            driver.get(urlPracticeLog)
            practiceIn = driver.find_element_by_id('gs_practice_name')
            practiceIn.send_keys(practiceNameInput, Keys.ENTER)#practiceEntry.get()
            practiceIn.send_keys(Keys.ENTER)
            practiceIn.send_keys(Keys.ENTER)
            practiceIn.send_keys(Keys.ENTER)            
            time.sleep(1)
            practiceIn.send_keys(Keys.ENTER)
            practiceIn.send_keys(Keys.ENTER)   
            time.sleep(2)       
            try:         
                folderI = driver.find_element_by_css_selector('#icons > li:nth-child(1) > span')
                time.sleep(1)
                folderI.click()
                time.sleep(2)
            except NoSuchElementException as exception:
                self.errorMessage2 = QtWidgets.QErrorMessage()
                self.errorMessage2.showMessage('No One Found With Practice Name: ' + practiceNameInput)
            logInAsUser = driver.find_element_by_css_selector('#node-user_admin_user_practice-edit > div > p:nth-child(7) > a')
            logInAsUser.click()
            pAnalytics = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(3) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-first > a')
            pAnalytics.click()
            startDatesAN = driver.find_element_by_id('date_start')
            startDatesAN.clear()
            startDatesAN.send_keys(pStartDate)
            endDatesAN = driver.find_element_by_id('date_end')            
            endDatesAN.clear()
            endDatesAN.send_keys(pEndDate)
            trafficByDate = driver.find_element_by_css_selector('#change_date > fieldset > div.qf-button-wrapper > button')
            trafficByDate.click()
            time.sleep(2)
            table = driver.find_element_by_id('practices').text.split('\n')
            table = table[1:]
            splitTable = []
            for i in table:
                splitTable.append(i.split(' '))
            self.pAnalyticsOut.append('Analytics from ' + str(pStartDate) + ' - ' + str(pEndDate) + '\nFor: ' + practiceNameInput)
            for i in splitTable:
                if len(i) == 5:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' \nHits: ' + str(i[2]) + ' \nRequested appointments: ' + str(i[3]) + ' \nBooked appointments: ' + str(i[4]) + '\n')
                elif len(i) == 6:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' ' + i[1] + ' \nHits: ' + str(i[3]) + ' \nRequested appointments: ' + str(i[4]) + ' \nBooked appointments: ' + str(i[5]) + '\n')
                elif len(i) == 7:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' ' + i[1] + i[2] + ' \nHits: ' + str(i[4]) + ' \nRequested appointments: ' + str(i[5]) + ' \nBooked appointments: ' + str(i[6]) + '\n')
                else:
                    self.errorMessage2 = QtWidgets.QErrorMessage()
                    self.errorMessage2.showMessage('Error on line 422')            
            driver.quit()
            self.practiceName.clear()
            self.startDate.clear()
            self.endDate.clear()
            self.dialog1 = QtWidgets.QErrorMessage()
            self.dialog1.showMessage('Done')            
            

        if len(doctorNameInput) != 0:
            splitName = doctorNameInput.split(' ')
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            chromedriver = desktop + '/chromedriver'
            driver = webdriver.Chrome(chromedriver,chrome_options=options)
            driver.get(urlPracticeLog)
            try:
                popUpRadio = driver.find_element_by_id('is21')
                popUpRadio.click()
                submit = driver.find_element_by_id('submitAgeGate')
                submit.click()
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
            try:
                userName = driver.find_element_by_id('qf_login_full__fields__email')
                userName.send_keys('ray@marijuanadoctors.com')
                pw = driver.find_element_by_id('qf_login_full__fields__password')
                pw.send_keys('Made2win$')
                logIn = driver.find_element_by_id('qf_login_full__submit')
                logIn.click()
                driver.implicitly_wait(5)
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
            driver.get(urlPracticeLog)
            firstName = driver.find_element_by_id('gs_first_name')
            firstName.send_keys(splitName[0])
            lastName = driver.find_element_by_id('gs_last_name')
            lastName.send_keys(splitName[1])
            lastName.send_keys(Keys.ENTER)
            lastName.send_keys(Keys.ENTER)
            lastName.send_keys(Keys.ENTER)
            time.sleep(1)
            lastName.send_keys(Keys.ENTER)
            lastName.send_keys(Keys.ENTER)
            lastName.send_keys(Keys.ENTER)  
            time.sleep(2)          
            try:         
                folderI = driver.find_element_by_css_selector('#icons > li:nth-child(1) > span')
                time.sleep(2)
            except NoSuchElementException as exception:
                self.errorMessage1 = QtWidgets.QErrorMessage()
                self.errorMessage1.showMessage('No One Found With First and Last Name')
            folderI.click()
            logInAsUser = driver.find_element_by_css_selector('#node-user_admin_user_practice-edit > div > p:nth-child(7) > a')
            logInAsUser.click()
            pAnalytics = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(3) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-first > a')
            pAnalytics.click()
            startDatesAN = driver.find_element_by_id('date_start')
            startDatesAN.clear()
            startDatesAN.send_keys(pStartDate)
            endDatesAN = driver.find_element_by_id('date_end')            
            endDatesAN.clear()
            endDatesAN.send_keys(pEndDate)
            trafficByDate = driver.find_element_by_css_selector('#change_date > fieldset > div.qf-button-wrapper > button')
            trafficByDate.click()
            time.sleep(2)
            table = driver.find_element_by_id('practices').text.split('\n')
            table = table[1:]
            splitTable = []
            for i in table:
                splitTable.append(i.split(' '))
            self.pAnalyticsOut.append('Analytics from ' + str(pStartDate) + ' - ' + str(pEndDate) + '\nFor: ' + doctorNameInput)
            for i in splitTable:
                if len(i) == 5:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' \nHits: ' + str(i[2]) + ' \nRequested appointments: ' + str(i[3]) + ' \nBooked appointments: ' + str(i[4]) + '\n')
                elif len(i) == 6:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' ' + i[1] + ' \nHits: ' + str(i[3]) + ' \nRequested appointments: ' + str(i[4]) + ' \nBooked appointments: ' + str(i[5]) + '\n')
                elif len(i) == 7:
                    self.pAnalyticsOut.append('\nPractice Location: ' + i[0] + ' ' + i[1] + i[2] + ' \nHits: ' + str(i[4]) + ' \nRequested appointments: ' + str(i[5]) + ' \nBooked appointments: ' + str(i[6]) + '\n')
                else:
                    self.errorMessage2 = QtWidgets.QErrorMessage()
                    self.errorMessage2.showMessage('Error on line 422')            
            driver.quit()
            self.doctorName.clear()
            self.startDate.clear()
            self.endDate.clear()
            self.dialog2 = QtWidgets.QErrorMessage()                        
            self.dialog2.showMessage('Done')            

            

        if  len(doctorNameInput) != 0 and len(practiceNameInput) != 0:          
            self.twoInputs = QtWidgets.QErrorMessage()
            self.twoInputs.showMessage('Please Enter Practice Name or First Last Name')

        
        print(' ')

    def searchStateDateRange(self):
        print(' ')

    def searchState30Days(self):
        stateInput = self.state.toPlainText()

        if len(stateInput) == 0:
            self.dialog5 = QtWidgets.QErrorMessage()                        
            self.dialog5.showMessage('Enter State Abbreviation')

        if len(stateInput) != 0:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

            url = 'https://www.marijuanadoctors.com/super/analytics.php' 
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            chromedriver = desktop + '/chromedriver'
            #Initate driver
            driver = webdriver.Chrome(chromedriver, chrome_options=options)
            #Get the URL
            driver.get(url) 
            try:
                popUpRadio = driver.find_element_by_id('is21')
                popUpRadio.click()
                submit = driver.find_element_by_id('submitAgeGate')
                submit.click()
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")
                
            try:
                userName = driver.find_element_by_id('qf_login_full__fields__email')
                userName.send_keys('ray@marijuanadoctors.com')
                pw = driver.find_element_by_id('qf_login_full__fields__password')
                pw.send_keys('Made2win$')
                logIn = driver.find_element_by_id('qf_login_full__submit')
                logIn.click()
                driver.implicitly_wait(5)
            except NoSuchElementException as exception:
                print("Element not found and test failed")
                print("Program will now continue..")

            driver.get(url)
            time.sleep(5)
            currentURL = driver.current_url
            print(currentURL)
            start_date = datetime.datetime.now() + datetime.timedelta(-30)
            now = datetime.datetime.now()
            newURL = currentURL + '?date_start=' + str(start_date.year) + '-' + str('{:02d}'.format(start_date.month)) + '-' + str('{:02d}'.format(start_date.day)) + '&date_end=' + str(now.year) + '-' + str('{:02d}'.format(now.month)) + '-' + str('{:02d}'.format(now.day)) + '&state_id=' + stateInput.upper()
            print(newURL)
            driver.get(newURL)
            time.sleep(3)
            show = driver.find_element_by_css_selector('#map_search_city_count_length > label > select')
            show.click()
            hundreds = driver.find_element_by_css_selector('#map_search_city_count_length > label > select > option:nth-child(4)')
            hundreds.click()
            time.sleep(5)
            stateRows = driver.find_elements_by_css_selector('#map_search_city_count > tbody > tr')            
            splitStateRows = []
            for i in stateRows:
                splitStateRows.append(i.text.split(' '))

            sumHits = []
            for i in stateRows:
                digits = re.findall(r'\d+', i.text)
                sumHits.append(digits)
            flat_list = [item for sublist in sumHits for item in sublist]
            totalHitState = sum(int(x) for x in flat_list)    
            
            self.stateHitsOut.append('Total Hits For State: ' + stateInput.upper() + ' ' + str(totalHitState))   
            for i in splitStateRows:
                sumHits = []
                if len(i) == 4:
                    self.stateHitsOut.append('\nCity: ' + i[0] + ' ' + i[1] + '      ' +  'State: ' + i[2] + '      ' + 'Hits: ' + str(i[3]))
                if len(i) == 3:
                    sumHits.append(i[2])
                    self.stateHitsOut.append('\nCity: ' + i[0] + '      ' +  'State: ' + i[1] + '      ' + 'Hits: ' + str(i[2]))
                if len(i) == 5:
                    sumHits.append(i[4])
                    self.stateHitsOut.append('\nCity: ' + i[0] + ' ' + i[1] + ' ' + i[2] + '      ' +  'State: ' + i[3] + '      ' + 'Hits: ' + str(i[4]))     
            driver.quit()        
            #self.stateHitsOut.append(stateInput)
            self.state.clear()
            self.dialog = QtWidgets.QErrorMessage()
            self.dialog.showMessage('Done')

    #Frame Navigation
    def pageOne(self):
        self.stackedWidget.setCurrentIndex(0)

    def pageTwo(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def pageThree(self):
        self.stackedWidget.setCurrentIndex(2)

    def pageFour(self):
        self.stackedWidget.setCurrentIndex(3)

    

    def retranslateUi(self, MarijuanaDoctorsV3):
        _translate = QtCore.QCoreApplication.translate
        MarijuanaDoctorsV3.setWindowTitle(_translate("MarijuanaDoctorsV3", "MainWindow"))
        self.label.setText(_translate("MarijuanaDoctorsV3", "<html><head/><body><p><img src=\":/logo/imageedit_1_4221648134.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MarijuanaDoctorsV3", "Practice Analytics"))
        self.radioButton.setText(_translate("MarijuanaDoctorsV3", "Practice Name"))
        self.radioButton_2.setText(_translate("MarijuanaDoctorsV3", "First Last Name"))
        self.label_4.setText(_translate("MarijuanaDoctorsV3", "Choose search type:"))
        self.searchPractice.setText(_translate("MarijuanaDoctorsV3", "Search"))
        self.label_5.setText(_translate("MarijuanaDoctorsV3", "Start Date"))
        self.label_6.setText(_translate("MarijuanaDoctorsV3", "End Date"))
        self.label_9.setText(_translate("MarijuanaDoctorsV3", "By Date Range"))
        self.pushButton_2.setText(_translate("MarijuanaDoctorsV3", "Next Page"))
        self.label_8.setText(_translate("MarijuanaDoctorsV3", "<html><head/><body><p><img src=\":/logo/imageedit_1_4221648134.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MarijuanaDoctorsV3", "Practice Analytics"))
        self.label_11.setText(_translate("MarijuanaDoctorsV3", "Last 30 Days"))
        self.radioButton_3.setText(_translate("MarijuanaDoctorsV3", "Practice Name"))
        self.radioButton_4.setText(_translate("MarijuanaDoctorsV3", "First Last Name"))
        self.searchPractice2.setText(_translate("MarijuanaDoctorsV3", "Search"))
        self.pushButton_3.setText(_translate("MarijuanaDoctorsV3", "Next Page"))
        self.label_12.setText(_translate("MarijuanaDoctorsV3", "<html><head/><body><p><img src=\":/logo/imageedit_1_4221648134.png\"/></p></body></html>"))
        self.label_13.setText(_translate("MarijuanaDoctorsV3", "State Hits"))
        self.label_14.setText(_translate("MarijuanaDoctorsV3", "State Abbreviation"))
        self.label_15.setText(_translate("MarijuanaDoctorsV3", "Last 30 Days"))
        self.searchState.setText(_translate("MarijuanaDoctorsV3", "Search"))
        self.pushButton_4.setText(_translate("MarijuanaDoctorsV3", "Next Page"))
        self.clearButton.setText(_translate("MarijuanaDoctorsV3", "Clear"))
        self.clearButton1.setText(_translate("MarijuanaDoctorsV3", "Clear"))
        self.clearButton2.setText(_translate("MarijuanaDoctorsV3", "Clear"))
        self.label_16.setText(_translate("MarijuanaDoctorsV3", "State Hits"))
        self.label_17.setText(_translate("MarijuanaDoctorsV3", "<html><head/><body><p><img src=\":/logo/imageedit_1_4221648134.png\"/></p></body></html>"))
        self.label_18.setText(_translate("MarijuanaDoctorsV3", " By Date Range"))
        self.label_19.setText(_translate("MarijuanaDoctorsV3", "Start Date"))
        self.startDateState.setPlaceholderText(_translate("MarijuanaDoctorsV3", "yyyy-mm-dd"))
        self.label_20.setText(_translate("MarijuanaDoctorsV3", "  End Date"))
        self.endDateState.setPlaceholderText(_translate("MarijuanaDoctorsV3", "yyyy-mm-dd"))
        self.searchState2.setText(_translate("MarijuanaDoctorsV3", "Search"))
        self.pushButton.setText(_translate("MarijuanaDoctorsV3", "Next Page"))
        self.menuMenu.setTitle(_translate("MarijuanaDoctorsV3", "Menu"))
        self.actionPractice_Date_Range.setText(_translate("MarijuanaDoctorsV3", "Practice Date Range"))
        self.actionPractice_Last_30_Days.setText(_translate("MarijuanaDoctorsV3", "Practice Last 30 Days"))
        self.actionState_Hits_Last_30_Days.setText(_translate("MarijuanaDoctorsV3", "State Hits Last 30 Days"))
        self.actionState_Hits_Date_Range.setText(_translate("MarijuanaDoctorsV3", "State Hits Date Range"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarijuanaDoctorsV3 = QtWidgets.QMainWindow()
    ui = Ui_MarijuanaDoctorsV3()
    ui.setupUi(MarijuanaDoctorsV3)
    MarijuanaDoctorsV3.show()
    sys.exit(app.exec_())

