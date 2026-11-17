# Эта библиотека нужна для окрашивания текста в консоли в разные цвета, чтобы сделать вывод программы более наглядным.
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + "Успех! Внешняя библиотека colorama работает.")
print(Fore.YELLOW + "Предупреждение: не забудьте залить проект на GitHub.")
print(Fore.CYAN + Style.BRIGHT + "Домашнее задание №6 выполнено!")