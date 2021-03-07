from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import smtplib
import os
from time import time, sleep
from datetime import datetime
from termcolor import colored
import csv
import numpy as np

featureNames = np.array([])
importData = np.empty(shape = (1,5))

with open ("data.csv") as file:

        reader = csv.reader(file, delimiter = ',')
        featureNames = next(reader)

        for row in reader:
            importData = np.vstack([importData, row])

        importData = np.delete(importData, (0), axis=0)
        importData = np.array(importData)

sender_email = importData[0,0]
receiver_emails = importData[:,1]
cred = importData[0,2]
url = importData[0,3]
xPathSizeButton = importData[0,4]
xPathProductName = '//*[@id="pdp_product_title"]'

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--window-size=1920,1080')
options.add_argument('--headless')
#options.add_argument('--disable-gpu')

windowClosedErrorMessage_01 = "Unable to evaluate script: no such window: target window already closed\nfrom unknown error: web view not found\n"
windowClosedErrorMessage_02 = "Unable to evaluate script: disconnected: not connected to DevTools\n"


def getButtonStatus(driver, service):

    success = False
    productName = "default"

    try:
        if(service == True):
            driver.get(url)
            xsButtonStatus = driver.find_element_by_xpath(xPathSizeButton).is_enabled()
            productName = driver.find_element_by_xpath(xPathProductName).text

            subject_text = '{} NOW IN STOCK!'.format(productName)
            text = '{} NOW IN STOCK!\n{}'.format(productName, url)
            message = 'Subject: {}\n\n{}'.format(subject_text, text)

        #Change xsButtonStatus to False for testing.
        if(xsButtonStatus == True):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, cred)
            os.system('cls')
            print(colored("Status: In stock.\n", "green"))
            print(colored("Login success.", "green"))

            for email in receiver_emails:
                server.sendmail(sender_email, email, message)

            print(colored("\nEmail(s) sent to:", "magenta"))

            for email in receiver_emails:
                print(colored("    " + email, "yellow"))

            success = True

        else:
            success = False

    except:

        if(service == True):
            print("{} Checker Service now running...".format(productName))
            print("Failed to connect to {}.\nTrying again...".format(url))
        else:
            print(colored("Service cancelled.", "red"))
        
    return success, productName


def startService():

    service = True

    driver = webdriver.Chrome(options=options)

    while(service):

        try:

            if(driver.get_log('driver')[-1]['message'] == windowClosedErrorMessage_01):
                os.system('cls')
                print(colored("Window closed by user. Launching new browser window...", "red"))
                driver = webdriver.Chrome(options=options)

            elif(driver.get_log('driver')[-1]['message'] == windowClosedErrorMessage_02): 
                os.system('cls')
                print(colored("Cannot connect to devtools.", "red"))

                validInput = False

                while(validInput == False):

                    userInput = input("Would you like to restart the service?(Y/N): ")

                    if(userInput == "y" or userInput == "Y"):
                        validInput = True
                        startService()

                    elif(userInput == "n" or userInput == "N"):
                        service = False
                        os.system('cls')
                        print(colored("Shutting down {} Checker Service...".format(productName), "yellow"))
                        break

                    else:
                        print("Invalid input.")

        except Exception as e:
            #Throws list index out of range error.
            pass
        
        success, productName = getButtonStatus(driver, service)

        if(success == True and service == True):
            service = False

        elif(service == True):
            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            concat_string = 'Last checked: ' + dt_string
            sleep(5 - time() % 5)

            os.system('cls')
            print(colored("{} Checker Service now running...".format(productName), "cyan"))
            print(colored("Status: Not in stock.", "red"))
            print(concat_string)

    print(colored("\n{} Checker Service ended successfully.".format(productName), "green"))

startService()