eng_to_rus = str.maketrans(
    "qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>",
    "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
)
rus_to_eng = str.maketrans(
    "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ",
    "qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>"
)

while True:
    word = input("введите слово : (для выхода нажмите 'q') ")

    if word.lower() in ['q', 'й']:
        print("программа завершена")
        break

    converted_word = ""
    for char in word:
        if char in eng_to_rus:
            converted_word += char.translate(eng_to_rus)
        elif char in rus_to_eng:
            converted_word += char.translate(rus_to_eng)
        else:
            converted_word += char

    print(converted_word.lower())