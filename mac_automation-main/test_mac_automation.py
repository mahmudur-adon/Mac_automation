#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from genericpath import exists
from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver
import time
from turtle import delay

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from sett import Setup as set

import pytest

from allure_commons.types import AttachmentType


class TestTextEdit:

    exe= set()
    def active_window(self, delay=0, bundle_id='com.apple.TextEdit'):
        """
        Activate the current application -> Since the link jumps or the third-party application is opened in a chain, you need to reactivate the current application at this time, and then continue the automated operation
         :param bundle_id: bundleId is the id of the program to be activated
         :param delay: delay, the unit is seconds, there is no delay by default, solve the problem that some form delays block the main form
         :return:
        """
        time.sleep(delay)
        self.exe.driver.execute_script("macos: activateApp", {"bundleId": bundle_id})
        assert 1==1
        # self.__init__()  
    def is_element_exist(self, value, by=AppiumBy.XPATH, max_time=5, is_elements=False):
        """
        Determines whether the specified element exists within the specified time
         :param by: How to search, the default is XPATH
         :param value: what selector to look for
         :param max_time: the maximum search time in seconds, the default is 5s
         :param is_elements: Whether to find a set of elements, the default is FALSE
         :return:
        """
        times = 10
        interval = max_time/times
        ele = False
        for i in range(times):
            try:
                if i > int(times/2):
                    self.active_window()  # When the new search time exceeds 1/2 of the maximum number of times, the form will be activated to solve the problem that some forms are delayed and the current form cannot be found.
                if is_elements:
                    element = self.exe.driver.find_elements(by=by, value=value)
                else:
                    element = self.exe.driver.find_element(by=by, value=value)
            except Exception as e:
                print("handled exception with love")
                #print("If it is not found, after sleeping for {}s, continue to search; it takes {}s in total".format(interval, interval*(i+1)))
                time.sleep(0.1)
            else:
                ele = element
                break
        else:
            print("Searched the element for {}s, stop searching".format(max_time))
        return ele

    def find_element(self, value, by=AppiumBy.XPATH, max_time=10):
        """
        find element
         :param by: How to search, the default is XPATH
         :param value: what selector to look for
         :param max_time: the maximum search time in seconds, the default is 10s
         :return:
        """
        element = self.is_element_exist(value=value, by=by, max_time=max_time, is_elements=False)
        return element

    def find_elements(self, value, by=AppiumBy.XPATH, max_time=10):
        """
        Find a class of elements
         :param by: How to search, the default is XPATH
         :param value: what selector to look for
         :param max_time: the maximum search time in seconds, the default is 10s
         :return:
        """
        element = self.is_element_exist(value=value, by=by, max_time=max_time, is_elements=True)
        print("element exists")
        return element

    def click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        In order to solve the problem when the element is clicked
         :param element: standard element
         :param radio_x: the offset x of the element, centered by default, 0.5
         :param radio_y: the offset y of the element, centered by default, 0.5
         :return:
        """
        ele_rect = element.rect
        #print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.exe.driver.execute_script('macos: click', {"x": x, "y": y})
        time.sleep(0.3)

    def right_click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        In order to solve the problem of right-clicking an element
         :param element: standard element
         :param radio_x: the offset x of the element, centered by default, 0.5
         :param radio_y: the offset y of the element, centered by default, 0.5
         :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: rightClick', {"x": x, "y": y})
        time.sleep(0.3)

    def double_click_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        In order to solve the method of not double-clicking the element
         :param element: standard element
         :param radio_x: the offset x of the element, centered by default, 0.5
         :param radio_y: the offset y of the element, centered by default, 0.5
         :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: doubleClick', {"x": x, "y": y})
        time.sleep(0.3)

    def hover_element(self, element, radio_x=0.5, radio_y=0.5):
        """
        In order to solve the method without the hover element
         :param element: standard element
         :param radio_x: the offset x of the element, centered by default, 0.5
         :param radio_y: the offset y of the element, centered by default, 0.5
         :return:
        """
        ele_rect = element.rect
        print(ele_rect)
        x, y = ele_rect["x"] + ele_rect["width"] * radio_x, ele_rect["y"] + ele_rect["height"] * radio_y
        self.driver.execute_script('macos: hover', {"x": x, "y": y})
        time.sleep(0.3)

    def send_keys(self, key_list, element=None):
        """
        Send characters globally, if element is not specified, send keyboard characters directly
         :param key_list: The list element of the sent character, if a string is specified, it will be converted internally
         :param element: standard element
         :return:
        """
        if element:
            self.click_element(element)
        if isinstance(key_list, str):
            key_list = list(key_list)
        self.exe.driver.execute_script('macos: keys', {'keys': key_list})

    def clear_keys(self, element=None):
        """
        Use the form of command+a+delete to clear everything in any position
         :param element: standard element
         :return:
        """
        if element:
            self.click_element(element)
        self.exe.driver.execute_script('macos: keys', {'keys': [{
            'key': 'a',
            'modifierFlags': 1 << 4}, 'XCUIKeyboardKeyDelete']})

    def test_quit_window(self, element=None):
        """
        Use the form of command+q to exit the form
         :param element: standard element
         :return:
        """
        try:
            if element:
                self.click_element(element)
                self.exe.driver.execute_script('macos: keys', {'keys': [{
                'key': 'q',
                'modifierFlags': 1 << 4}]})
                assert 1==1
        except Exception as e:
            print("TTT has failed")
            assert 1==0

    def switch_window(self, element=None):
        """
        Switch the main interface
         :param element: standard element
         :return:
        """
        if element:
            self.click_element(element)
        self.driver.execute_script('macos: keys', {'keys': [{
            'key': "XCUIKeyboardKeyTab",
            'modifierFlags': 1 << 4}]})

    def quit(self):
        """
        exit the driver
        :return:
        """
        self.exe.driver.quit()

   

    def test_changeFont(self):
        #self.driver.execute_script('macos: press', {"x": 715, "y": 580})
        """
        Verify the Speech to Text functionality is working
         1. Launch the application
         2. Click the font list
         3. choose a font
        """
        try:
            time.sleep(2)
            self.exe.driver.execute_script('macos: clickAndDrag', {"startX": 715, "startY": 580,"endX": 715, "endY": 580, "duration": 12.0})
            time.sleep(5)
            assert 1==1
        except Exception as e:
                print("Couldnot change font")
                #print("If it is not found, after sleeping for {}s, continue to search; it takes {}s in total".format(interval, interval*(i+1)))
                assert 1==0

    def test_changeSize(self):
        #self.driver.execute_script('macos: press', {"x": 715, "y": 580})
        """
        Verify the Speech to Text functionality is working
         1. Launch the application
         2. Click the font list
         3. choose a font
        """
        try:
            #Goes to Size
            Size= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeButton[1]")
            #print("VALUE IS" + str(TTT))
            self.click_element(Size)
            assert 1==1
        except Exception as e:
                print("Couldnot change size")
                #print("If it is not found, after sleeping for {}s, continue to search; it takes {}s in total".format(interval, interval*(i+1)))
                assert 1==0
   
    def test_write(self):
        """
        Verify the Speech to Text functionality is working
         1. Launch the application
         2. Write a text on input field
         3. Clear the text 
        """
        try:
            #Goes to TTT
            TTT= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeButton[1]")
            #print("VALUE IS" + str(TTT))
            self.click_element(TTT)

            #Input on textbox
            TTTbox= self.is_element_exist("/AXApplication[@AXTitle='Pocketalk Pair']/AXWindow[@AXTitle='Pocketalk Pair' and @AXIdentifier='_NS:6' and @AXSubrole='AXStandardWindow']/AXStaticText[@AXValue='Enter messages here' and @AXIdentifier='_NS:110']")
            self.send_keys("hello world",TTTbox)

        
            #Press send
            TTTsend= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeButton[1]")
            self.click_element(TTTsend)

            time.sleep(3)
            #self.allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            
            #Clear TTT
            self.clear_keys()
            assert 1==1
        except Exception as e:
                print("TTT has failed")
                assert 1==0


    def test_SettingsTraverse(self):
        """
        Verify the Speech to Text functionality is working
         1. Launch the application
         2. Click on settings icon
         4. Traverse through each options
        """
        try:
            #Goes to STT
            TTTsend= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeButton[2]")
            self.click_element(TTTsend) 
            #Goes to settings
            newele= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeWindow/XCUIElementTypeButton[2]")
            self.click_element(newele)

            #Goes to Audio input
            newele1= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeTableRow[2]/XCUIElementTypeCell/XCUIElementTypeStaticText")
            self.click_element(newele1)

            #Goes to Subtitles layout
            newele2= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeTableRow[3]/XCUIElementTypeCell/XCUIElementTypeStaticText")
            self.click_element(newele2)

            #Goes to General
            newele3= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeTableRow[4]/XCUIElementTypeCell/XCUIElementTypeStaticText")
            self.click_element(newele3)

            #Goes to Software updates
            newele3= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeScrollView/XCUIElementTypeTable/XCUIElementTypeTableRow[5]/XCUIElementTypeCell/XCUIElementTypeStaticText")
            self.click_element(newele3)

            #Goes to plans
            newele3= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeButton[2]")
            self.click_element(newele3)
            time.sleep(1)

            #Goes to User manual
            newele3= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeButton[3]")
            self.click_element(newele3)
            time.sleep(1)

            #Goes to Feedback
            newele3= self.is_element_exist("/XCUIElementTypeApplication/XCUIElementTypeDialog/XCUIElementTypeButton[4]")
            self.click_element(newele3)
            assert 1==1
        except Exception as e:
                print("TTT has failed")
                assert 1==0
       



        




if __name__ == '__main__':
    ma = TestTextEdit()
    ma.active_window()
    ma.test_write()
    ma.test_changeFont()
    ma.test_changeSize()
    ma.test_SettingsTraverse()
    ma.test_quit_window()
   
