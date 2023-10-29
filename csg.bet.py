from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv
import re
import pandas as pd

ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
options.page_load_strategy = 'none'

# Ссылка на сайт
url = 'https://csg.bet/'
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Закроет страницу если не догрузится
driver.set_page_load_timeout(20)

try:
    driver.get(url=url)
    # Пауза работы страницы в селениум
    time.sleep(15)
    # Сохранение страницы
    with open("index_selenium.html", 'w') as file:
        file.write(driver.page_source)
    time.sleep(2)
    # Данные с сохраненной страницы
    with open("index_selenium.html") as file:
        src = file.read()
    # Включил суп
    soup = BeautifulSoup(src, 'lxml')
    # Поиск по классу
    all_products_class = soup.find_all(
        class_="card darken-3 item-card waves-effect waves-light hoverable withdraw-card")
    steam_url = soup.find_all(
        class_=re.compile('white-text inspect-link'))
    # Создание .csv с заголовками
    with open('Пересчетная таблица.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Стоимость в долларах', 'Стоимость в рублях', 'Количество в наличии','Ссылка'])
    count = 0

    for item in all_products_class:
        # Пополнение таблицы данными со страницы csg.bet
        with open('Пересчетная таблица.csv', 'a', encoding='utf-8-sig', newline='') as file:
            # Поиск ссылки по классу


            # Запись данных в консоли
            b = float(item['data-value']) * 99
            print(f'Название предмета ' + item['data-tooltip'])
            print(f'Стомость в долларах ' + item['data-value'], '$')
            print(f'Количество в наличии ' + item['data-count'])
            print(f'Стоимость в рублях', b, 'рублей')
            # Запись данных в .csv
            writer = csv.writer(file, delimiter=';')
            writer.writerow([item['data-tooltip'],
                             format(float(item['data-value']), '10f'),
                             format(float(b), '10f'),
                             item['data-count']])

            count = count+1



    for item in steam_url:
        cnt=0
        with open('Пересчетная таблица.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            text = item['href']
            text_1=text.replace('#mainContents","","top=250,left=1,width=640,height=900")','')
            text_2= text_1.replace('javascript:open("','')
            writer.writerow([text_2],)
            count = count + 1
            print(text_2)
        
        if count == 2:
            break
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
