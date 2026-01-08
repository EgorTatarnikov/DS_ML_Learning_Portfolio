# ============================================================
# 1. PYTHON BASICS
# ============================================================

# создаем простейшие функции
def square(x):
    return x * x

def sub (x, y):
    return x - y

def exchange (x, y):
    temp = x
    x = y
    y = temp
    return x, y

print(sub(5, 1))            # 4

print(sub(5, sub(4, 1)))    # 2


# следующие 150 строк разбираемся с типами данных, изменяемостью и хранением в памяти
t1 = (5, 1)
t2 = 4, 2

print(type(t2))             # <class 'tuple'>

print(exchange(1, 5))       # (5, 1)

x1, x2 = t1                 # это называется распаковка кортежа (tuple unpacking)
                            # Python сразу «распаковывает» его — присваивает первое значение переменной x1, 
                            #                                                       второе — переменной x2.
x1, x2                      # (5, 1)
print(x1, x2)               # 5 1
print(type(exchange(1, 5))) # <class 'tuple'>

print(square(5))            # 25

print(type("Hello World!")) # <class 'str'>

print('''Hello          
How are you?''')            # ''' ''' и """ """ позволяет писать многостроковые строки

print('Hello \\ ')          # \ позволяет написать после него "зарещенные" символы
print('hi\'')

print(45000)                # 45000
print(45_000)               # 45000, _ можно использовать для удобства чтения больших чисел
print(45, 000)              # 45 0

print(45, "hello", x1)      # 45 hello 5
#print(45 + "hello") #error
print(str(45) + "hello")    # 45hello

type('c')                   # <class 'str'> В Python нет отдельного типа для отдельных символов
print(ord('a'))             # ord() в Python возвращает числовой код (Unicode) символа.

in1 = input('Input smth: ')
print('Type of in1:', type(in1))

n = input("Please enter your name (str): ")
print("Hello", n)

my_age = int(input('How old I am (int): '))
print('My age:', my_age, '\nType of "my_age":', type(my_age))
print(int(1.9)) # output 1

i = int()
print(i)
i = 'hi'
print(i)        # иллюстрация динамического типизирования.

a = 'hello'

# Python при запуске создаёт заранее объекты int для чисел от –5 до 256 и повторно использует их, 
# чтобы ускорить работу и сэкономить память.
a = 100         
b = 100
print(id(a))    # 140717307187080
print(id(b))    # 140717307187080
print(a == b)   # True 
print(a is b)   # True — оба указывают на один и тот же объект
x = 1000
y = 1000
print(id(x))    # 2648153138224
print(id(y))    # 2648153141872 отличается
print(x == y)   # True
print(x is y)   # False — это разные объекты, хотя значения равны


print(id(a))    # 2648156418480
b = a
print(id(b))    # 2648156418480 также
print(a == b)   # True
a = 500
print(id(a))    # 2648153141456 поменялось
print(b)        # 100 осталось без изменения
print(id(b))    # 2648156418480 осталось без изменения
print(a == b)   # False
# int и str неизменяемые. 
# В Python переменные — это ссылки на объекты, а не "ячейки памяти", как в C.
# Присваивание b = a копирует ссылку, но не сам объект.
# При переназначении a (перенаправлении её на другой объект), b остаётся привязанной к старому.

a = 7
b = 8
print(hex(id(a)))   # 0x7ffb4d1bc3e8
print(hex(id(b)))   # 0x7ffb4d1bc408
b = 8 - 1
print(hex(id(a)))   # 0x7ffb4d1bc3e8
print(hex(id(b)))   # 0x7ffb4d1bc3e8
print(a == b)       # True
print(a is b)       # True


# Списки изменяемые
l1 = [1, 2, 3]
l2 = l1
print(hex(id(l1)))  # 0x268926c1bc0
print(hex(id(l2)))  # 0x268926c1bc0
l1.append(4)
print(l1)           # [1, 2, 3, 4]
print(l2)           # [1, 2, 3, 4]
print(hex(id(l1)))  # 0x268926c1bc0 адрес не поменялся
print(hex(id(l2)))  # 0x268926c1bc0
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # True — это один и тот же объект

l1 = [4, 5, 6]      # не изменил а переназначил.
print(hex(id(l1)))  # 0x2689266ef00 новый адрес
print(hex(id(l2)))  # 0x268926c1bc0 старый адрес
print(l1 == l2)     # False - значения разные
print(l2 is l2)     # False - объекты разные

l1 = [1, 2, 3, 4]   # переназначил старые значения
print(l1)           # [1, 2, 3, 4]
print(l2)           # [1, 2, 3, 4]
print(hex(id(l1)))  # 0x268926c1680 новый адрес
print(hex(id(l2)))  # 0x268926c1bc0 не совпадает
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # False - объекты разные

print(len('hello'))

x = 0
x += 3  # increment x by 3; same as x = x + 3
print(x)
x += 1
print(x)


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)))  # 0x268926c1680
print(hex(id(l2)))  # 0x2689266ef00
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # False - объекты разные


from python_summary_module_example import calculate
calculate(4, 4)

import random
print(random.random())
print(random.randrange(1, 10))

a = 502
b = 503
print(id(a))    # 2648153138224
print(id(b))    # 2648153140944

3/2             # 1.5 деление всегда дает в результате флоат
3/3             # 1.0
1+1.0           # 2.0
x = 10
x **= 3 
print(x)        # 1000
x = 0b11        # бинарная запись чисел
x = 0o74        # восьмиричная
x = 0xa13       # шестнадцатиричная
print(x)        # 2579, при выводе переводит в десятичную

print(bin(15))  # 0b1111
print(oct(15))  # 0o17
print(hex(15))  # 0xf

x = 3e310       # максимальное значение для float ограничено — обычно это около 1.8e308
print(x)        # inf
type(x)         # float


# Decimal
from decimal import Decimal

d = Decimal(10)
print(d/20)
print(0.1 + 0.2)
print(Decimal(0.1)+Decimal(0.2)) #неточно

a = Decimal("0.1")  # Важно: всегда создавай Decimal из строк, 
b = Decimal("0.2")  # чтобы избежать неточностей при преобразовании float.
print(type(a))
print(a + b)


# Tuples, Lists and Strings
x = 1, 2
y = (2,)
print(type(x))
print(x)
print(y)
empty_tuple = ()
empty_tuple = tuple()

print("He said \"Hello\"")  # He said "Hello"


# Indexes
string = "Hello World!"
print(string[-1])
for char in string:
    print(char)


# The Slice Operator
print(string[3:5])      # lo
h = string[:5]          # элемент с индексом 5 не включается
w = string[6:]
print(h, w)             # Hello World!

list_1 = ['Tatarnikov', 'Egor', 30, 'Korolev']
print(list_1)
print(list_1[1])
print(list_1[:2])       # ['Tatarnikov', 'Egor']
print(list_1[0][:5])    # Tatar

tuple_1 = ('Tatarnikov', 'Egor', 30, 'Korolev')
print(tuple_1)
print(tuple_1[1])
print(tuple_1[:2])      # ('Tatarnikov', 'Egor')
print(tuple_1[0][:5])   # Tatar

# Python автоматически интернирует некоторые строки, особенно: короткие строки (например, 'a', 'abc')
# Интернирует - значит хранит в одном экземпляре и переиспользует один и тот же объект в памяти, 
# вместо создания новых. Это оптимизация памяти и скорости.
string = 'a'
print(id(string))  # 140717306530904
s = 'a'
print(id(s))       # 140717306530904
print(string is s) # True - интернирование

dict_2 = {'Family Name': 'Tatarnikov',
          'First Name': 'Egor',
          'Age': 30,
          'City': 'Korolev'}
print(dict_2)
print(dict_2['Age'])

dict_3 = {
    'Family Name': ['Tatarnikov', 'Basova'],
    'First Name': ['Egor', 'Svetlana'],
    'Age': [30, 28],
    'City': ['Korolev', 'Korolev']
}
for key in dict_3.keys():
    print(key)
for value in dict_3.values():
    print(value)
dict_3['Age'][0]

string = 'Hello World!'
string.count('l')  # количество вхождений
string.index('l')  # индекс первого вхождения
string.index('lo') # первого символа первого вхождения

string = 'Hello World!'
l1 = string.split()
print(l1)
print(type(l1))
l2 = string.split('o') # можно назначить сепаратор
print(l2)

s = ' '             # назначаем строку склеиватель
s.join(l1)

'o'.join(l2)        # !!!

alist = [1, 3, 5]
print(alist + alist)
print(alist * 3)
alist.count(5)  # количество вхождений
alist.index(5)  # индекс первого вхождения



# The for Loop
for i in range(5):
    print(i)
    #i += 1     # не нужна, i сама берет следуюшее значение из range на каждом шаге
    i += 2      # вывод все равно 0 1 2 3 4
    
for i in range(0, 10, 2):   # дмапазон от 0 (включительно) до 10 (не включая) с шагом 2
    print(i)    # 0 2 4 6 8
    
for num in [1, 3, 42, 21]:
    print(num)
    
for num in (1, 3, 42, 21):
    print(num)
    
for char in "Hello":
    print(char)

dict_2 = {'Family Name': 'Tatarnikov',
          'First Name': 'Egor',
          'Age': 30,
          'City': 'Korolev'}

for k in dict_2:
    print(k)    # Family Name ... печатает ключи
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for fruit in fruits:
    print(fruit)  
    
for i in range(len(fruits)):    # we can iterate through the indexes by generating a sequence of them, using the range function
    print(i, fruits[i])         # 0 apple ...
    
    
# Turtle class    
import turtle
egor = turtle.Turtle()
egor.forward(100)


# if conditions
x = int(input("Enter x: "))
if x < 5:
    print('x < 5')
else:
    print('x >= 5')
    
if x < 5:
    print('x < 5')
elif x < 10:
    print('5 <= x < 10')   
else:
    print('x >= 10')


# Boolean Expressions
print(True)
print(type(True))
print(type(False))
print(type(bool('True')))
x = 1
y = 2
x == y               # x is equal to y
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y


# Logical operators: and, or, not
x = True
y = False
print(x and y)
print(x or y)
print(not x)

if x and (x or y):
    x = not x
    print('x:', x)
else:
    x = not y
    y = not y
    print('y:', y)


# in, not in
print('a' in 'a')           # True
print('apple' in 'apple')   # True
print('' in 'a')            # True
print('' in 'apple')        # True

print('x' not in 'apple')   # True

print("a" in ["a", "b", "c", "d"])  # True
print(2.0 in [3, 2, 9, 10, 9.0])    # True

y = ["0", 2]
z = [0, 1]
# is x inside of y or z
'x' in y or z # wrong
'x' in y or 'x' in z


# assert - Оператор assert  полезен при отладке программ, поскольку позволяет быстро обнаружить проблемы
# assert останавливает программу, если условие ложно, с выбросом исключения AssertionError
def divider(x, y):
    assert y != 0, 'Деление на ноль'
    print(x / y)
    return x / y

# divider(5, 0)   # AssertionError: Деление на ноль

"""
If the code has conditional blocks (if..elif..else) 
then you’ll want to have tests that check that the right block executes when you expect it to.
"""
x = 3
y = 4
if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        ## x must be equal to y
        assert x==y
        z = 0
      
      
        
# Sequence Mutation

fruit = ["banana", "apple", "cherry"]
print(hex(id(fruit)))   # 0x22f38371f40
fruit[0] = "pear"
print(hex(id(fruit)))   # 0x22f38371f40 не изменилось

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []  # Удаляются элементы с индексами 1 и 2: 'b' и 'c'
print(alist)     # ['a', 'd', 'e', 'f']

alist[4:4] = ['e']  # Вставка 'e' перед элементом с индексом 4 (то есть перед 'f')
print(alist)        # ['a', 'd', 'e', 'e', 'f']

a = ['one', 'two', 'three']
del a[1]  # Удаляется элемент с индексом 1: 'two'
print(a)  # ['one', 'three']

a.remove('three')  # Удаляется элемент со значением 'three'
print(a)           # ['one']

# копирование (клонирование) листов
import copy

a = [1, 2, [3, 4]]
b = a                  # ссылка — всё общее
c = a.copy()           # поверхностная копия — вложенные объекты общие
d = a[:]               # тоже поверхностная копия
e = copy.deepcopy(a)   # глубокая копия — всё независимое

# Меняем исходный список:
a[0] = 'x'
a[2][0] = 'y'

print("a =", a)  # ['x', 2, ['y', 4]]
print("b =", b)  # ['x', 2, ['y', 4]] — то же самое, потому что ссылка
print("c =", c)  # [1, 2, ['y', 4]] — верхний уровень скопирован, вложенный остался общим
print("d =", d)  # [1, 2, ['y', 4]] — как и c
print("e =", e)  # [1, 2, [3, 4]] — полностью независимая копия




# Methods on Strings and Lists

# Examples of working with list methods in Python

# append(item) – добавляет один элемент в конец списка
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# extend(iterable) – добавляет все элементы из переданного итерируемого объекта в конец списка
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # [1, 2, 3, 4, 5]

# Using the concatenation operator "+" creates a new list (new object)
lst = [1, 2, 3]
print(hex(id(lst)))  # 0x7f8b582c5c00 — original list
lst = lst + [4]
print(lst)  # [1, 2, 3, 4]
print(hex(id(lst)))  # 0x7f8b582c5d00 — new object created

# Using += (in-place addition) modifies the existing list without changing its identity
lst = [1, 2, 3]
print(hex(id(lst)))  # 0x7f8b582c5e00 — original list
lst += [4]
print(lst)  # [1, 2, 3, 4]
print(hex(id(lst)))  # 0x7f8b582c5e00 same as before — list modified in place

# Summary:
# - append() → in-place, adds one element
# - +        → creates new list object (new id)
# - +=       → in-place, adds elements from another iterable (like extend)


# insert(position, item) – вставляет элемент на указанную позицию
lst.insert(1, 99)  # [1, 99, 2, 3, 4]

# pop() – удаляет и возвращает последний элемент списка
last = lst.pop()  # last = 4, lst = [1, 99, 2, 3]

# pop(position) – удаляет и возвращает элемент по индексу
second = lst.pop(1)  # second = 99, lst = [1, 2, 3]

# sort() – сортирует список по возрастанию (изменяет сам список)
lst.sort()  # [1, 2, 3]

# reverse() – разворачивает список в обратном порядке (изменяет сам список)
lst.reverse()  # [3, 2, 1]

# index(item) – возвращает индекс первого вхождения элемента
idx = lst.index(2)  # idx = 1

# count(item) – возвращает количество вхождений элемента
ct = lst.count(3)  # ct = 1

# remove(item) – удаляет первое вхождение элемента
lst.remove(3)  # lst = [2, 1]




# Examples of working with string methods in Python

s = "  Hello, World! Hello!  "

# upper() – возвращает строку в верхнем регистре
print(s.upper())  # "  HELLO, WORLD! HELLO!  "

# lower() – возвращает строку в нижнем регистре
print(s.lower())  # "  hello, world! hello!  "

# strip([chars]) – удаляет пробелы или любые символы из переданной строки с начала и конца исходной строки
print(s.strip())  # "Hello, World! Hello!"
print(s.strip(" !,H"))  # "ello, World! Hello"

# count(sub[, start[, end]]) – возвращает количество неперекрывающихся вхождений подстроки
print(s.count("Hello"))  # 2
print(s.count("l"))      # 5

# index(sub[, start[, end]]) – возвращает индекс первого вхождения или вызывает ValueError, если не найдено
print(s.index("World"))  # 10
# print(s.index("Python"))  # ValueError, если раскомментировать

# replace(old, new[, count]) – заменяет все (или некоторые) вхождения подстроки
s2 = s.replace("World", "Python")  
print(s2)  # "  Hello, Python! Hello!  "

# замена с указанием количества (только первые две "l")
s3 = s.replace("l", "*", 2)
print(s3)  # "  He**o, World! Hello!  "

# split([sep]) – разбивает строку по пробелам (или указанному разделителю) в список
words = s.split()  # ['Hello,', 'World!', 'Hello!']
print(words)

# split с кастомным разделителем
csv = "apple,banana,grape"
print(csv.split(","))  # ['apple', 'banana', 'grape']

# join(iterable) – объединяет элементы последовательности, вставляя между ними строку-разделитель
joined = "-".join(["2025", "06", "03"])
print(joined)  # "2025-06-03"

# startswith(prefix[, start[, end]]) – проверяет, начинается ли строка с prefix
print(s.startswith("  He"))  # True

# endswith(suffix[, start[, end]]) – проверяет, заканчивается ли строка на suffix
print(s.endswith("!  "))  # True

# find(sub[, start[, end]]) – возвращает индекс первого вхождения подстроки или -1, если не найдено
print(s.find("World"))   # 9
print(s.find("Hello"))   # 2
print(s.find("Python"))  # -1

# Срезы (slices)
s = "Hello, Egor!"

print(s[0:5])      # 'Hello' — символы с 0 по 4
print(s[7:])       # 'Egor!' — с 7 до конца
print(s[:5])       # 'Hello' — с начала до 5
print(s[::2])      # 'Hlo go!' — каждый второй символ
print(s[::-1])     # '!rogE ,olleH' — строка в обратном порядке



# Расширенный пример format с именованными аргументами
template2 = "Coordinates: {lat}, {lon}"
print(template2.format(lat="55.7558° N", lon="37.6173° E"))  # "Coordinates: 55.7558° N, 37.6173° E"

# Строки в Python неизменяемы – при изменении создаётся новый объект
print(hex(id(s)))  # адрес в памяти до модификации
s = s.strip()
print(hex(id(s)))  # другой адрес после модификации (новый объект)


# format and f-string

name = "Egor"
last_name = "Tatarnikov"
language = "Python"

# вариант без format и f -строк
print("My name is " + name + " " + last_name + " and I code in " + language + ".")

# format
template = "My name is {} and I code in {}."
formatted = template.format(name + " " + last_name, language)
print(formatted)  # My name is Egor Tatarnikov and I code in Python.
# чаще пишут сразу так
print("My name is {} and I code in {}.".format(name + " " + last_name, language))

# f-string
print(f"My name is {name} {last_name} and I code in {language}.")


mile = 1609.344
print("Mile is {:.2f} kilometers".format(mile)) # ... 1609.34 ...
print(f"Mile is {mile:.2f} kilometers")         # ... 1609.34 ...


# Accumulating Lists and Strings

alist = [4, 2, 8, 6, 5]
blist = []
clist = []

# Добавляем к каждому элементу alist значение 5 и накапливаем в blist
for item in alist:
    blist.append(item + 5)
print(blist)

# Альтернативный способ накопления с использованием индексов
for i in range(len(alist)):
    clist.append(alist[i] + 5)
print(clist)


text = "hello"
new_text_1 = ""
new_text_2 = ""

# Накапливаем символы строки, преобразуя их в верхний регистр
for char in text:
    new_text_1 += char.upper()

print(new_text_1) # HELLO

# Альтернативный способ накопления с использованием индексов
for i in range(len(text)):
    new_text_2 += text[i].upper()

print(new_text_2) # HELLO

# Don’t Mutate A List That You Are Iterating Through
colors = ["Red", "Purple", "Yellow"]

"""
for i in range(len(colors)):    # IndexError: list index out of range
	if colors[i] == "Purple":
	    del colors[i]
	
print(colors)
"""

"""
Памятка. Это выглядит как многострочный комментарий,
но на самом деле это строка, которая просто никуда не присвоена.
Python её проигнорирует, если она не используется.
Для настоящих комментариев, которые гарантированно игнорируются интерпретатором, нужно использовать #
"""

# set – неупорядоченная коллекция уникальных элементов

# Создание множеств
a = {1, 2, 3}
b = set([3, 4, 5])
empty = set()  # пустое множество, а не словарь

# Добавление и удаление
a.add(4)         # добавить элемент
a.remove(2)      # удалить элемент (ошибка, если нет)
a.discard(10)    # удалить без ошибки, если элемента нет
a.clear()        # очистить множество
a.update([5, 6]) # добавить несколько элементов

# Операции с множествами
a = {1, 2, 3}
b = {3, 4, 5}

a | b    # объединение: {1, 2, 3, 4, 5} # or a.union(b)
a & b    # пересечение: {3}
a - b    # разность: {1, 2}
a ^ b    # симметрическая разность: {1, 2, 4, 5}

# Проверки
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True
print(b.issuperset(a)) # True
print(a.isdisjoint({3, 4}))  # True – нет общих элементов

# Перебор множества
for item in a:
    print(item)

# Преобразование
lst = list(set([1, 2, 2, 3]))  # удаление дубликатов из списка

# Пример использования
words = ["apple", "banana", "apple", "cherry"]
unique_words = set(words)
print(len(unique_words))  # 3










# ============================================================
# 2. Python Functions, Files, and Dictionaries
# ============================================================

    # ___ Files ___#
    
    # File Path Examples

# 'example.txt'        – файл в текущей директории
# './example.txt'      – то же самое: текущая директория
# 'files/data.txt'     – файл в подпапке 'files'
# './files/data.txt'   — то же самое, что 'files/data.txt'
# '../data.txt'        – файл на один уровень выше
# '../files/data.txt'  – файл в папке 'files', которая находится уровнем выше
# '/home/user/file.txt'  – абсолютный путь (Linux/macOS)
# 'C:\\Users\\User\\file.txt'  – абсолютный путь (Windows, экранированные слэши)
# r'C:\Users\User\file.txt'  – абсолютный путь (Windows, raw-строка без экранирования)


    # File Open Modes
    
my_file =  open('./python_summary_files/example_read.txt', 'r', encoding='utf-8')   
print(my_file.read())
print(len(my_file.read()))  # 0 - выводит 0 потому что файл уже прочитан
my_file.seek(0)
print(len(my_file.read()))  # 485
my_file.seek(0)
print(len(my_file.readlines()))
my_file.seek(0)
#for line in my_file.readlines():   # без разницы
for line in my_file:                #   можно и так
    print(line, end='')             # не добавляем лишний \n
my_file.close()

filename = "./python_summary_files/squared_numbers.txt"
outfile = open(filename, "w")
for number in range(1, 10):
    square = number * number
    outfile.write(str(square) + "\n")
outfile.close()

infile = open(filename, "r")
print(infile.read())
infile.close()

# Using with for Files
# Конструкция with автоматически закрывает файл после завершения блока
# и визуально отделяет блок работы с файлом
# Это предпочтительный способ работы с файлами

# 'r' – read (Чтение. Ошибка, если файл не существует)
# 'utf-8' – универсальная кодировка, которая поддерживает русский, английский и большинство других языков.
# Рекомендуется всегда указывать encoding.
with open('python_summary_files/example_read.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 'w' – write (Перезаписывает файл. Создаёт, если не существует)
with open('./python_summary_files/example_write.txt', 'w', encoding='utf-8') as file:
    file.write('Новая строка\n')

# 'a' – append (Добавляет в конец файла. Создаёт, если не существует)
with open('./python_summary_files/example_append.txt', 'a', encoding='utf-8') as file:
    file.write('Добавленная строка\n')

# 'x' – exclusive creation (Создаёт новый файл. Ошибка, если уже существует.
# with open('./python_summary_files/example_create.txt', 'x', encoding='utf-8') as file:
#     file.write('Создаём файл впервые')

# 'r+' – чтение + запись (Ошибка, если файл не существует)
with open('./python_summary_files/example_read_write.txt', 'r+', encoding='utf-8') as file:
    old_content = file.read()
    file.seek(0)  # переместиться в начало файла
    file.write('Новое начало\n' + old_content)

# 'w+' – запись + чтение (Перезаписывает файл или создаёт)
with open('./python_summary_files/example_write_read.txt', 'w+', encoding='utf-8') as file:
    file.write('Сначала запись\n')
    file.seek(0)
    print(file.read())  # Считаем то, что только что записали

# 'a+' – добавление + чтение (Создаёт файл, если не существует)
with open('./python_summary_files/example_append_read.txt', 'a+', encoding='utf-8') as file:
    file.write('Строка для добавления\n')
    file.seek(0)
    print(file.read())  # Покажет весь файл, включая добавленное

# 'rb' – чтение в бинарном режиме
with open('./python_summary_files/example_binary.jpg', 'rb') as file:
    binary_data = file.read()
    print(type(binary_data))  # <class 'bytes'>

# 'wb' – запись в бинарном режиме
with open('./python_summary_files/example_copy.jpg', 'wb') as file:
    file.write(binary_data)
    
    
    # File Object Methods
    
# write(astring) – записывает строку в файл
with open('./python_summary_files/methods_write.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!\n')
    file.write('Это вторая строка.\n')

# read(n) – читает n символов или весь файл, если n не указан
with open('./python_summary_files/methods_write.txt', 'r', encoding='utf-8') as file:
    full_text = file.read()  # читаем всё
    print(full_text)

# readline() – читает одну строку (до \n)
with open('./python_summary_files/methods_write.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    print('Первая строка:', first_line)

# readlines() – читает все строки в список
with open('./python_summary_files/methods_write.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print('Список строк:', lines)

# writelines(list_of_strings) – записывает список строк в файл
lines_to_write = ['строка 1\n', 'строка 2\n', 'строка 3\n']
with open('./python_summary_files/methods_writelines.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

# seek(offset) – перемещает указатель позиции (в байтах)
with open('./python_summary_files/methods_write.txt', 'r', encoding='utf-8') as file:
    file.seek(4)  # перейти на 4-й байт
    print(file.read(10))  # читаем 10 символов с позиции 5

# tell() – показывает текущую позицию указателя
with open('./python_summary_files/methods_write.txt', 'r', encoding='utf-8') as file:
    file.seek(4)  # перейти на 4-й байт
    print('Позиция в начале:', file.tell())                 # 4
    file.read(7)
    print('Позиция после чтения 7 символов:', file.tell())  # 16, потому что в 'utf-8' буквы - 2 байта, а ',' и ' ' - 1 байт

# flush() – принудительно записывает буфер в файл (обычно используется с 'w')
with open('./python_summary_files/methods_flush.txt', 'w', encoding='utf-8') as file:
    file.write('Буфер записан.\n')
    file.flush()  # полезно при долгой работе с файлами
    
# Если файл большой, лучше читать его построчно в цикле:
with open('./python_summary_files/bigfile.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip удаляет \n в конце строки
      


    # ___ Работа с CSV файлами в Python ___ #

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing, 1500m"), # csv.writer бере
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

writer = open("./python_summary_files/my_file.csv", 'w')
for olympian in olympians:
    writer.write(f"{olympian[0]},{olympian[1]},{olympian[2]}")
    writer.write('\n')
writer.close()
  

import csv

csvfile = open("./python_summary_files/my_file.csv", 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow(['Name', 'Age', 'Sport'])
for olympian in olympians:
    writer.writerow(olympian)
csvfile.close()

# Пример 1: чтение CSV как список списков
with open('python_summary_files/data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # ['name', 'age'], затем ['Egor', '32'], ['Anna', '28']

# Пример 2: чтение CSV как словари
with open('python_summary_files/data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])  # Egor 32, затем Anna 28

# Пример 3: запись в CSV (список списков)
# newline='' в open() предотвращает появление лишних пустых строк в CSV-файле. Это касается только записи. 
with open('python_summary_files/output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'age'])      # заголовки
    writer.writerow(['Egor', 32])         # строка 1
    writer.writerow(['Anna', 28])         # строка 2
# output.csv будет выглядеть так:
# name,age
# Egor,32
# Anna,28

# Пример 4: запись в CSV (список словарей)
with open('python_summary_files/output_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Egor', 'age': 32})
    writer.writerow({'name': 'Anna', 'age': 28})
# output_dict.csv будет иметь такой же результат, но создан с использованием словарей



    # ___ Dictionaries ___ #

# Словарь — это изменяемая структура данных, где значения хранятся в паре ключ:значение
# ключом в словаре может быть только неизменяемый объект

# Создание словаря
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Доступ к значениям
print(person["name"])  # Alice

# Добавление и изменение элементов
person["job"] = "Engineer"
person["age"] = 31

# Удаление элементов
del person["city"]         # Удаление по ключу
print(person.pop("job"))   # Возврат и удаление значения (Engineer)

print(person)   # {'name': 'Alice', 'age': 31}


# Получение значения
print(person.get('age'))    # 31
print(person.get('job'))    # None
# Безопасное получение значения
print(person.get("city", "Not found"))  # Вернет "Not found", если ключа нет

# Проверка наличия ключа
print('age' in person)  # True

if "name" in person:
    print("Name is present")
else:
    print("There is no name")
    
# Получение всех ключей, значений и пар
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 31])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 31)])

# list() — это встроенная функция в Python, преобразует переданный ей объект в список, если это возможно.
print(list(person.keys()))      # ['name', 'age']
print(list(person.values()))    # ['Alice', 31]
print(list(person.items()))     # [('name', 'Alice'), ('age', 31)]

#print(person.keys()[0])        # TypeError
print(list(person.keys())[0])   # name
# Очистка словаря
#person.clear()
#print(person)   # {}

# Копирование словаря
wrong_copy = person
print(hex(id(person)))      # 0x2a61d957980
print(hex(id(wrong_copy)))  # 0x2a61d957980 - скопировали только ссылку на словарь
person_copy = person.copy()
print(hex(id(person)))      # 0x2a61d957980
print(hex(id(person_copy))) # 0x2a61da10400 - адрес поменялся

# Объединение словарей (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2 
print(merged) # {'a': 1, 'b': 2}

# Итерация по словарю

# По ключам
for key in person.keys():
    print(f"Key: {key}, Value: {person[key]}")
# можно и так, то же самое
for key in person:
    print(f"Key: {key}, Value: {person[key]}")
    
# По значениям
for value in person.values():
    print(f"Value: {value}")

# По парам ключ-значение
for key, value in person.items():
    print(f"{key} -> {value}")
    
# Пример: подсчёт частоты символов
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1  # если буквы еще нет, создает новый ключ, возвращает 0 и прибавляет 1, 
                                        # если буква уже есть возвращает сколько уже насчитал и прибавляет 1
print(freq)  # {'b': 1, 'a': 3, 'n': 2}

text = "London is the capital of the United Kingdom"
dict_char = {}
for c in text:
    if c not in dict_char:
        dict_char[c] = 0
    dict_char[c] += 1
print(dict_char)

dict_words = {}
for word in text.split():
    if word not in dict_words:
        dict_words[word] = 0
    dict_words[word] += 1
print(dict_words)



# Работа с CSV-файлами через DictReader и DictWriter
import csv

# Чтение CSV через DictReader
# Каждая строка файла превращается в словарь: ключи — из заголовков CSV

with open('./python_summary_files/data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # пример: {'name': 'Alice', 'age': '30'}

# апись в CSV через DictWriter
# Сначала указываем список полей (заголовков)

fieldnames = ['name', 'age', 'city']
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'London'}
]

with open('./python_summary_files/output.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()        # Запись заголовков
    writer.writerows(data)      # Запись всех строк сразу
    # Или:
    # for row in data:
    #     writer.writerow(row)

# Полезно знать
# - DictReader автоматически преобразует первую строку файла в ключи словаря
# - DictWriter требует вручную указать fieldnames
# - Используйте newline='' при работе с файлами на Windows
# - Все значения читаются как строки — для чисел нужна дополнительная обработка



    # ___ Functions ___#

# The syntax for creating a named function, a function definition, is:
# def name(parameters):
#     """documentation"""   # необязательно
#     statements
#     return result
# параметры и return необязательны. Если return нет возвращается None

# A type annotation
def add(x: int, y: int) -> int:         # A type annotation. Показывает какие данные должны быть переданы в функцию 
                                        # и какие она возвращает. Не обязательна к исполнению.
    """Returns the sum of `x` and `y`"""
    return x + y

# Локальные и глобальные переменные
power = 2                   # power - глобальная переменная
def my_square(x):           # x - локальная переменная
    y = x ** power          # можно ссылаться на глобальные переменные. так делать плохо, но можно
                            # к примеру можно сослаться на констану.
    return y

def my_power(x, power):     # x, power - локальные переменные
    y = x ** power          # сначала пайтон будет искать локальные переменные, а если не найдет - глобальные
    return y

print(my_square(10))    # 100
print(my_power(10,3))   # 1000


    # Passing Mutable Objects
# В Python переменные — это ссылки на объекты.
# Мы не можем изменить саму переменную (ссылку), переданную в функцию,
# но можем изменить содержимое изменяемого объекта (например, список, словарь и т.д.).

# Пример с изменяемым объектом:
def modify_list(lst):   # локальная переменная lst ссылается на тот же список, что и глобальная my_list.
    lst.append(42)      # меняется сам объект

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 42] — список изменился
modify_list(list(my_list))  # list() делаем копию списка
print(my_list)  # [1, 2, 3, 42] — список неизменился

# Пример с неизменяемым объектом:
def try_modify(x):
    x += 10  # создаётся новый объект, исходный не меняется

a = 5
try_modify(a)
print(a)  # 5 — переменная a осталась без изменений

# Пример с изменяемым объектом (нюанс):
def changeit(lst):
    lst = ["Michigan", "Wolverines"]  # создаётся НОВЫЙ список и локальная переменная lst нереназначается на него.

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)  # ['our', 'students', 'are', 'awesome']


# Параметр (parameter) - это имя переменной, указанное в определении функции.
#                       A name used inside a function to refer to the value which was passed to it as an argument.
# Аргумент (argument) — это конкретное значение, которое передаётся функции при вызове.
#                       A value provided to a function when the function is called.



    # Проверка функций с помощью assert

# Проверка типов с помощью assert
def greet(name):
    # assert type(name) == str, "Аргумент 'name' должен быть строкой"
    # assert isinstance(name, str), "Аргумент 'name' должен быть строкой"
    # лучше использовать isinstance(name, str), так как он поддерживает наследование. То есть наследующие объекты тоже пройдут проверку
    print(f"Привет, {name}!")

greet("Егор")      # OK
greet(123)         # AssertionError: Аргумент 'name' должен быть строкой


# Проверка вывода функции через assert
def square(x):
    return x*x
# граничные случаи и любой другой
assert square(1) == 1
assert square(0) == 0
assert square(-1) == 1
assert square(3) == 9

# проверка изменения функцией изменяемых объектов через assert
def update_counts(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c] += 1
        else:
            counts_d[c] = 1
            
counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)

assert counts['a'] == 6  # было 3, добавили ещё 3
assert counts['b'] == 3  # было 2, добавили 1

# Testing Optional Parameters
def count_long_words(words, min_length=5):
    ct = 0
    for word in words:
        if len(word) >= min_length:
            ct += 1
    return ct

test_words = ["", "1", "12", "123", "1234", "12345", "123456"]
assert count_long_words(test_words) == 2
assert count_long_words(test_words, min_length=0) == 7
assert count_long_words(test_words, min_length=4) == 3
assert count_long_words(test_words, min_length=100) == 0

    # Test Driven Development
# При написании сложных функиций можно сначала написать тест-кейсы через assert, а затем реализовывать функцию
# 2. Затем реализуем функцию, чтобы проходила все тесты
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

# 1. Сначала прописываем разные известные или граничные случаи
assert distance(1,2, 1,2) == 0
assert distance(3,4, 3,5) == 1
assert distance(3,4, 5,4) == 2
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) == 2**0.5


    # Optional Parameters

# Опциональные параметры — это параметры со значениями по умолчанию.
# Они задаются в определении функции, например:
# def func(x, y=10, z=0): - сначала обязательные, потом опциональные.

# ----------------------------------------------------------
# Важно 1: значения по умолчанию вычисляются ОДИН РАЗ —
# во время определения функции, а не при каждом вызове.
# Пример 1. Значения по умолчанию (y=3, z=initial) запоминаются во время определения функции, а не во время её вызова.
# То есть z=initial означает z=7, потому что initial в тот момент был равен 7.
# Даже если позже ты переопределяешь initial = 10, значение по умолчанию z уже стало 7 и не меняется.
initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

initial = 10
f(2)    # x, y, z, are: 2, 3, 7

# Важно 2: изменяемые значения по умолчанию (например, списки)
# сохраняются между вызовами функции. Это может вызвать баги.
# пример 2: Значение аргумента L=[] создаётся один раз при определении функции, и сохраняется между вызовами.
# Поэтому L в первых трёх вызовах — это один и тот же список, который постепенно накапливает [1, 2, 3].
# В f(4, ["Hello"]) и f(5, ["Hello"]) ты передаёшь новые списки вручную, поэтому там всё ожидаемо.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))                  # [1]
print(f(2))                  # [1, 2]
print(f(3))                  # [1, 2, 3]
print(f(4, ["Hello"]))       # ['Hello', 4]
print(f(5, ["Hello"]))       # ['Hello', 5]

# как решить
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Использование именованных аргументов
def introduce(name, age=29, city="Москва"):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

introduce("Егор")                           # Имя: Егор, Возраст: 29, Город: Москва
introduce("Егор", 30, "Королев")            # Имя: Егор, Возраст: 30, Город: Королев
introduce("Егор", city="Королев")           # Имя: Егор, Возраст: 29, Город: Королев
introduce("Егор", city="Королев", age=30)   # Имя: Егор, Возраст: 30, Город: Королев
#introduce(city="Королев", age=30", Егор")  # SyntaxError: invalid syntax.


    # Для справки! Ограничения на передачу аргументов 
# Только позиционные параметры (слева от "/")
# Только именованные параметры (справа от "*")
# Между ними — обычные: можно и так, и так
def example(pos1, pos2, /, both, *, kw1, kw2):
    print(f"pos1 = {pos1}, pos2 = {pos2}")
    print(f"both = {both}")
    print(f"kw1 = {kw1}, kw2 = {kw2}")

example(1, 2, both=3, kw1=4, kw2=5)             # Правильно
# example(pos1=1, pos2=2, both=3, kw1=4, kw2=5) # TypeError: pos1 и pos2 должны быть переданы позиционно
# example(1, 2, 3, 4, 5)                        # TypeError: kw1 и kw2 нужно передавать по имени


    # ___ Использование кортежей в функциях и циклах ___ #
    
# Присваивание нескольких значений через кортеж
tup = (13, 46)
atup, btup = tup        # распаковка кортежа (слева и справа кортежи одинаковой длины)
print('atup:', atup, ', \
btup:', btup)          # atup: 13 , btup: 46

alist, blist = [3, 4]   # распаковка оказывается работает и с другими типами данных. лист
print('alist:', alist, ', \
blist:', blist)        # alist: 3 , blist: 4

adict, bdict = {'Name': 'Egor', 'Age': 30}   # словарь
print('adict:', adict, ', \
bdict:', bdict)        # adict: Name , bdict: Age

astr, bstr = 'hi'       # строка
print('astr:', astr, ', \
bstr:', bstr)          # astr: h , bstr: i

# Использование Кортежей в циклах
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for p_nm, p_nb in pokemon.items():
    p_names.append(p_nm)
    p_number.append(p_nb)
print(p_names)    
print(p_number)    

p_names2 = []
for pokemon in pokemon.items():
    p_names2.append(pokemon[0])
print(p_names2)

# Возврат нескольких значений через кортеж
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))       # (62.8318, 314.159)

circumference, area = circleInfo(1)
print(circumference, area)  # 6.28318 3.14159

# Передача аргументов в функцию в виде кортежа
def add(x, y):
    return x + y

print(add(3, 4))    # 7 
z = (5, 4)
#print(add(z))      # TypeError: add() missing 1 required positional argument: 'y'
print(add(*z))      # 9. * - используется для распаковки кортежей



    # ___ Цикл While ___ #
    
# Цикл While используют:
# - Если не известно число итераций заранее.
import random
x = 0
i = 0
while x != 5:
    x = random.randint(0, 9)
    i +=1
    print('iter:', i, ' x:', x)
print('Done')

# - При ожидании ввода или события.
password = ""
while password != "secret":
    password = input("Введите пароль (подсказка: секрет по-английски): ")
print("Доступ разрешен")

# В while-loop можно сделать все то же самое, что и в for-loop
eve_nums = []
i = 0
while i < 15:   # Цикл while выполняет блок кода, пока условие истинно (True).
    if i % 2 == 0:
        eve_nums.append(i)
    i += 1
print(eve_nums) # [0, 2, 4, 6, 8, 10, 12, 14]

eve_nums = []
i = 0
for i in range(15):
    if i % 2 == 0:
        eve_nums.append(i)
print(eve_nums) # [0, 2, 4, 6, 8, 10, 12, 14]

# break and continue
lst = []
x = 0
while True:         #  while True: - бесконечный цикл
    x += 1
    if x % 3 == 0:
        continue    # continue переводит на следующую итерацию
    if x > 10:
        break       # break прекращает выполнение цикла
    lst.append(x)

print(lst) # [1, 2, 4, 5, 7, 8, 10]

def sublist(lst):
    sl = []
    item = 0
    while item < len(lst):
        if lst[item] == 5:
            break
        sl.append(lst[item])
        item += 1
    return sl


print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print(sublist([5]))
print(sublist([8, 6, 5]))
print(sublist([1, 6, 2, 3, 9]))



    # Лямбда-функции

# Лямбда — это компактная, безымянная функция, задаётся через ключевое слово lambda.
# Синтаксис:
# lambda arguments: expression
def func(args):
    return value

func = lambda args: value

# Функция, определённая через def
def f(x):
    return x - 1

print(f)                        # <function f at 0x...> — ссылка на функцию f
print(type(f))                  # <class 'function'>
print(f(3))                     # 2 — вызов функции f

# Анонимная (лямбда) функция:
print(lambda x: x - 1)          # <function <lambda> at 0x...> — тоже функция
print(type(lambda x: x - 1))    # <class 'function'>
print((lambda x: x - 1)(3))     # 2 — вызов лямбда-функции

# Лямбда-функция, сохранённая в переменной
func = lambda x: x - 1

print(func)                     # <function <lambda> at 0x...>
print(type(func))               # <class 'function'>
print(func(3))                  # 2

# Оба способа создают объект типа <function>
# Оба работают одинаково при вызове
# def → для создания именованных, многострочных функций
# Лямбда-функция не имеет имени и предназначена для простых, анонимных выражений (например, в map, filter, sorted)
# Лямбда-функцию присваивают переменной, если нужно компактно описать простую операцию.



    # Обёрточные функции и декораторы: пример с защитой по паролю

# Декоратор: принимает функцию и возвращает обёрнутую версию
def passwordProtect(func):
    def wrappedFunc():
        password = input("Enter the password to call the function: ")

        if password == "password123":
            func()  # вызываем исходную функцию
        else:
            print("Access denied. Sorry")

    return wrappedFunc

# Вариант без синтаксиса @
def printMessage():
    print("Секретное сообщение")

protectedPrint = passwordProtect(printMessage)  # Оборачиваем вручную
protectedPrint()

# Вариант с использованием @decorator 
@passwordProtect    # это означает, что следующая функция будет обернута в passwordProtect
def printMessage2():
    print("Это вторая защищённая функция")

printMessage2()     # при вызове printMessage2() на самом деле вызывается passwordProtect(printMessage2)



    # ___ Функция sorted() и метод .sort() в Python ___

# sorted() — встроенная функция
# работает с любыми итерируемыми объектами (список, строка, кортеж и т.д.)
# возвращает новый отсортированный объект
# не меняет оригинальный

nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4]
print(sorted(nums)) # [1, 2, 3, 4]
print(nums)         # [3, 1, 4, 2] — не изменился

# .sort() — метод списка
# работает только со списками
# сортирует **на месте** (in-place)
# ничего не возвращает (возвращает None)

nums.sort()
print(nums)         # [1, 2, 3, 4]
print(nums.sort())  # None

# Оба способа поддерживают опциональные парамтры:
# - reverse=True — сортировка по убыванию
# - key= — функция, по которой сравниваются элементы

# Пример с reverse=True 
words = ['apple', 'banana', 'kiwi', 'lemon', 'pear', 'pineapple']
print(sorted(words, reverse=True))  # ['pineapple', 'pear', 'lemon', 'kiwi', 'banana', 'apple']
words.sort(reverse=True)
print(words)                        # ['pineapple', 'pear', 'lemon', 'kiwi', 'banana', 'apple']

# Пример с key=
# В key мы передаём функцию (или lambda), в которую будет подставляться каждый элемент объекта 
# и сравниваться при сортировке будут уже возвращаемые величины
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)                # ['pear', 'kiwi', 'lemon', 'apple', 'banana', 'pineapple']

# Сортировка по нескольким критериям:
# Что делает lambda x: (-len(x), x):
# - сначала сортирует по длине слова len(x) по убыванию (минус перед len)
# - если длины слов одинаковые, сортирует по алфавиту (второй элемент кортежа)
sorted_by_len = sorted(words, key=lambda x: (-len(x), x)) 
print(sorted_by_len)                # ['pineapple', 'banana', 'apple', 'lemon', 'kiwi', 'pear']


    # ___ Сортировка словарей в Python (Sorting a Dictionary) ___

# Словари (dict) в Python по умолчанию не упорядочены по значению ключей,
# но их можно отсортировать по ключам или значениям.

# Сортировка словаря = сортировка списка кортежей (key, value) через data.items() и sorted()

data = {'apple': 5, 'banana': 2, 'pear': 8, 'grape': 3}

# Сортировка по ключам (по алфавиту)
sorted_by_keys = dict(sorted(data.items())) # dict() обратно превращает список кортежей в словарь
print(sorted_by_keys)       # {'apple': 5, 'banana': 2, 'grape': 3, 'pear': 8}

# Сортировка по значениям (по возрастанию)
sorted_by_values = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_by_values)     # {'banana': 2, 'grape': 3, 'apple': 5, 'pear': 8}

# Сортировка по нескольким критериям:
# 1) по значению (по убыванию)
# 2) по ключу (по алфавиту)
data2 = {'apple': 5, 'banana': 2, 'pear': 8, 'grape': 3}

sorted_multi = dict(sorted(data2.items(), key=lambda x: (-x[1], x[0])))
print(sorted_multi)
# {'apple': 5, 'banana': 5, 'pear': 5, 'grape': 3}

# Если нужно получить отсортированный список ключей/значений:
print(sorted(data.keys()))     # ['apple', 'banana', 'grape', 'pear']
print(sorted(data.values()))  # [2, 3, 5, 8]

# Пример
dictionary = {"Flowers": 10, 'Trees': 6, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 22}
# по ключам
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
sorted_dict = dict(sorted(dictionary.items())) # то же самое
print(sorted_dict)  # {'Chairs': 6, 'Firepit': 1, 'Flowers': 10, 'Grill': 2, 'Lights': 22, 'Trees': 6}
# по значениям
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(sorted_dict)  # {'Firepit': 1, 'Grill': 2, 'Trees': 6, 'Chairs': 6, 'Flowers': 10, 'Lights': 22}
# сначала по значениям, потом по ключам
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0])))
print(sorted_dict)  # {'Firepit': 1, 'Grill': 2, 'Chairs': 6, 'Trees': 6, 'Flowers': 10, 'Lights': 22}

# список ключей по алфавиту
sorted_keys = sorted(dictionary.keys())
print(sorted_keys)          # ['Chairs', 'Firepit', 'Flowers', 'Grill', 'Lights', 'Trees']
# список значений по возрастанию
sorted_values = sorted(dictionary.values())
print(sorted_values)        # [1, 2, 6, 6, 10, 22]
# список ключей по возрастанию значений. 
# по умолчанию сортировка идет по ключам, т.е. вместо х подставляются ключи, dictionary[x] - значения
sorted_keys_by_value = sorted(dictionary, key=lambda x: dictionary[x])
print(sorted_keys_by_value) # ['Firepit', 'Grill', 'Trees', 'Chairs', 'Flowers', 'Lights']










# ============================================================
# 3. Data Collection and Processing with Python
# ============================================================

    # Nested Data (вложенные структуры данных) в Python

# Вложенные данные — это структуры данных, содержащие другие структуры:
# списки в списках, словари в словарях, списки в словарях и т.д.

# ▶ Примеры вложенных структур:

# Список списков:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Словарь списков:
student_scores = {
    "Alice": [85, 90, 95],
    "Bob": [78, 82, 88]
}

# Список словарей:
users = [
    {"id": 1, "name": "Egor"},
    {"id": 2, "name": "Yeva"}
]

# Словарь словарей:
user_profiles = {
    "egor": {"age": 30, "city": "Korolev"},
    "yeva": {"age": 25, "city": "Moscow"}
}

# ▶ Доступ к данным:

# Элемент во вложенном списке:
element = matrix[1][2]  # 6

# Оценка Боба:
score = student_scores["Bob"][1]  # 82

# Имя второго пользователя:
name = users[1]["name"]  # "Yeva"

# Город Егора:
city = user_profiles["egor"]["city"]  # "Korolev"


# ▶ Итерация по вложенным структурам:

# Перебор матрицы:
for row in matrix:
    for value in row:
        print(value)

# Перебор списка словарей:
for user in users:
    print(user["name"])

# Перебор списка списков:
nested = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

# Пример 1 : список с разным уровнем вложенности
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

# Пример 2 : список с разным уровнем вложенности (любой сложности)  
data = [
    1,
    [2, 3],
    [[4, 5], 6],
    7,
    [[[8]]]
]

def iterate_nested(lst):
    for item in lst:
        if isinstance(item, list):
            # если элемент — список, рекурсивно итерируем внутри
            yield from iterate_nested(item)
        else:
            yield item

for value in iterate_nested(data):
    print(value, end=' ')
print()


# ▶ Изменение вложенных данных:

# Изменим значение:
matrix[0][1] = 42
users[0]["name"] = "Yegor"

# ▶ Практические приёмы:

# Добавление элемента:
student_scores["Alice"].append(100)

# Проверка существования ключа:
if "egor" in user_profiles:
    print(user_profiles["egor"]["age"])




    # *args и **kwargs в Python

# знаки * и ** в пайтоне используются для распаковки аргументов при вызове функций
# * — распаковывает итерируемый объект (список, кортеж, строку и т.п.). Передаёт его элементы как позиционные аргументы.
# ** — распаковывает словарь. Передаёт его пары ключ=значение как именованные аргументы.
# ▶ Распаковка аргументов:
numbers = [10, 20, 30]
params = {"sep": " | "}
print(*numbers, **params)  # 10 | 20 | 30

# ▶ *args — собирает произвольное количество позиционных аргументов в кортеж
# *args — нужен, чтобы передавать любое количество позиционных аргументов в функцию.
# Полезно, когда ты не знаешь заранее, сколько аргументов будет передано.
def example_args(*args):
    print(args)

example_args(1, 2, 3)  # (1, 2, 3)

# ▶ **kwargs — собирает произвольное количество именованных аргументов в словарь
# **kwargs — нужен, чтобы передавать любое количество именованных аргументов (в виде ключ=значение).
# Удобно для настройки параметров или прокидывания аргументов в другие функции
def example_kwargs(**kwargs):
    print(kwargs)

example_kwargs(name="Egor", age=30)  # {'name': 'Egor', 'age': 30}

# ▶ Использование вместе:
def example_all(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example_all(1, 2, name="Yeva", job="AI")  
# args: (1, 2)
# kwargs: {'name': 'Yeva', 'job': 'AI'}




    #  Работа с JSON в Python (модуль json)

# JSON (JavaScript Object Notation) — текстовый формат хранения структурированных данных.
# Широко используется для обмена данными между приложениями, особенно в API и веб-разработке.

# Пример JSON:
# {
#     "name": "Egor",
#     "age": 30,
#     "skills": [
#         "Python", 
#         "Machine Learning"
#     ]
# }

# Модуль json (встроенный модуль Python) нужен для работы с форматом JSON
import json

# Основные функции: 
# dump, dumps - Конвертация Python-объектов в JSON (сериализация)
# load, loads -  Парсинг JSON-строк в Python-объекты (десериализация)

# 🔹 Функция json.dumps(obj, **kwargs)
# Преобразует Python-объект (словарь, список и т.д.) в JSON-строку (str).

data = {
    "name": "Egor",
    "age": 30,
    "skills": ["Python", "Data Science"]
}

json_string = json.dumps(data)
print(json_string)  # '{"name": "Egor", "age": 30, "skills": ["Python", "Data Science"]}'

# С отступами и читаемым форматом:
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)    
# indent добавляет отступы. Без этого параметра JSON будет в одной строке
# ensure_ascii=False - Unicode (в том числе русские) символы сохранятся в читаемом виде, а не в в \uXXXX
print(pretty_json)
# {
#     "name": "Egor",
#     "age": 30,
#     "skills": [
#         "Python", 
#         "Machine Learning"
#     ]
# }

# --------------------------------------------
# 🔹 Функция json.loads(json_string)
# Преобразует JSON-строку обратно в Python-объект.

parsed_data = json.loads(json_string)
print(parsed_data["name"])  # "Egor"

# --------------------------------------------
# 🔹 Функция json.dump(obj, file, **kwargs)
# Записывает Python-объект в файл в формате JSON.

with open("./python_summary_files/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# --------------------------------------------
# 🔹 Функция json.load(file)
# Считывает JSON из файла и возвращает Python-объект.

with open("./python_summary_files/data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data["skills"])

# --------------------------------------------
# 🔹 Таблица соответствия типов данных:

# Python тип          →  JSON тип           →  Пример Python          →  Пример JSON
# ------------------------------------------------------------------------------
# dict                →  объект (object)     →  {"key": "value"}       →  { "key": "value" }
# list, tuple         →  массив (array)      →  [1, 2, 3]              →  [1, 2, 3]
# str                 →  строка (string)     →  "Hello"                →  "Hello"
# int, float          →  число (number)      →  42, 3.14               →  42, 3.14
# True                →  true                →  True                   →  true
# False               →  false               →  False                  →  false
# None                →  null                →  None                   →  null
# --------------------------------------------

# Важные моменты:
# - Ключи словаря (dict) должны быть строками, иначе при сериализации будет ошибка.
#   Например, {10: "val"} вызовет ошибку при сериализации.
# - Кортежи (tuple) сериализуются как списки JSON.
# - Неподдерживаемые типы (например, set, объекты классов) требуют кастомной сериализации.




    # Deep and Shallow Copies

# 🔹 Поверхностное копирование (shallow copy):
# Копируется только верхний уровень объекта.
# Вложенные объекты остаются ссылками на те же самые данные.

import copy

original = [[1, 2], [3, 4]]     # В памяти создаётся внешний список и два вложенных списка.
shallow = copy.copy(original)   # поверхностная копия (shallow). Создается новый внешний список, но внутренние списки остаются общими (указывают на те же объекты)
shallow_2 = original[:]         # тоже способ поверхностного копирования. Срез копирует только верхний уровень

original[0][0] = 99             # Меняется первый элемент первого вложенного списка. Этот вложенный список общий для всех копий → изменение отразится везде.
shallow_2[1] = [10, 11]         # Мы заменяем второй вложенный список в shallow_2. Это разрывает связь с original[1] → теперь shallow_2[1] указывает на новый список, независимый.
print(original)                 # [[99, 2], [3, 4]] - изменился оригинал
print(shallow)                  # [[99, 2], [3, 4]] - и копия
print(shallow_2)                # [[99, 2], [10, 11]] - вторая вложенность заменена, первая всё ещё ссылается на общий объект

# 🔹 Глубокое копирование (deep copy):
# Копируются все уровни, включая вложенные объекты.
# Результат — полностью независимая копия.

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)  # глубокая копия (deep)

deep[0][0] = 99
print(original)                 # [[1, 2], [3, 4]] — оригинал не изменился




    # Map, Filter, List Comprehensions, and Zip

# --- Функция map() ---
# Сигнатура: map(function, iterable)
# Применяет функцию к каждому элементу списка и возвращает ИТЕРАТОР (не список!)
# Чтобы увидеть результат — нужно обернуть в list()

nums = [1, 2, 3, 4]

# Пример 1: lambda-функция
print(list(map(lambda x: 2 * x, nums)))  # [2, 4, 6, 8]

# Пример 2: именованная функция
def double(x):
    return x * 2

print(list(map(double, nums)))          # [2, 4, 6, 8]

# Без map — тот же эффект вручную:
def doubleStuff(a_list):
    new_list = []
    for value in a_list:
        new_elem = double(value)
        new_list.append(new_elem)
    return new_list

print(doubleStuff(nums))                # [2, 4, 6, 8]


# --- Функция filter() ---
# Сигнатура: filter(function, iterable)
# Возвращает итератор из элементов, для которых функция возвращает True.
# Чтобы увидеть результат — нужно обернуть в list()

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 
             'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
print(list(filter(lambda x: 'B' in x, countries)))  # ['Brazil', 'Botswana', 'Britain', 'Belarus', 'Belgium']

nums = [1, 2, 3, 4, 5]

# Пример 1: lambda-функция
print(list(filter(lambda x: x % 2 != 0, nums)))  # [1, 3, 5]

# Пример 2: именованная функция
def is_odd(x):
    return x % 2 != 0

print(list(filter(is_odd, nums)))                # [1, 3, 5]

# Без filter — вручную:
def filter_odds(a_list):
    result = []
    for x in a_list:
        if is_odd(x):
            result.append(x)
    return result

print(filter_odds(nums))                         # [1, 3, 5]


# --- Функция zip() ---
# Сигнатура: zip(iter1, iter2, ...)
# Объединяет элементы из нескольких списков в кортежи
# Чтобы увидеть результат — нужно обернуть в list()

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# Пример 1: объединение списков
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Пример 2: распаковка
zipped = list(zip(names, ages))
print(zipped)                   # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# * перед zipped распаковывает список кортежей в отдельные аргументы: zip(('Alice', 25), ('Bob', 30), ('Charlie', 35))
# затем zip(...) группирует по позициям внутри кортежей:
print(list(zip(*zipped)))   # [('Alice', 'Bob', 'Charlie'), (25, 30, 35)]
# далее кортеж списков распаковывается в unzipped_names, unzipped_ages
unzipped_names, unzipped_ages = zip(*zipped)
print(unzipped_names)          # ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)           # (25, 30, 35)

# Пример 3: списки разной длины
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))         # [(1, 'a'), (2, 'b')]

# Без zip — вручную:
def manual_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result

print(manual_zip(a, b))        # [(1, 'a'), (2, 'b')]


# --- List Comprehension ---
# полностью заменяет map и filter
# Сигнатура: [expression for item in iterable if condition (опционально)]
# Возвращает List

# Пример 1: квадраты чисел
print([x**2 for x in range(5)])          # [0, 1, 4, 9, 16]

# Пример 2: только чётные
print([x for x in range(10) if x % 2 == 0])  # [0, 2, 4, 6, 8]

# Пример 3 с zip 
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x + y for (x, y) in list(zip(L1, L2)) if (x > 10 and y < 5)]
print(L3)   # [18, 57, 103]

# Пример 4: аналог filter + map
print([x**2 for x in nums if x % 2 == 0])    # [4, 16]

# Без list comprehension — обычный цикл:
def squared_evens(a_list):
    result = []
    for x in a_list:
        if x % 2 == 0:
            result.append(x ** 2)
    return result

print(squared_evens(nums))                  # [4, 16]


# Пример. Составить список вымирающих видов.
species = [
    'golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel',
    'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout',
    'black bear', 'blue whale', 'water moccasin', 'giant panda',
    'green turtle', 'blue jay', 'japanese beetle'
]

population = [
    10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000,
    12000, 2300, 7500, 100, 1800, 9500, 125000
]

# Шаг 1: Объединить в пары (вид, популяция)
pop_info = list(zip(species, population))

# Шаг 2: Оставить только тех, у кого популяция < 2500
endangered = [name for name, pop in pop_info if pop < 2500]

print(endangered)   # ['black rhino', 'orangutan', 'sumatran elephant', 'blue whale', 'giant panda', 'green turtle']




    # Data Parsing HTML / веб-страниц

# Модуль requests в Python — это мощная и удобная библиотека для работы с HTTP-запросами. С его помощью можно легко:
# - скачивать страницы с интернета,
# - отправлять GET и POST-запросы,
# - работать с API.

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results


iTunes_response = requests.get("https://itunes.apple.com/search?term=jack+johnson&media=music&entity=musicTrack&limit=25")
py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])




    # Для справки

    # yield и return

# return — возвращает значение и завершает функцию
def f():
    return 1
    print("Это не выполнится")

print(f())  # 1

# yield — возвращает значение во временной точке и приостанавливает функцию
# Функция с yield — это генератор. Она возвращает значения по одному, сохраняя своё состояние, и может быть возобновлена позже.
# Функция с yield — это генератор, и она завершается, когда выполнение достигает конца функции или встречает return без значения.
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3


    # yield from — делегирование генератора

# Обычный генератор возвращает значения через yield:

def gen1():
    yield 1
    yield 2

def gen2():
    yield 3
    yield 4

# Чтобы вывести все значения из gen1 и gen2, можно делать так:

def combined_old():
    for v in gen1():
        yield v
    for v in gen2():
        yield v

# Но это громоздко. Вместо этого есть удобный синтаксис:

def combined_new():
    yield from gen1()   # делегируем генератор gen1()
    yield from gen2()   # делегируем генератор gen2()

# Использование:

for val in combined_new():
    print(val)
# Вывод:
# 1
# 2
# 3
# 4










# ============================================================
# 4. Python Classes and Inheritance
# ============================================================

    # Classes 

# Термины

# Класс — пользовательский составной тип (шаблон), в котором описано, какие переменные (атрибуты) и функции (методы) будут у объектов. 
# Объект (экземпляр класса) — конкретный экземпляр класса, созданный по его шаблону. У объекта есть своё состояние (значения переменных) и поведение (методы).
# Поле (атрибут) — переменная, хранящаяся внутри объекта. Атрибуты определяют состояние объекта и задаются в __init__.
# Метод — функция, определённая внутри класса. Методы описывают, что умеет делать объект, и вызываются через экземпляр (например, obj.method()).
# Переменная экземпляра — переменная, связанная с конкретным объектом (self.variable). У каждого объекта она может иметь своё значение.
# Переменная класса — переменная, общая для всех объектов класса. Определяется внутри класса вне методов. Обращение: ClassName.variable.
# Метод экземпляра — обычный метод, первым аргументом которого идёт self. Позволяет работать с переменными конкретного объекта.
# Метод класса — метод, первым аргументом которого идёт cls. Определяется с декоратором @classmethod и работает с переменными самого класса.
# Статический метод — метод без доступа к self или cls. Используется, когда логика метода не зависит от состояния объекта или класса. Объявляется через @staticmethod.
# Сигнатура функции — это её имя + список параметров с их порядком и типами (если указаны).
# Параметры — переменные, указанные в сигнатуре функции или метода. Получают значения из аргументов при вызове.
# Аргументы — конкретные значения, переданные при вызове функции или метода, чтобы соответствовать параметрам.
# Публичные переменные — переменные, которые можно свободно читать и изменять снаружи класса. В Python все переменные по умолчанию публичные.
# Приватные переменные — переменные, начинающиеся с двойного подчёркивания __. Они защищены от прямого доступа извне через механизм name mangling (self.__x становится self._ClassName__x).



# Основы
class Car:
    pass        # pass - заглушка, когда синтаксис требует, чтобы что-то было, но ты ещё не реализовал поведение.

my_car = Car()  # создание объекта (экземпляра класса) с помощью конструктора (специального метода)


# Поля: переменные экземпляра и класса
class Car:
    wheels = 4                  # переменная класса (общая для всех машин)

    def __init__(self, color):  # cоздание инициализатора, метода, который вызывается при инициализации объекта в качестве конструктора
        self.color = color      # переменная экземпляра (уникальна для каждой машины)

car1 = Car("red")
car2 = Car("blue")

print(car1.color)   # red
print(car2.color)   # blue
print(car1.wheels)  # 4


# Методы: экземпляра, класса и статический
class Car:
    total_cars = 0

    def __init__(self, color):
        self.color = color
        Car.total_cars += 1

    def honk(self):  # метод экземпляра
        print("Beep beep!")

    @classmethod
    def show_total(cls):  # метод класса
        print(f"Total cars: {cls.total_cars}")

    @staticmethod
    def info():  # статический метод
        print("Cars are means of transportation")

car = Car("green")
car.honk()           # Beep beep!
Car.show_total()     # Total cars: 1
Car.info()           # Cars are means of transportation


# Аргументы и параметры 
def greet(name):  # name — параметр
    print("Hello,", name)

greet("Egor")  # "Egor" — аргумент


# Публичные и приватные переменные
class User:
    def __init__(self, name, password):
        self.name = name               # публичная
        self.__password = password     # приватная

    def get_password(self):
        return self.__password

u = User("Egor", "12345")
print(u.name)             # OK
#print(u.__password)    # Ошибка (AttributeError)
print(u.get_password())   # OK


# Специальные методы (магические методы)
# Эти методы начинаются и заканчиваются двойным подчёркиванием (__method__).
# Используются для настройки поведения объектов класса.

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        print(f"Hello, I'm {self.name}")

p1 = Person("Egor")
p2 = Person("Egor")
print(str(p1))      # Person: Egor
print(len(p1))      # 4
p1()                # Hello, I'm Egor

# Часто используемые специальные методы:
# - __init__(self, ...)     — инициализация объекта
# - __str__(self)           — строковое представление (print)
# - __eq__(self, other)     — оператор ==
# - __lt__(self, other)     — определяет поведение оператора <  def __lt__(self, other):    # less than
#                                                                   return self.price < other.price
# - __len__(self)           — функция len()
# - __call__(self)          — позволяет вызывать объект как функцию


# Приватные элементы в Python 

class Example:
    def __init__(self):
        self.public = "Я общедоступен"
        self._protected = "Я защищённый (protected), по соглашению"
        self.__private = "Я приватный (private) с name mangling" # __var переименовывается в _ClassName__var

    def get_private(self):
        return self.__private

e = Example()

print(e.public)             # Доступно везде
print(e._protected)         # Технически доступно, но по соглашению не трогать
# print(e.__private)        # Ошибка! Атрибут не найден

# Обход name mangling:
print(e._Example__private)  # Получаем приватное значение



# Примеры с учебы

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    count = 0               # переменная класса

    def __init__(self, initX, initY):

        self.x = initX      # переменная экземпляра
        self.y = initY
        Point.count += 1    # на переменную класса ссылаюсь через Point

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance(self, point2):                 # метод, считает расстояние от конкретного экземпляра до точки
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()
        
        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    def distancePoints1(point1, point2):        # функция класса, считает расстояние от между двумя точками
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    @staticmethod                               # чтобы можно было вызывать через экземпляр. пример ниже
    def distancePoints2(point1, point2):         
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    def __str__(self):                  # специальный метод
        return "x = {}, y = {}".format(self.x, self.y)
    
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)            # Возвращает точку

p = Point(4,3)
q = Point(0,0)

print(p.distanceFromOrigin())
print(p.distance(q))

#print(q.distancePoints1(p,q))      # TypeError, Python автоматически передаёт экземпляр p как первый аргумент. @staticmethod - решает эту проблему.
print(q.distancePoints2(p,q))   
print(Point.distancePoints1(p,q))   # Лучше так вызывать 
print(Point.distancePoints2(p,q))   #               методы класса (функции класса)


class Cereal:
    def __init__(self, str1, str2, int1):
        self.name = str1
        self.brand = str2
        self.fiber = int1
    
    def __str__(self):
        return f'{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!'
        
c1 = Cereal('Corn Flakes', "Kellogg's", 2)   
c2 = Cereal('Honey Nut Cheerios', "General Mills", 3) 

print(c1)
print(c2)


# dir() – просмотр атрибутов и методов
# dir(Cereal) — показывает все атрибуты и методы класса (включая магические)
"""
[
 '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__'
]
"""
# dir(c1) — показывает всё то же самое плюс переменные экземпляра
"""
[
 '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__',
 'brand', 'fiber', 'name'
]
"""


# Тестирование классов

#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0



    # Наследование классов

# Наследование — это механизм, с помощью которого один класс (называется подкласс, subclass) 
# может наследовать свойства и поведение другого класса (называемого суперкласс, superclass или base class).

# superclass
class Animal:           
    count = 0           # переменная класса

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    def sleep(self):    # метод
        print("Zzz")

    def speak(self):    # метод
        print("Some sound")

# subclass
class Dog(Animal):      # В скобках пишем родительский класс
    def speak(self):    # Переопределение метода
        print("Woof!")

a = Animal("a")
dog = Dog("b")

print(Animal.count)     # 2 Dog тоже посчитался
print(dog.name)         # b - вызвался инизиализатор родительского класса
dog.speak()             # Woof!


# subclass
class Cat(Animal):      

    def __init__(self, name, breed):    # Создание своего инициализирующего метода
        super().__init__(name)          # с помощью ключевого слова super сслыаемся на родительский метод
        self.breed = breed              # добавляем свою переменную

    def speak(self):    # Переопределение метода
        print("Meow!")

cat = Cat("c", "siam")

print(Animal.count)     # 3
cat.speak()             # Some sound
print(cat.breed)        # siam


# Множественное наследование в Python
# Python позволяет создавать класс, который наследует поведение от двух и более базовых классов.
# Однако лучше избегать множественного наследования, если только оно не даёт реального преимущества и не делает код чище и понятнее.

class BreedClass(Cat, Dog):
    pass

# Если оба родительских класса имеют метод с одинаковым именем, Python выбирает из первого родительского класса
class Mother:
    eyes = "Brown"
    def hello(self):
        print("Привет от Мамы")

class Father:
    eyes = "Blue"
    def hello(self):
        print("Привет от Папы")

class Child(Mother, Father):  # порядок важен!
    pass

Ivan = Child()
print(Ivan.eyes)    # Brown
Ivan.hello()        # Привет от Мамы


# Полиморфизм в Python
# Полиморфизм - это способность объектов разных классов использовать один и тот же интерфейс (одинаковые имена методов), 
# но при этом реализовывать поведение по-своему.

# animal_sound работает с любым объектом, у которого есть метод speak() — неважно, какой это класс. Это и есть полиморфизм.
def animal_sound(animal):
    animal.speak()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!


# Как интерпретатор ищет атрибуты:
# 1. Проверяет в экземпляре класса. 
# 2. Если не найдено, ищет в с самом классе
# 3. Проверяет родительский класс
# 4. Проверяет следующих предков по порядку до конца.


    # Декораторы

# Повтор. Декоратор функции
def addLogging(func):           # Это декоратор — он принимает функцию в качестве аргумента.
    def wrapper(x):             # Это обёртка (wrapper-функция), которая заменит оригинальный метод.
                                # Она должна принимать те же аргументы, что и оригинальный метод.
                                # В случае метода — первый аргумент всегда self, а далее — любые аргументы (здесь x — один аргумент)
        print(f"Before")        # Первый лог
        result = func(x)        # Это вызов оригинального метода, который был передан как func. Ему передаются все нужные аргументы.
        print(f"After")         # Второй лог
        return result           # Возвращается результат, который вернул оригинальный метод.
    return wrapper              # Возвращается обёртка, которая содержит в себе логи и результат выполнения функции.
                                # Теперь обёртка будет использоваться вместо оригинальной функции.

@addLogging
def printName(name):
    print(f"My name is {name}")

printName("Egor")       # Before
                        # My name is Egor
                        # After


# Декоратор метода: логирование вызовов. Универсальный
def universal_logger(func):
    def wrapper(*args, **kwargs):               # *args и **kwargs делают декоратор универсальных на любое количество аргументов
        print(f"Calling: {func.__name__}")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# Применение к обычной функции
@universal_logger
def add(a, b):
    return a + b

add(3, 5)           # Calling: add
                    #   args: (3, 5)
                    #   kwargs: {}
                    # Result: 8

# Применение к методу класса
class Calculator:
    @universal_logger
    def multiply(self, x, y):
        return x * y

calc = Calculator()
calc.multiply(4, 6) # Calling: multiply
                    #   args: (<__main__.Calculator object at 0x...>, 4, 6)
                    #   kwargs: {}
                    # Result: 24


# Декоратор класса: добавление метода
def addBeep(cls):
    def beep(self):
        print(f"{self.model} says 'Beep!'")
    cls.beep = beep
    return cls

@addBeep
class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

mustang = Car("Ford", "Mustang", "blue", 0)
mustang.beep()      # Mustang says 'Beep!'


# Декораторы с аргументами
def repeat(n):
    """Декоратор, который повторяет выполнение функции n раз"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()  # напечатает "Hi!" три раза


# Модуль functools
# Предоставляет утилиты для работы с функциями и декораторами, особенно когда функции нужно модифицировать, оборачивать или кэшировать.

# Самое полезное: @functools.wraps
# Когда ты создаёшь свой декоратор, Python заменяет оригинальную функцию обёрткой (wrapper). В результате теряется имя, докстрока, аннотации и т.д.
# Чтобы сохранить оригинальные свойства функции — используют @functools.wraps.

import functools
import time

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()     # "Start" timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()       # "Stop" timer
        elapsed_time = end_time - start_time 
        return result, elapsed_time
    return wrapper

@performance
def say_hello():
    """Prints a greeting"""
    print("Hello!")

say_hello()                 # Hello!
                            # (None, 4.700000863522291e-05) - None, потому что обертка возвращает (result, elapsed_time)
print(say_hello.__name__)   # say_hello
print(say_hello.__doc__)    # Prints a greeting



# Динамические аргументы позволяют передать любое количество аргументов в функцию без заранее известного количества параметров.

# Динамические позиционные аргументы: *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))           # 6
print(sum_all(5, 10, 15, 20))     # 50

# Динамические именованные аргументы: **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Egor", age=30, city="Korolyov")

# Комбинирование *args и **kwargs
# def example(pos1, *args, kw1=None, **kwargs):


    # Exceptions Исключения

# Исключения — это ошибки, которые возникают во время выполнения программы.

#Базовая структура обработки исключений

try:
    print (1/0)
except :
    print("Произошла ошибка")   # Произошла ошибка
finally:                                # не обязательная часть
    print("Этот код выполнится всегда") # Даже если ошибки нет, finally будет выполнен

#   Есть встроенные типы исключений:
# ZeroDivisionError — деление на ноль
# ValueError — неправильное значение
# TypeError — несоответствие типов
# IndexError — выход за границы списка
# KeyError — отсутствует ключ в словаре
# FileNotFoundError — файл не найден
# AttributeError — обращение к несуществующему атрибуту
# и много других

# Пример:
try:
    x = int(input("Введите число: "))
    print(10 / x)
except ZeroDivisionError:
    print("Нельзя делить на ноль!")
except ValueError:
    print("Это не число!")


# Создание собственных исключений
class NegativeNumberError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Отрицательное число не допускается: {value}")

def square_root(x):
    if x < 0:
        raise NegativeNumberError(x)    # Ключевое слово raise используется, чтобы намеренно вызвать исключение — встроенное или пользовательское.
    return x ** 0.5

try:
    print(square_root(-25))
except NegativeNumberError as e:
    print(e)  # Отрицательное число не допускается: -25