

from source import *
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

    #method to test if an element is present
def is_element_present(driver, self, how, what):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try: driver.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

# screenshot function
def screenshot(driver, self):
    test_method_name = self._testMethodName
    time.sleep(1)
    text_path = os.path.dirname(os.path.realpath(__file__))
    filename = str(__file__)
    filename = filename[:-3]
    final_file = filename.replace(text_path + "/", '')
    print ("Taking screenshot for " + final_file + "-" + test_method_name)
    driver.save_screenshot(cwd + "/screenshot/"  + "screenshot-" + final_file + "-" + test_method_name + ".png")

