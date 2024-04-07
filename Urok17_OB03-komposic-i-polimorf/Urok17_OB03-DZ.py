

# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`,
# и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты
# и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников,
# например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, vozrast):
        self.name = name
        self.vozrast = vozrast
    def make_sound(self):
        print("Животное кричит")

    def eat(self):
        print("животное ест")

class Ptiza(Animal):
    def __init__(self, name, vozrast, vid, zvuk):
        super().__init__(name, vozrast)
        self.vid = vid
        self.zvuk = zvuk
    def make_sound(self):
        print(f" {self.name} - {self.vid} кричит {self.zvuk}")

class Mlekopit(Animal):
    def __init__(self, name, vozrast, vid, zvuk):
        super().__init__(name, vozrast)
        self.vid = vid
        self.zvuk = zvuk
    def make_sound(self):
        print(f" {self.name} - {self.vid} кричит {self.zvuk}")

class Reptiliya(Animal):
    def __init__(self, name, vozrast, vid, zvuk):
        super().__init__(name, vozrast)
        self.vid = vid
        self.zvuk = zvuk
    def make_sound(self):
        print(f" {self.name} - {self.vid} кричит {self.zvuk}")


class Sotrudnik_Zoo():
    def __init__(self, name):
        self.name = name

    def umenie(self):
        return "разнорабочий, делает разные дела"

class Smotritel_Zoo(Sotrudnik_Zoo):
    def __init__(self, name):
        super().__init__(name)
    def umenie(self):
        return "Кормит животных"


class Veterinar_Zoo(Sotrudnik_Zoo):
    def __init__(self, name):
        super().__init__(name)
    def umenie(self):
        return "Лечит животных"
class Zoo():
    def __init__(self):
        self.spisok_animal = []
        self.spisok_sotrudnki = []

    def add_animal(self, animal:Animal):
        self.spisok_animal.append(animal)
        print(f" {animal.name} - {animal.vid} - добавлен в зоопарк")

    def add_sotrudnik(self, sotrudnik):
        self.spisok_sotrudnki.append(sotrudnik)
        print(f" Сотрудник: {sotrudnik.name} добавлен в штат зоопарка")

animals1 = Mlekopit("Маша", 3, "Обезьяна", " Дай-Дай")
animals2 = Mlekopit("Даша", 25, "Слон", " У-ууух-х")
animals3 = Reptiliya("Гоша", 12, "Варан", " Щелк")
animals4 = Ptiza("Гоша", 12, "Орел", " Я орел")
animals5 = Ptiza("Гоша", 12, "Павлин", " Гхы - гхы")

animal_list = [animals1, animals2, animals3, animals4, animals5 ]

print(" \n Звери кричат:")
for i in animal_list:
    i.make_sound()

print(" Зверей больше нет")

sotrudnik1 = Sotrudnik_Zoo("Вася")
sotrudnik2 = Sotrudnik_Zoo("Петя")
sotrudnik3 = Veterinar_Zoo("Георгий Иваныч")
sotrudnik4 = Smotritel_Zoo("Вениамин Сергеич")

zoopark = Zoo()

zoopark.add_sotrudnik(sotrudnik1)
zoopark.add_sotrudnik(sotrudnik2)
zoopark.add_sotrudnik(sotrudnik3)
zoopark.add_sotrudnik(sotrudnik4)

for i in animal_list:
    zoopark.add_animal(i)

print(" \n Звери в зоопарке кричат:")
for i in zoopark.spisok_animal:
    i.make_sound()

print(" \n Сотрудники в зоопарке делают:")
for i in zoopark.spisok_sotrudnki:
    print(f"Сотрудник {i.name} - {i.umenie()}")
