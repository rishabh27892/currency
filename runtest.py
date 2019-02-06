# !/usr/bin/env python
# Author: Rishabh Chauhan
# Currency website
# Test case count: 1

import sys
import getopt
from shutil import copyfile
from subprocess import call
from os import path
from web_browse import run_web_browse_test
from web_close import run_web_close_test


sys.stdout.flush()

ip = "https://currencypay.com/home/"

from driverF import webDriver
print("Running Firefox Driver")
runDriver = webDriver()

# running tests
run_web_browse_test(runDriver, ip)
run_web_close_test(runDriver)

# cleaning up files
if path.exists('driverF.pyc'):
    call(["rm", "driverF.pyc"])

if path.exists('function.pyc'):
    call(["rm", "function.pyc"])

if path.exists('web_browse.pyc'):
    call(["rm", "web_browse.pyc"])

if path.exists('source.pyc'):
    call(["rm", "source.pyc"])

if path.exists('web_close.pyc'):
    call(["rm", "web_close.pyc"])

if path.exists('geckodriver.log'):
    call(["rm", "geckodriver.log"])

if path.exists('__pycache__'):
    call(["rm", "-r", "__pycache__"])

if path.isdir('.cache'):
    call(["rm", "-r", ".cache"])
