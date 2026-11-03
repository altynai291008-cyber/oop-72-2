#Функции  виды параметров  возращение данных  виды аргументов
from idlelib.pyshell import usage_msg

from Урок3 import counter


def some_name(name,  surname ='неизвестно'):
    print(f'name: {name}, surname: {surname}')


    some_name(name 'bek' surname 'alley'): # reguired positional argument
    some_name(surname='ivanova', name='olva') #keyword arguments
    some_name('mike')


    word = 'geeks'
    print(len(word)*2)


    def len1(iterable):
        counter=0
        for _ in iterable:

        counter +=1
        return counter
    print(len1(word)+4)



    def find_area (length int , width int)-> int:
        return length*width
    sguare_2 = find_area(length:7, width:5)
    sguare_coworking =  find_area(length:15, width:8)
    print(help(find_area))
    print(find_area._doc_)


    #print(sguare_2)
    #print(sguare_coworking)


def plus (*args):
    return sum(args)

print(plus(1,2,6, 9, 8))

def menu(**kwargs):
    return kwargs
monday = menu(eat='pizza', drink='colla')
print(monday)



