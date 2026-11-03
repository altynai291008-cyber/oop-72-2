data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for x in data_tuple:
    if type(x) == str:
        letters.append(x)
    else:
        numbers.append(x)

numbers.remove(6.13)

numbers.remove(True)
letters.append(True)

numbers.insert(1,2)

numbers.sort()
letters.reverse()

letters[1] = 'G'
letters[7] = 'c'

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)
print(letters_tuple)
print(numbers_tuple)