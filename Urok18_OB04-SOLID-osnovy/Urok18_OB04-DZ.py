
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Luk(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self):
        pass
class Mech(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self):
        pass
class Kopiyo(Weapon):
    def __init__(self, name):
        self.name = name
    def attack(self):
        pass

class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = "Безоружен"
    def change_weapon(self, weapon_cur:Weapon):
        self.weapon = weapon_cur
        print(f"{self.name} выбирает {self.weapon.name}")
    def attack(self):
        self.weapon.attack()
        print(f"{self.name} берет {self.weapon.name} и наносит удар!")

class Monster():
    def __init__(self, name):
        self.name = name
    def Go(self):
        print(f"{self.name} приближается!")
    def kayuk(self):
        print(f"{self.name} Побежден!")

weapon_list = [Mech("Меч Кладенец"),
               Mech("Меч Самурая"),
               Luk("Лук Эльфов "),
               Kopiyo("Копье Справедливости")]

geroy = Fighter("Алеша Попович")

monster_list = [Monster("Зеленый Гоблин"),
                Monster("Злобный Саурон"),
                Monster("Змей Горыныч")]

monster_list[0].Go()
geroy.change_weapon(weapon_list[0])
geroy.attack()
monster_list[0].kayuk()
print()

monster_list[1].Go()
geroy.change_weapon(weapon_list[2])
geroy.attack()
monster_list[1].kayuk()
print()

monster_list[2].Go()
geroy.change_weapon(weapon_list[3])
geroy.attack()
monster_list[2].kayuk()
print()



