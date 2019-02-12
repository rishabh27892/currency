# !/usr/bin/env python
# Author: Rishabh Chauhan
# Currency Capital
# Test case count: 3

import function
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#error handling/screenshotsave
import sys
import traceback
import os
cwd = str(os.getcwd())

import time
import unittest
import xmlrunner
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

xpaths = {'contactusButton': '/html/body/header/nav/ul/li[3]/a',
          'aboutButton': '/html/body/header/nav/ul/li[2]/a',
          'blogButton': '/html/body/header/nav/ul/li[4]/a',
            # text "Company Information"
          'contactusPage': '/html/body/div[2]/div/section[2]/div[1]/form/fieldset[1]/div[1]'
          }


class nav_page_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        pass

    def test_01_nav_to_contactus(self):
        try:
            print ("opening the browser and the site")
            # click on contact us
            driver.find_element_by_xpath(xpaths['contactusButton']).click()
#            time.sleep(10)
#            ui_element = driver.find_element_by_xpath(xpaths['contactusPage'])
#            page_data=ui_element.text
            # assert response
#            self.assertTrue("Company Information" in page_data)
            #taking screenshot
            function.screenshot(driver, self)
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            #taking screenshot
            function.screenshot(driver, self)
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")


    def test_02_nav_to_about(self):
        try:
            print ("navihgating to about page")
            # click on contact us
            driver.find_element_by_xpath(xpaths['aboutButton']).click()
            #taking screenshot
            function.screenshot(driver, self)
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            #taking screenshot
            function.screenshot(driver, self)
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")

    def test_03_nav_to_blog(self):
        try:
            print ("navihgating to about page")
            # click on contact us
            driver.find_element_by_xpath(xpaths['blogButton']).click()
            #taking screenshot
            function.screenshot(driver, self)
        except Exception:
            exc_info_p = traceback.format_exception(*sys.exc_info())
            #taking screenshot
            function.screenshot(driver, self)
            for i in range(1,len(exc_info_p)):
                print (exc_info_p[i].rstrip())
            self.assertEqual("Just for fail", str(Exception), msg="Test fail: Please check the traceback")




    @classmethod
    def tearDownClass(inst):
        pass

def run_nav_page_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(nav_page_test)
    xmlrunner.XMLTestRunner(output="results", verbosity=2).run(suite)
