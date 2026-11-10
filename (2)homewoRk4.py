rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def _init_(self, сумма_денег, валюта):
        self.сумма_денег = сумма_денег
        self.валюта = валюта

    def convert_to_kgs(self):
        koef = rates[self.unit]
        return self.сумма_денег * koef

    def _add_(self, other):
        лево = self.convert_to_kg()
        право = other.convert_to_kg()
        return Box(лево + право, "KGS")

    def _sub_(self, other):
        лево = self.convert_to_kgs()
        право = other.convert_to_kgs()
        return Money(лево - право, "KGS")

    def _mul_(self, number):
        return Money(self.weight * number, self.валюта)

    def _truediv_(self, number):
        return Money(self.сумма_денег / number, self.валюта)

    def _str_(self):
        return f"{self.сумма_денег} {self.валюта}"

money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

result = money1 + money2
print(result)

