#Логических тип данных, операторы условные , сравнения, логические.
time = input('enter time:').lower()
if time == 'morning' or time == 'утро':
    print('good morning')
elif time =='day' or time == 'день':
    print('good afternoon')
elif time == 'evening' or time == 'вечер':
    print('good evening')
else:
    print('hello')