import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

url = {
    "Главная": "https://ru.wikipedia.org/wiki/Заглавная_страница",
    }

browser = webdriver.Firefox()

browser.set_window_size(1024, 768)
browser.set_window_position(100, 100)

browser.get(url["Главная"])

input("Начнем. Нажмите Enter")

poisk = input("Введите поисковый запрос для поиска по Вики: \n")

print(f" \n Ваш запрос: {poisk}")

class_str = "vector-search-box-input"
poisk_box = browser.find_element(By.CLASS_NAME,class_str)
poisk_box.send_keys(poisk)
poisk_box.send_keys(Keys.RETURN)

print("Произведен поиск по Вашему запросу")

input("Нажмите Enter для продолжения.")

while True:
    deystvie = input("выберите действие: \n 1 - листать параграфы \n "
                 "2 - перейти на статью по названию статьи \n "
                 "3 - выйти из программы \n")
    if deystvie == "3":
        print("Завершаем программу")
        break

    if deystvie == "1":
        print("Листаем параграфы: \n Жмите Enter для листания. или stop и потом Enter для остановки \n")
        for paragraf in browser.find_elements(By.TAG_NAME, "p"):
            print(paragraf.text)
            listanie = input()
            if listanie == "stop":
                break

    if deystvie == "2":
        statya = input("Введите название статьи для перехода: \n")

        uspeshniy_poisk_statyi = False
        for element in browser.find_elements(By.TAG_NAME, "a"):
            result = element.text
            if result == statya:
                ssylka = element.get_attribute("href")
                uspeshniy_poisk_statyi = True
                browser.get(ssylka)
                print(f"Открыта статья c названием:\n{statya}  \n\n Возвращаемся к выбору действий.")
                break
        if uspeshniy_poisk_statyi == False:
            print("Название статьи не найдено на странице. \n\n Возвращаемся к выбору действий.")


