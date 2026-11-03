#Операторы пренадлежности  назначения циклы

counter = 1
while counter < 20:
    counter += 1
    if counter == 13:
        break
    if counter in (5, 10):
        continue
    print("Hello World", counter)


rounds = int(input("how many rounds"))
while rounds > 0:
    time = input('enter time:').lower()
    if time == 'stop':
        break
    if time == 'morning' or time == 'утро':
        print('good morning')
    elif time =='day' or time == 'день':
        print('good afternoon')
    elif time == 'evening' or time == 'вечер':
        print('good evening')
    else:
        print('hello')
    rounds -= 1

#цикл  for
    word = "KYRGYZSTAN"
    for letter in word:
        if letter == 'Z':
            break
        if letter == 'YRZ':
            continue
        print(letter)