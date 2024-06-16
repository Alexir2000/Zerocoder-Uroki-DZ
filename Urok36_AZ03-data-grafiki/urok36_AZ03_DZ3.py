import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

def func_pars_cian(file_name_pars):
    url = 'https://www.divan.ru/category/uglovye-divany'

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    browser = webdriver.Chrome(options=chrome_options)

    # browser.set_window_size(1024, 768)
    # browser.set_window_position(100, 100)
    print(" Открываем страницу...")
    # Открываем страницу
    browser.get(url)
    print(" Начинаем работу...")
    # Ждем некоторое время для полной загрузки страницы
    time.sleep(10)
    print(" Начинаем парсинг...")
    # Парсим цены
    prices = browser.find_elements(By.XPATH, '//span[@data-testid="price"]')

    # Выводим найденные цены
    # for price in prices:
    #     print(price.text)

    # Открываем файл для записи результатов
    with open(file_name_pars, 'w', encoding='utf-8') as file:
        for price in prices:
            file.write(price.text + '\n')
    # Закрываем браузер
    browser.quit()
    print(" Завершаем работу...")

def func_load_pars(file_name_pars):
    # Читаем информацию из файла в переменную load_pars
    with open(file_name_pars, 'r', encoding='utf-8') as file:
        load_pars = file.readlines()
    price = []
    str_del_text = "руб."
    for line in load_pars:
        price_str = line.replace(str_del_text, "").strip()
        price_str = price_str.replace(" ", "")
        price.append(int(price_str))
    return price

def func_main(price):
    data = {"Цена": price}
    df = pd.DataFrame(data)
    kol = str(len(price))
    kol_text = "Количество найденных диванов: " + str(len(price)) +" шт."
    sred_cena = df['Цена'].mean()
    sred_cena_text = "Средняя цена диванов из раздела:  " + str(round(sred_cena)) + " руб."
    print(f"\n Количество найденных диванов: {kol}")
    print(f"\n Средняя цена диванов из раздела: - {sred_cena:.0f} \n")

    # for line in price:
    #     print(line)
    # Создаем гистограмму
    plt.hist(price, bins=12)
    plt.xlabel('Цена (в рублях)')
    plt.ylabel('Количество')
    plt.title('Гистограмма цен на диваны')
    plt.grid(True)
    plt.text(0.5, -0.25, kol_text, ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
    plt.text(0.5, -0.35, sred_cena_text, ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
    plt.subplots_adjust(bottom=0.3)
    # Показываем гистограмму
    plt.show()

file_name_pars = 'pars_url.txt'

# здесь мы парсим сайт и сохраняем в файл
# func_pars_cian(file_name_pars)

price = func_load_pars(file_name_pars)

func_main(price)




