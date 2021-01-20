# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import time
import hashlib
from Credentials import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


cred = Credentials()
user_login = cred.get_login()
user_password =cred.get_password()

print(user_login)

browser = webdriver.Chrome(executable_path="//10.12.100.48/HomeEtu/etudiants/vbrother/Desktop/BOTS/chromedriver_win32/chromedriver")
"""browser.get("https://cas.upf.pf/login?service=https%3A%2F%2Fent.upf.pf%2Findex.php%3Fauth")

username = browser.find_element_by_id("username").send_keys(user_login)
password = browser.find_element_by_id("password").send_keys(user_password + Keys.ENTER)
"""
browser.execute_script('''window.open("http://google.com","_blank");''')
browser.switch_to.window(browser.window_handles[1])

#
#   PROBLEM HERE W/ ALERT AND TAB FOCUS
#

time.sleep(3)
alert = browser.switch_to.alert
time.sleep(2)
alert.send_keys(user_login + Keys.TAB)
alert.send_keys(user_password + Keys.ENTER)


