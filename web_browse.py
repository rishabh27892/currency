# !/usr/bin/env python
# Author: Rishabh Chauhan
# Currency Capital
# Test case count: 1

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

xpaths = {'firstpagecontent': '//*[@id="banner_video"]/div/div[1]/div[1]/h2/span',
          }


class web_browse_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.get(ui_url)

    def test_01_url_open(self):
        try:
            print ("opening the browser and the site")
            # ui_content
            ui_element=driver.find_element_by_xpath(xpaths['firstpagecontent'])
            # get the weather data
            page_data=ui_element.text
            # assert response
            self.assertTrue("Start selling more by optimizing" in page_data)
            driver.execute_script("document.body.style.zoom='50 %'")
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

def run_web_browse_test(webdriver, ip):
    global driver
    driver = webdriver
    global ui_url
    ui_url = ip
    suite = unittest.TestLoader().loadTestsFromTestCase(web_browse_test)
    xmlrunner.XMLTestRunner(output="results", verbosity=2).run(suite)
