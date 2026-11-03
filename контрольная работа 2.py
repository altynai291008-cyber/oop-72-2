days = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
rashody = []

for day in days:
    rashody.append(int(input(f"Сколько расходов за {day}? ")))

total_sum = sum(rashody)
average_sum = total_sum // 7

print(total_sum)
print(average_sum)