import sys
import os
path = os.getcwd()
sys.path.append(os.path.abspath(os.path.join(path, os.pardir)))
from time import time
from behave import given
from appium import webdriver
import appConfig as appConf
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Start the android app automation test")
def startAndroidAppAutomationTest(self):
    if os.environ.get("LT_USERNAME") is None:
        username = "username" #Enter LT username here if environment variables have not been added
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        accesskey = "accesskey" #Enter LT accesskey here if environment variables have not been added
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    driver = webdriver.Remote(
        command_executor="https://"+username+":"+accesskey+"@beta-hub.lambdatest.com/wd/hub",
        desired_capabilities=appConf.app_android_desired_caps
        )
    try:
        colorElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/color")))
        colorElement.click()

        textElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Text")))
        textElement.click()

        toastElement = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/toast")))
        toastElement.click()

        notification = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()

        home = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Home")))
        home.click()

        speedTest = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()

        home = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Home")))
        home.click()

        browser = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/Browser")))
        browser.click()

        url = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver,20).until(EC.element_to_be_clickable((MobileBy.ID,"com.lambdatest.proverbial:id/find")))
        find.click()

        #MARKING TEST AS PASSED
        driver.executeScript("lambda-status=passed")

        driver.quit()
    except:
    
        #MARKING TEST AS FAILED
        driver.executeScript("lambda-status=failed")
        driver.quit()
