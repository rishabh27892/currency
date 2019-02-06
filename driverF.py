# /usr/bin/env python
# Author: Rishabh Chauhan
# Driver script for Firefox browser

from os import path
from selenium import webdriver
# from example import run_creat_nameofthetest

def webDriver():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver
