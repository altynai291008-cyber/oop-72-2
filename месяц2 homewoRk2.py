import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print("Привет! Я герой " + self.name)

    def attack(self):
        print(self.name + " атакует!")

    def rest(self):
        self.health += 20
        print(self.name + " отдохнул.")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


warrior = Warrior("Конан", 5, 100, 20, 50)
mage = Mage("Гэндальф", 5, 70, 10, 100)
assassin = Assassin("Эцио", 5, 80, 15, 70)

print("Выберите героя: Warrior / Mage / Assassin")
user_choice = input()

heroes = ["Warrior", "Mage", "Assassin"]
enemy_choice = random.choice(heroes)

print("Вы выбрали: " + user_choice)
print("Противник: " + enemy_choice)

if user_choice == "Warrior":
    warrior.attack()
elif user_choice == "Mage":
    mage.attack()
elif user_choice == "Assassin":
    assassin.attack()

if enemy_choice == "Warrior":
    warrior.attack()
elif enemy_choice == "Mage":
    mage.attack()
elif enemy_choice == "Assassin":
    assassin.attack()


if user_choice == enemy_choice:
    print("Ничья!")

elif user_choice == "Warrior":
    if enemy_choice == "Assassin":
        print("Warrior победил!")
    elif enemy_choice == "Mage":
        print("Mage победил!")

elif user_choice == "Assassin":
    if enemy_choice == "Mage":
        print("Assassin победил!")
    elif enemy_choice == "Warrior":
        print("Warrior победил!")

elif user_choice == "Mage":
    if enemy_choice == "Warrior":
        print("Mage победил!")
    elif enemy_choice == "Assassin":
        print("Assassin победил!")