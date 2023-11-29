from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--headless')

service = Service('webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.fizyka.pw.edu.pl/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')

main_div = driver.find_element(By.CLASS_NAME, 'content-view-full-folder-pracownikow')

for results in main_div.find_elements(By.CSS_SELECTOR, 'h2, h2 + div'):
    print(results.tag_name)
    print(results.text.strip())
    print('------------------')


#time.sleep(1000)
driver.close()