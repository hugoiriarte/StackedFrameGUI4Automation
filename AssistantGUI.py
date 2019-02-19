#Imports
import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from tkinter import messagebox
import os
import csv
import re
from tkinter import *
import tkinter.scrolledtext as tkscrolled

#Main Class
class MdAppv2(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.title('MD BackEnd Scraper V2 Powered By Python')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Dictionary holding app frames
        self.frames = {}
        #Append franes
        for F in (StartPage, Analytics, Billing):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #Show StartPage when app opens
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#Start Page
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to MD.com V2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to Practice Analytics",
                            command=lambda: controller.show_frame("Analytics"))
        button2 = tk.Button(self, text="Go to Billing",
                            command=lambda: controller.show_frame("Billing"))
        button1.pack()
        button2.pack()

#Analytics Page
#Give extra time for elements to load
class Analytics(tk.Frame):
    def __init__(self, parent, controller):
        #Clear text function
        def clearText():
            text.delete('1.0', END)

        #Retrieve practice analytics function
        def practiceAnalytics():
            if len(practiceEntry.get()) == 0:
                messagebox.showerror(title='Error 01', message='Please enter a practice name')
            else:
                #URL
                url = 'https://www.marijuanadoctors.com/user/login'
                #Initate driver
                chromedriver = 'C:/Users/Owner/Desktop/chromedriver'
                driver = webdriver.Chrome(chromedriver)
                #Get the URL
                driver.get(url)
                #Popup message exception handler
                try:
                    popUpRadio = driver.find_element_by_id('is21')
                    popUpRadio.click()
                    submit = driver.find_element_by_id('submitAgeGate')
                    submit.click()
                except NoSuchElementException as exception:
                    print("")
                #Login exception handler
                # Inputs are empty for security    
                try:
                    userName = driver.find_element_by_id('qf_login_full__fields__email')
                    userName.send_keys('')
                    pw = driver.find_element_by_id('qf_login_full__fields__password')
                    pw.send_keys('')
                    logIn = driver.find_element_by_id('qf_login_full__submit')
                    logIn.click()
                    driver.implicitly_wait(5)
                except NoSuchElementException as exception:
                    print("")
                try:
                    mobileSuperAd = driver.find_element_by_css_selector('body > header > div.tab_header > div > ul > li:nth-child(1) > a')
                    mobileSuperAd.click()
                    time.sleep(5)
                except NoSuchElementException as exception:
                    print("Element not found and test failed")
                
                #Practice hits for the last 30 days
                analytics = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(1) > a')
                analytics.click()
                #Give program sleep time so elements fully load
                #Back end is very slow
                time.sleep(3)
                searchIn = driver.find_element_by_css_selector('#practice_view_count_filter > label > input')
                #Send user input keys to search field
                searchIn.send_keys(practiceEntry.get())
                hundoHits = driver.find_element_by_css_selector('#practice_view_count_length > label > select > option:nth-child(4)')
                hundoHits.click
                try:
                    aHits = driver.find_elements_by_css_selector('#practice_view_count > tbody > tr > td.sorting_1')
                except NoSuchElementException as exception:
                    print('Error')
                hits = []
                #Extract text and convert to integers
                for i in aHits:
                    hits.append(int(i.text))
                #Add hits variable that will equal Total Hits for practice
                totalHits = sum(hits)
                #Text output
                text.insert(INSERT, "Hits for the last 30 days is: " + str(totalHits))#text.insert(INSERT,)

                #Last 30 days APPT REQUEST
                clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
                clicks.click()
                time.sleep(3)
                appointmentRequestQuery = driver.find_elements_by_css_selector('#appointment_requests > div')
                appointmentRequestQuery[3].click()
                time.sleep(1)
                searchToday = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
                #Send user input to search field
                searchToday.send_keys(practiceEntry.get())
                time.sleep(1)
                apptReq = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
                #Finds digits within apptReq web element
                lurksss = re.findall('\d+', apptReq)
                #Text output
                #lurksss[2] hold the total amount of appointment request without having to count tr's
                text.insert(INSERT,"\n" + "\nAppointment requests for the last 30 days is: " + str(lurksss[2]))
                
                #Last 30 Dats Appt Booked        
                clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
                clicks.click()
                apptBooked = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(2) > div:nth-child(4)')
                apptBooked.click()
                apptBookedInput = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
                #Send user input keys
                apptBookedInput.send_keys(practiceEntry.get())
                apptBook = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
                #Find digits within apptbook web element
                lurks = re.findall('\d+', apptBook)
                #Text output
                #lurksss[2] hold the total amount of appointment request without having to count tr's                    
                text.insert(INSERT, "\n" + "\nAppointments Booked for the last 30 days is: " + str(lurks[2]))#text.insert(INSERT,)
                
                #Last 30 Days TeleMedicine Appointments
                clicks = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
                clicks.click()
                tele = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(3) > div:nth-child(4)')
                tele.click()
                teleInput = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
                #Send user input keys
                teleInput.send_keys(practiceEntry.get())
                time.sleep(2)
                teleBook = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
                #Find digits within apptbook web element
                lurkss = re.findall('\d+', teleBook)
                #Text output
                #lurksss[2] hold the total amount of appointment request without having to count tr's                     
                text.insert(INSERT, "\n" + "\nTelemedicine Appointments Booked for the last 30 days is: " + str(lurkss[2]))#text.insert(INSERT,)

                #CALLS
                practiceAppointments = driver.find_element_by_css_selector('body > div.page-container > div.page-sidebar-wrapper > div > ul > li:nth-child(3)')
                practiceAppointments.click()
                callsLast30Days = driver.find_element_by_css_selector('body > div.page-container > div.page-content-wrapper > div > div:nth-child(4) > div:nth-child(4)')
                callsLast30Days.click()
                time.sleep(4)
                search = driver.find_element_by_css_selector('#DataTables_Table_0_filter > label > input')
                #Send users input keys
                search.send_keys(practiceEntry.get())
                callsMade = driver.find_element_by_css_selector('#DataTables_Table_0_info').text
                #Find digits within callsMade web element
                lurk = re.findall('\d+', callsMade)
                #Text output
                #lurksss[2] hold the total amount of appointment request without having to count tr's                        
                text.insert(INSERT, "\n" + "\nCalls made for the last 30 days is: " + str(lurk[2]))#text.insert(INSERT,)

                #Next step sign in as practice to get even more analytics that are only given within doctor profiles
                driver.get('https://www.marijuanadoctors.com/user/admin/user/practice/index')
                practiceIn = driver.find_element_by_id('gs_practice_name')
                #Send user keys to input box
                practiceIn.send_keys(practiceEntry.get(), Keys.ENTER)
                #There was a bug that did not allow the enter key to send
                #A work around is hitting enter a few times
                #Letting time to sleep
                #And hitting enter again, I added extra enter keys just to make sure 
                practiceIn.send_keys(Keys.ENTER)
                practiceIn.send_keys(Keys.ENTER)            
                time.sleep(1)
                practiceIn.send_keys(Keys.ENTER)
                practiceIn.send_keys(Keys.ENTER)
                time.sleep(2)
                #If no elements were found means that practice name was entered incorrectly
                try:         
                    folderI = driver.find_element_by_css_selector('#icons > li:nth-child(1) > span')
                    time.sleep(2)
                except NoSuchElementException as exception:
                    #Send message box with error explaning what went wrong
                    messagebox.showerror('Error', 'No practice was found. Data currently being displayed could be wrong. Check spelling close pop-up chrome window and try again.')                
                #Program wont continue if practice name was entered incorrectly
                #Program will not break and will allow user to try again
                #Else program will continue to log in as practice to get life time analytics
                folderI.click()
                logInAsUser = driver.find_element_by_css_selector('#node-user_admin_user_practice-edit > div > p:nth-child(7) > a')
                logInAsUser.click()
                subMan = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-last.qi-menu-parent')    
                subMan.click()
                bHistory = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-last.qi-menu-parent > ul > li.qi-menu-item.qi-menu-item-level-3.qi-menu-first > a')
                bHistory.click()
                #date holds the day the practice signed up
                date = driver.find_element_by_css_selector('#node-user_practice_billing-index > div > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1)').text
                #Navigate to practice analytics
                pAnalytics = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(3) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-first > a')
                pAnalytics.click()
                startDate = driver.find_element_by_id('date_start')
                #Clear out start date range
                startDate.clear()
                #Replace start date with date variable which holds the day practice signed up
                startDate.send_keys(date)
                trafficByDate = driver.find_element_by_css_selector('#change_date > fieldset > div.qf-button-wrapper > button')
                #Click to select to check analytics within date range
                trafficByDate.click()
                #Give some time to sleep for elements to load
                time.sleep(3)
                #Split table by next lines
                table = driver.find_element_by_id('practices').text.split('\n')
                #Remove first 
                table = table[1:]
                splitTable = []
                #Split the table even more by space
                for i in table:
                    splitTable.append(i.split(' '))
                #Text output to clarify what practice and what start date
                text.insert(INSERT, '\n' + '\nLife Time Analytics for: ' + practiceEntry.get() + '\nPractice start date: ' + date)
                #Depending on the length of the splitTable data indices will differ
                for i in splitTable:
                    if len(i) == 5:
                        text.insert(INSERT, "\n" + '\nPractice Location: ' + i[0] + ' \nLife time hits: ' + str(i[2]) + ' \nLife time requested appointments: ' + str(i[3]) + ' \nLife time booked appointments: ' + str(i[4]) + '\n')
                    elif len(i) == 6:
                        text.insert(INSERT, "\n" + '\nPractice Location: ' + i[0] + ' ' + i[1] + ' \nLife time hits: ' + str(i[3]) + ' \nLife time requested appointments: ' + str(i[4]) + ' \nLife time booked appointments: ' + str(i[5]) + '\n')
                    elif len(i) == 7:
                        text.insert(INSERT, "\n" + '\nPractice Location: ' + i[0] + ' ' + i[1] + i[2] + ' \nLife time hits: ' + str(i[4]) + ' \nLife time requested appointments: ' + str(i[5]) + ' \nLife time booked appointments: ' + str(i[6]) + '\n')
                    else:
                        text.insert(INSERT, '\nError please contact Hugo.')
                
                #Find patient cost for every practice location if more than 1 location
                profileManagers = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-first.qi-menu-parent > span')
                profileManagers.click()
                viewListings = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-first.qi-menu-parent > ul > li.qi-menu-item.qi-menu-item-level-3.qi-menu-last > a > span')
                viewListings.click()
                manageListings = driver.find_elements_by_css_selector('#node-user_practice_profile-index > div > div.mobile-table-wrapper > div > table > tbody > tr > td:nth-child(3) > a')
                #manageListings holds how many listings the practice has
                listingLinks = []
                for i in manageListings:
                    #listingLinks find the url to each location
                    listingLinks.append(i.get_attribute('href'))
                #Loop through location and find patient cost and if they have a trackable phone number
                for i in listingLinks:
                    driver.get(i)
                    pName = driver.find_element_by_id('qf_practice__info1__practice_name').get_attribute('value')
                    bh = driver.find_element_by_css_selector('#center > ul > li:nth-child(2) > a')
                    bh.click()
                    pCost = driver.find_element_by_id('qf_practice__billing__cost_new').get_attribute('value')
                    cInfo = driver.find_element_by_css_selector('#center > ul > li:nth-child(3) > a')
                    cInfo.click()
                    pTrackable = driver.find_element_by_id('qf_address__address__phone_trackable').get_attribute('value')
                    #Output result
                    text.insert(INSERT, '\nPractice Location: ' + pName + '\nPatient Cost: ' + str(pCost) + '\nPhone Trackable: ' + str(pTrackable) + '\n')
                #Close driver              
                driver.quit()

        #Setting up frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Practice Analytics", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back to home page",
                           command=lambda: controller.show_frame("StartPage"))
        label = Label(self,text='Enter Practice Name')
        practiceEntry = Entry(self,width=40)
        searchButton = tk.Button(self,text='Search', command=practiceAnalytics)
        clearButton = Button(text="Clear Practice Analytics", command = clearText)
        CheckVar1 = IntVar()
        c1 = Checkbutton(text='Hits', variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,width=20)
        c1.pack()
        text = tk.Text(self, wrap='word')
        vsb = tk.Scrollbar(self, orient='vertical')
        text.configure(yscrollcommand=vsb.set)
        vsb.configure(command=text.yview)
        label.pack()
        practiceEntry.pack()  
        clearButton.pack(side=LEFT)   
        searchButton.pack()        
        vsb.pack()
        text.pack()
        button.pack()

#Billing Frame
class Billing(tk.Frame):

    def __init__(self, parent, controller):
        #Clean text box function
        def clearText():
            text2.delete('1.0', END)
        
        #Practice Billing function
        def searchPractice():
            #Message box if no practice was entered
            if len(practiceEntries.get()) == 0:
                messagebox.showerror('Error', 'No practice was entered. Enter a practice and try again')
            else:
                #URL
                url = 'https://www.marijuanadoctors.com/user/login'

                #Initate driver
                chromedriver = 'C:/Users/Owner/Desktop/chromedriver'
                driver = webdriver.Chrome(chromedriver)
                #Get the URL
                driver.get(url)
                #Exception handler for popup
                try:
                    popUpRadio = driver.find_element_by_id('is21')
                    popUpRadio.click()
                    submit = driver.find_element_by_id('submitAgeGate')
                    submit.click()
                except NoSuchElementException as exception:
                    print("Element not found and test failed")
                    print("Program will now continue..")
                #Log in to back end 
                #Keys Empty for security    
                try:
                    userName = driver.find_element_by_id('qf_login_full__fields__email')
                    userName.send_keys('')
                    pw = driver.find_element_by_id('qf_login_full__fields__password')
                    pw.send_keys('')
                    logIn = driver.find_element_by_id('qf_login_full__submit')
                    logIn.click()
                    driver.implicitly_wait(5)
                except NoSuchElementException as exception:
                    print("Element not found and test failed")
                    print("Program will now continue..")

                driver.get('https://www.marijuanadoctors.com/user/admin/user/practice/index')                
                practiceIn = driver.find_element_by_id('gs_practice_name')
                #Send user input keys
                practiceIn.send_keys(practiceEntries.get(), Keys.ENTER)
                practiceIn.send_keys(Keys.ENTER)
                #There was a bug that did not allow the enter key to send
                #A work around is hitting enter a few times
                #Letting time to sleep
                #And hitting enter again, I added extra enter keys just to make sure                 
                practiceIn.send_keys(Keys.ENTER)
                time.sleep(1)
                practiceIn.send_keys(Keys.ENTER)
                practiceIn.send_keys(Keys.ENTER)
                time.sleep(2)
                #Exception handler if practice name was entered incorrectly
                try:
                    folderI = driver.find_element_by_css_selector('#icons > li:nth-child(1) > span')
                    time.sleep(2)
                except NoSuchElementException as exception:
                    messagebox.showerror('Error', 'No practice was found. Check spelling, close pop-up chrome window and try again')
                #Program wont continue if practice name was entered incorrectly
                #Program will not break and will allow user to try again
                #Else program will continue to log in as practice to get life time analytics                    
                folderI.click()
                logInAsUser = driver.find_element_by_css_selector('#node-user_admin_user_practice-edit > div > p:nth-child(7) > a')
                logInAsUser.click()
                #Navigate to transaction history
                transactionH = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-last.qi-menu-parent > span')
                transactionH.click()   
                transH = driver.find_element_by_css_selector('#block-menu_practice > div > ul > li:nth-child(2) > ul > li.qi-menu-item.qi-menu-item-level-2.qi-menu-last.qi-menu-parent > ul > li:nth-child(3) > a > span')
                transH.click()
                """This section holds practice billing history"""
                monthCheck = driver.find_elements_by_css_selector('#node-user_practice_billing-transactions > div > div.mobile-table-wrapper > table > tbody > tr')
                monthChecker = []
                #Delete every other row
                del monthCheck[1::2]
                #Extract text from web elements
                for i in monthCheck:
                    monthChecker.append(i.text)
                splitMonth = []
                #Split the data by spaces
                for i in monthChecker:
                    splitMonth.append(i.split(' '))
                #Replace any forward slash with empty space
                for i in splitMonth:
                    i[1] = i[1].replace('/', ' ')

                """Formula to check for requested date range"""
                #Output Variables
                m = []#OUTPUT REQUESTED for first date range
                n = []#OUTPUT REQUESTED for second date range  
                #Variables holding user input        
                a = monthDate.get()
                b = yearDate.get()
                c = secondMonthDate.get()
                d = secondYearDate.get()
                #Check to see if given dates live within data
                for i in splitMonth:
                    if a in i[1] and b in i[1]:
                        #If dates are found append to output variables
                        m.append(i)
                for i in splitMonth:
                    if c in i[1] and d in i[1]:
                        #If dates are found append to output variables
                        n.append(i)
                #If no dates were found throw error message
                if len(m) == 0:
                    messagebox.showerror('Error', 'No dates were found for first date range')
                else:
                    #Text output for billing
                    for i in m:
                        text2.insert(INSERT, '\n' + str(i) + '\n')
                        for x in i:
                            if '$' in x:
                                text2.insert(INSERT,'\n' + str(x))  
                #Second date range error message
                if len(n) == 0:
                    messagebox.showerror('Error', 'No dates were found for second date range')
                #Output second date requests
                else:           
                    for i in n:
                        text2.insert(INSERT, '\n' + str(i) + '\n')
                        for x in i:
                            if '$' in x:
                                text2.insert(INSERT,'\n' + str(x))
                #Close driver
                driver.quit()                                                       

        #Setup billing frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        searchBt = Button(text='Search Billing', command=searchPractice)
        clearButton = Button(text='Clear Billing', command=clearText)
        clearButton.pack(side=RIGHT)
        searchBt.pack(side=RIGHT)
        label = tk.Label(self, text="Billing", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        explainLabel = tk.Label(self,text='Enter a Practice you wish to check billing history. If no dates are entered it will return lifetime.')
        explainLabel.pack(side='top', fill='x', pady=10)        
        button = tk.Button(self, text="Go back to home page",
                           command=lambda: controller.show_frame("StartPage"))
        practiceLabel = Label(self, text='Please Enter Practice')
        practiceEntries = Entry(self,width=40)

        monthLabel = Label(self,text='Start Month')
        monthDate = Entry(self,width=10)
        yearLabel = Label(self,text='Start Year')
        yearDate = Entry(self,width=10)
        secondMonthLabel = Label(self,text='End Month')
        secondMonthDate = Entry(self, width=10)
        secondYearLabel = Label(self,text='End Year')
        secondYearDate = Entry(self,width=10)
        text2 = Text(self,wrap='word')
        vsb2 = tk.Scrollbar(self, orient='vertical')
        text2.configure(yscrollcommand=vsb2.set)
        vsb2.configure(command=text2.yview)
        practiceLabel.pack()
        practiceEntries.pack()
        monthLabel.pack()
        monthDate.pack()
        yearLabel.pack()
        yearDate.pack()
        secondMonthLabel.pack()
        secondMonthDate.pack()
        secondYearLabel.pack()
        secondYearDate.pack()        
        #lastDate.pack()
        vsb2.pack()
        text2.pack()
        button.pack()

#Execution
if __name__ == "__main__":
    app = MdAppv2()
    app.mainloop()