import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys






options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
options.page_load_strategy = 'none'

# Ссылка на сайт
url = 'https://www.woman.ru/forum/#show-d-login/'
service = Service()
driver = webdriver.Chrome(service=service, options=options)
try:
    # Закроет страницу если не догрузится
    driver.set_page_load_timeout(10)
    driver.get(url=url)
    # Пауза работы страницы в селениум
    time.sleep(10)
    email_input = driver.find_element(By.NAME, 'username')
    email_input.clear()
    email_input.send_keys('legkovoyger@yandex.ru')

    time.sleep(2)
    pass_input = driver.find_element(By.NAME, 'password')
    pass_input.clear()
    pass_input.send_keys('$7eFFFGF')
    pass_input.send_keys(Keys.ENTER)

    time.sleep(5)
    time.sleep(5)
    find_button_to_create = driver.find_element(By.CLASS_NAME, 'content-nav__right-actions')
    find_button_to_create.click()

    time.sleep(1)
    find_field_to_text = driver.find_element(By.CLASS_NAME, 'tagify__input')
    find_field_to_text.clear()
    find_field_to_text.send_keys('С праздником девачьки, вы самые лучшие на свете 10/10')
    time.sleep(2)

    find_theme_to_text = driver.find_element(By.CSS_SELECTOR, "[name='name'][placeholder='Название темы']")
    find_theme_to_text.clear()
    find_theme_to_text.send_keys('Самое лучшее поздравление для девочек 10/10')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()