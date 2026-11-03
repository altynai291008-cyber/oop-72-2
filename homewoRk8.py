import keyword

keywords_list = keyword.kwlist

otlichno = []
yes = 0
no = 0

for k in keywords_list:
    n = int(input(f'{k} от 1-10: '))
    if n >= 6:
        yes += 1
    else:
        no += 1
    if n >= 9:
        otlichno.append(k)

print('Всего:', len(keywords_list))
print('Пройдено:', yes, f'{yes / len(keywords_list) * 100}%')
print('Не пройдено:', no, f'{no / len(keywords_list) * 100}%')
print('>=9:', otlichno)