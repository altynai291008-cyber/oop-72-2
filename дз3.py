from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print("Воин атакует мечом")

class Mage(Hero):
    def attack(self):
        print("Маг использует магию")

class Assassin(Hero):
    def attack(self):
        print("Ассасин атакует из-под тишка")

voin = Warrior("Иван", 1, 100, 10)
mag = Mage("Петр", 2, 50, 15)
ubiytsa = Assassin("Влад", 3, 70, 8)

voin.greet()
voin.attack()
voin.rest()

mag.greet()
mag.attack()
mag.rest()

ubiytsa.greet()
ubiytsa.attack()
ubiytsa.rest()