import csv
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

url1 = "https://www.divan.ru/category/svet"

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=chrome_options)

browser.set_window_size(1024, 768)
browser.set_window_position(100, 100)

browser.get(url1)

input("Начнем. Нажмите Enter")

class_str = "div.WdR1o"
svet_all = browser.find_elements(By.CSS_SELECTOR,class_str)

svet_data = []

                # "name": divan.css("div.lsooF span::text").get(),
                # "cena": divan.css("div.q5Uds span.ui-LD-ZU::text").get(),
                # "url": divan.css("a").attrib["href"]

for svet in svet_all:
    try:
        name_div_class = "div." + "lsooF"
        name_span = "span"
        cena_div_class = "div." + "q5Uds"
        cena_span_class = "span." + "ui-LD-ZU"
        link_a_class = "href"

        name = (svet.find_element(By.CSS_SELECTOR,name_div_class).
                find_element(By.TAG_NAME,name_span).text)
        cena = (svet.find_element(By.CSS_SELECTOR,cena_div_class).
                find_element(By.CSS_SELECTOR,cena_span_class).text)
        link = svet.find_element(By.TAG_NAME, "a").get_attribute("href")

    except:
        print(" Произошла ошибка парсинга в блоке данных, продолжаем другой блок...")
        continue

    svet_data.append([name, cena, link])

browser.quit()

file_name = "pars.csv"
with open(file_name,"w",newline="",encoding="utf-8") as file:
    zapis_file = csv.writer(file)
    zapis_file.writerow(["Название светильника", "Цена", "Ссылка"])
    zapis_file.writerows(svet_data)
