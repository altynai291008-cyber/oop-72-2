class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


hero1 = Hero("Aragorn", 5, 100, 15)
hero2 = Hero("Legolas", 6, 80, 12)

hero1.greet()
print(hero1.strength)
hero1.attack()
print(hero1.strength)

print()

hero2.greet()
print(hero2.health)
hero2.rest()
print(hero2.health)