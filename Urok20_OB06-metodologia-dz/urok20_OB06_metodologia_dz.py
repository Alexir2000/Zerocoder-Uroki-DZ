
import time

const_Zdorovie = 100
const_Attack = 20

class Hiro():
    def __init__(self, name:str):
        self.name = name
        self.health = const_Zdorovie
        self.attack_power = const_Attack

    def attack(self, other:'Hiro'):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self,player,computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0  # номер хода
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:  # очередность хода
                self.player.attack(self.computer)
                print(f" {self.player.name}=> атакует => {self.computer.name}")
                time.sleep(0.5)
                print(f"У {computer.name} осталось {computer.health} здоровья.")
            else:
                self.computer.attack(self.player)
                print(f" {self.computer.name}=> атакует => {self.player.name}")
                time.sleep(0.5)
                print(f"У {player.name} осталось {player.health} здоровья.")
            turn += 1

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
            elif not self.computer.is_alive():
                print(f"{self.player.name} победил!")
            print()
            time.sleep(1)


player = Hiro("Геймер")
computer = Hiro("Компьютер")

game = Game(player,computer)
game.start()

