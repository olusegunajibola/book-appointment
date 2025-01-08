import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

from dotenv import load_dotenv
load_dotenv()

import os
import openpyxl

options = Options()
# disable save password popup
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)
# end

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("window_size=1280,800")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-save-password-bubble")

# open chrome
driver = webdriver.Chrome(options=options)
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(1);')

website = os.environ["website"]
driver.get(website)
driver.maximize_window()
time.sleep(5)



# Enter email
email = driver.find_element(By.XPATH, "//*[@id='login-email']")
email.send_keys(os.environ["Email"])
time.sleep(10)

# Enter password
password = driver.find_element(By.XPATH, "//*[@id='login-password']")
password.send_keys(os.environ["Password"])
time.sleep(10)

# click forward i.e login
log_in = driver.find_element(By.XPATH, "//*[@id='login-form']/button")
log_in.click()

driver.find_element(By.XPATH,"//*[@id='advanced']/span").click()
time.sleep(10)

# book appointment or check where possible
book = driver.find_element(By.XPATH,
                           "//*[@id='dataTableServices']/tbody/tr[1]/td[4]/a/button")
book.click()
