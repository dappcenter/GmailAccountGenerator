from selenium import webdriver
import time
import os
import logging
FirstN_input = "MadeBY"
SeconN_input = "LXQM"
UserName = input(str("Username: "))
PassWord = input(str("Password: "))
PassConf = (PassWord)
PhNum = input(str("Phone Number: "))
AllInfo = ("Email: " + UserName + "@gmail.com" "\nPassword: " + PassWord + "\nPhone Number: " + PhNum + "\n\tMade By Lxqm")
SaveInfo = input(str("File Name To Save Info To: "))
logging.basicConfig(filename=SaveInfo + ".log", filemode='w', format=AllInfo)
logging.warning('This will get logged to a file')
print("Loading...")
time.sleep(2)
print("Saving Credentials To " + SaveInfo)
time.sleep(2)
print("Starting...")
time.sleep(1)
url = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"
path = ("./chromedriver")
driver = webdriver.Chrome(path)
driver.get(url)
driver.find_element_by_name("firstName").send_keys(FirstN_input)
driver.find_element_by_name("lastName").send_keys(SeconN_input)
driver.find_element_by_name("Username").send_keys(UserName)
driver.find_element_by_name("Passwd").send_keys(PassWord)
driver.find_element_by_name("ConfirmPasswd").send_keys(PassConf)
driver.find_element_by_class_name("CwaK9").click() 
time.sleep(1)
driver.find_element_by_id("phoneNumberId").send_keys(PhNum)
driver.find_element_by_class_name("CwaK9").click()







    
