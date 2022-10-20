# Mac_automation
An automation project of mac default application "TextEdit" using appium-mac2-driver and generated report using allure reporting tool

Install appium mac2 driver- https://github.com/appium/appium-mac2-driver#requirements <br>

Environment deployment on the MAC side (only need to be configured once)
1. Install the Xcode environment
1.1 Open the App Store
1.2 Search Xcode
1.3 After waiting for the download to complete, open Xcode
2. Open Xcode and add Xcode Helper to Accessibility
2.1 Open Finder —> MAC version of Explorer
2.2 Jump to the following address
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/Library/Xcode/Agents/Xcode Helper.app
2.3 Open the icon in the upper left corner of the screen, click System Preferences, click Security and Privacy, click Privacy, click Accessibility, click the unlock button in the lower left corner, enter the password to unlock, and drag the Xcode Helper software to the add bar to complete the assistance. function addition
3. Configure the authentication assistance function
In the macos shell, enter the following command and press Enter
automationmodetool enable-automationmode-without-authentication
4. Install NodeJS environment
4.1 Download the installation package of NodeJS MAC version normally, you can go to the official website to download
Download and install, after the installation is complete, open the mac terminal, enter npm, there is a command line prompt indicating that the installation is successful

5. Switch npm source
5.1 Type in the terminal,
npm install -g nrm
Or shorthand: npm i -g nrm
5.2 Enter nrm ls to view the current available sources, it is recommended to select Tencent source,
nrm use tencent
6. Install Appium2.0 environment
6.1 Type in the terminal
npm i -g appium@next
to install Appium version 2.0

6.2 After the installation is complete, enter (invalid for Appium 1.x)
appium driver list will find that the mac2 driver is not currently installed, and the next step will be to install it

7. Install the appium-mac2-driver driver
7.1 After installing appium, enter
appium driver install mac2
Wait for the mac driver installation to complete

8. Install the software to be tested, such as xxx
8.1 The process of installing conventional software will not be repeated
9. Open the bundle content in the app, remember the bundleId
9.1 After installing the software, open Finder and click the application
9.2 Locate the installed software, right-click, and click Show Package Contents
9.3 Navigate to Info.plist and open it for viewing
9.4 Remember the displayed Bundle identifier content
10. Start the Appium2.0 environment
10.1 Enter in the terminal:
appium and then press Enter to start

11.Install PyTest- pip install -U pytest <br><br>
12.Install allure reporting tool- npm install -g allure-commandline

