
# Менеджер задач
# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from datetime import datetime, timedelta
class Zadacha():
    def __init__(self, opisanie=""):
        #from datetime import datetime, timedelta
        self.opisanie = opisanie
        self.date = None # datetime.now() + timedelta(days=1)
        self.status = False
        self.sost = "Не выполнено"

    def vvod_date(self):
        while True:
            status_end = True
            try:
                # Пользовательский ввод строки даты в формате "дд.мм.гггг"
                date_str = input("Введите дату в формате дд.мм.гггг: ")
                # Преобразование строки в datetime
                self.date = datetime.strptime(date_str, "%d.%m.%Y")
                break  # Если формат был правильным, выйти из цикла
            except Exception as e:
                print(f"Неправильный формат даты. Ошибка  {e}")
                # Вывод сообщения об ошибке, если введен неверный формат
                status_end = False
        return status_end
    def set_date(self, date):
        status_end = True
        try:
            # Преобразование строки в datetime
            self.date = datetime.strptime(date, "%d.%m.%Y")
        except:
            # Вывод сообщения об ошибке, если введен неверный формат
            status_end = False
        return status_end

    def set_Status(self,status):
        status_end = True
        try:
            self.status = status
            if self.status:
                self.sost = "Задача выполнена"
            else:
                self.sost = "Не выполнено"
        except ValueError:
            status_end = False
        return status_end

    def set_opisanie(self, opisanie):
        status_end = True
        try:
            # Преобразование строки в datetime
            self.opisanie = opisanie
        except ValueError:
            # Вывод сообщения об ошибке, если введен неверный формат
            status_end = False
        return status_end

    def print_zadacha(self):
        print(f" Описание задачи: {self.opisanie}")
        if self.date is not None:
            print(f" Срок выполнения: {self.date.strftime('%d-%m-%Y')}")
        else:
            print(f" Срок выполнения: {self.date}")
        print(f" Состояние задачи: {self.sost}")


class Task():
    def __init__(self):
        self.spisok = []

    def nov_zadacha(self):
        status_end = True
        opisanie_str = input("Введите задачу: ")
        while True:
            status_end = True
            try:
                #date_str = input("Введите дату выполнения задачи в формате дд.мм.гггг: ")
                # Преобразование строки в datetime
                #date = datetime.strptime(date_str, "%d.%m.%Y")
                new_zd = Zadacha(opisanie_str)
                #new_zd.set_date(date)
                self.spisok.append(new_zd)
                break  # Если формат был правильным, выйти из цикла
            except Exception as e:
                print(f"Неправильный ввод данных. Ошибка  {e}")
                # Вывод сообщения об ошибке, если введен неверный формат
                status_end = False

        return status_end
    def print_spisok(self):
        print(" Полный список текущих задач")
        for element in self.spisok:
            print(f"задача: {element.opisanie}, статус: {element.sost}")
    def print_spisok_aktual(self):
        print(" Список задач еще НЕ выполнены")
        for element in self.spisok:
            if not element.status:
                print(f"задача: {element.opisanie}, статус: {element.sost}")

    def set_vipolneno(self, text_zadachi):
        for element in self.spisok:
            if text_zadachi == element.opisanie:
                element.status = True
                element.sost = "Задача выполнена"


zd1 = Zadacha()
zd1.set_opisanie(" Пойти поесть")
#zd1.vvod_date()
zd1.set_date("30.03.2024")

zd1.print_zadacha()
zd1.set_Status(True)
zd1.print_zadacha()

task = Task()

task.nov_zadacha()
task.nov_zadacha()
task.nov_zadacha()

task.print_spisok()

zd = "Поесть"
task.set_vipolneno(zd)

task.print_spisok_aktual()