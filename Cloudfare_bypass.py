from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from platform import system
import os
import time


options = Options()
# options.add_argument("--headless")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars") 
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars") 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

exec_path = os.path.join(os.getcwd(), 'driver', 'chromedriver.exe') if system() == "Windows" else \
    os.path.join(os.getcwd(), 'driver', 'chromedriver')

browser = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, executable_path=exec_path))

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})

browser.get('https://nowsecure.nl/')
time.sleep(4)
# print("reset driver")
# handle = browser.current_window_handle
# browser.service.stop()
# time.sleep(6)
# browser = webdriver.Chrome('E:\Programs\Python\ChromeDriver\chromedriver.exe', options=options)
# browser.switch_to.window(handle)
# time.sleep(5)