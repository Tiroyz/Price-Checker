from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
from PIL import Image

xshift = 140

def cropimage(elem, browser, name):
    global xshift
    location = elem.location
    size = elem.size
    browser.save_screenshot('pagescreenshot.png')
    
    x = location['x'] + xshift 
    y = location['y'] - 50
    width = x + size['width'] + 100
    height = y + size['height']
    xshift += 125
    fullImg = Image.open("pagescreenshot.png") 
    cropImg = fullImg.crop((x, y, width, height)) 
    cropImg.save(str(name) + '.png')

def parcer(barcode):
    translate_symbols = {'™':None, '®':None}
    translate_table = str.maketrans(translate_symbols)  # Создание таблицы для метода translate

    barcode = str(barcode)
    option = Options()
    option.add_argument("--disable-infobars") 
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome('E:\Programs\Python\ChromeDriver\chromedriver.exe', options=option)
    browser.get('http://ru.disai.org/accreditation_check/search_by_GTIN')
    elem = browser.find_element(By.NAME, 'search_query')
    elem.send_keys(str(barcode) + Keys.RETURN)
    time.sleep(1)
    # share = browser.find_element(By.CLASS_NAME, 'btn.btn_.btn-small_')
    # share.click()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    if soup.find_all('td'):
        data = str(soup.find_all('td')[3].text.replace('<br />','\n').strip())
        data = data.translate(translate_table)  # Очистка строки от ненужных симолов, согласно словарю translate_symbols
        if len(data) > 30:
            data = data[:data.find(' ', 30)]     # Сокращение слишком длинных строк
        return data
    else: return False


def ozon_parcer(name):
  
    option = Options()
    option.add_argument("--start-maximized")
    option.add_argument("--disable-infobars") 
    option.add_experimental_option('excludeSwitches', ['enable-logging'])   # Функция для обхода cloudfare
    browser = webdriver.Chrome('E:\Programs\Python\ChromeDriver\chromedriver.exe', options=option)

    browser.get('https://www.ozon.ru')
    elem = browser.find_element(By.NAME, 'text')
    elem.send_keys(str(name) + Keys.RETURN)

    time.sleep(3)

    browser.execute_script("window.scrollTo(0, 150)")

    elements_arr = [browser.find_element(By.XPATH, '//*[@id="paginatorContent"]/div/div/div[1]')]
    elements_arr.append(browser.find_element(By.XPATH, '//*[@id="paginatorContent"]/div/div/div[2]'))
    elements_arr.append(browser.find_element(By.XPATH, '//*[@id="paginatorContent"]/div/div/div[3]'))

    href = [elements.get_attribute('href') for elements in elements_arr]    # Переменная для хранения ссылок на товары

    time.sleep(3)

    return href


barcode = '8594737253317'

name = 'НОВО-ПАССИТ, ТАБЛЕТКИ ПОКРЫТЫЕ'

print(name)

ozon_parcer(name)