def is_strong_password(password):
    if len(password) < 6:
        return False

    цифра_есть = False
    большая_есть = False
    маленькая_есть = False
    сколько_спец = 0

    for буква in password:
        if буква.isdigit():
            цифра_есть = True
        if буква.isupper():
            большая_есть = True
        if буква.islower():
            маленькая_есть = True
        if буква in "$#@%!&*()/?!;:-_":
            сколько_спец += 1

    if цифра_есть and большая_есть and маленькая_есть and сколько_спец >= 2:
        return True
    else:
        return False


print(is_strong_password('$PassW/12'))
print(is_strong_password('3gT*5?O'))
print(is_strong_password('k2-iR!49;'))
print(is_strong_password('12345'))
print(is_strong_password('password'))
