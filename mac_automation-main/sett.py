from genericpath import exists
from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver
import time
from turtle import delay

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class Setup:
    def __init__(self, mac_ip="0.0.0.0", port=4723, caps=None):
        if caps is None:
            caps = {'appium:automationName': 'Mac2', 'platformName': 'mac',
                    'appium:bundleId': 'com.bjitgroup.sn.ptsubtitle', 'appium:noReset': True,
                    'appium:connectHardwareKeyboard': True, "appium:newCommandTimeout": 2000}
        self.driver = webdriver.Remote("http://{}:{}".format(mac_ip, port), caps)
        if self.driver is not None:
            print("Do not use Mac Pair while executing the script")
            #self.quit()
        #self.driver = webdriver.Remote("http://{}:{}".format(mac_ip, port), caps)

    