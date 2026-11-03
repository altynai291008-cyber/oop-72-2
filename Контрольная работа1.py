while True:
    color = input("Введите цвет светофора (зеленый, желтый, красный) или 'выход': ").lower().strip()

    if color == "выход":
        print("Программа завершена")
        break
    elif color == "красный":
        print("Стой!")
    elif color == "желтый":
        print("Приготовься!")
    elif color == "зеленый":
        print("Иди!")
    else:
        print("Неверный запрос, введите: зеленый, желтый, красный или выход")