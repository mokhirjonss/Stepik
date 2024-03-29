# 13.2 Функции с параметрами

# Тема урока: функции с параметрами

# Функции с параметрами
# Область видимости параметрической переменной
# Решение задач

# Аннотация. Создание пользовательских функций с параметрами.

# Функции с параметрами

# В предыдущем уроке мы определили функцию draw_box(), которая выводит звездный прямоугольник с размерами 5×7:
def draw_box():
    for i in range(5):
        print('*' * 7)

draw_box()
# *******
# *******
# *******
# *******
# *******

# Было бы намного удобнее, если бы функция draw_box() выводила прямоугольник с произвольными размерами.
# И действительно, функции могут принимать входные параметры, что делает их более гибкими.

# Функции с параметрами объявляются так же как функции без параметров, только с указанием в скобках:
# def название_функции(параметры):
#     блок кода

# Давайте перепишем предыдущую версию функции draw_box() так, чтобы она принимала параметры,
# задающие высоту и ширину прямоугольника:
print()
def draw_box(height, width):  # функция принимает два параметра
    for i in range(height):
        print('*' * width)
# Теперь наша функция draw_box() принимает два целочисленных параметра height – высота прямоугольника и width – ширина
# прямоугольника, и для ее вызова нам нужно обязательно их указать.

# Чтобы вывести звездный прямоугольник размерами 5 на 7 мы пишем код:
draw_box(5, 7)
# *******
# *******
# *******
# *******
# *******

# Результатом такого вызова функции draw_box(5, 7) будет:
# *******
# *******
# *******
# *******
# *******

# Чтобы вывести прямоугольник размерами 10 на 15, мы пишем код:
draw_box(10, 15)
# Результатом такого вызова функции draw_box(10, 15) будет:
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************

# Теперь с помощью нашей новой версии функции draw_box() можем в одной программе
# выводить прямоугольники разных размеров. Следующий программный код:
draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)

# выведет:

# ***
# ***
# ***
#
# *****
# *****
# *****
# *****
# *****
#
# **********
# **********
# **********
# **********

# На место параметров мы можем подставлять не только целочисленные константы, но и значения переменных.
# Следующий программный код:
n = 3
m = 9
draw_box(n, m)

# выведет:
# *********
# *********
# *********

# Еще примеры
# Напишем функцию print_hello(n), которая принимает одно натуральное число n и печатает слово Hello ровно n раз.
def print_hello(n):
    print('Hello' * n)

# Следующий программный код:
print_hello(3)
print_hello(5)
times = 2
print_hello(times)

# выведет:
# HelloHelloHello
# HelloHelloHelloHelloHello
# HelloHello

# Функцию print_hello() можно сделать более гибкой, если передавать в нее еще один параметр – текст для вывода:
def print_text(txt, n):
    print(txt * n)

# Следующий программный код:
print_text('Hello', 5)
print_text('A', 10)
# выведет:
# HelloHello
# HelloHelloHelloHelloHello
# AAAAAAAAAA

# Параметры VS аргументы

# Аргумент – это любая порция данных, которая передается в функцию, когда функция вызывается.
# Параметр – это переменная, которая получает аргумент, переданный в функцию.

# Для функции draw_box(height, width):
def draw_box(height, width):
    for i in range(height):
        print('*' * width)
# параметрами являются переменные height и width.

# В момент вызова функции draw_box(height, width):
height = 10
draw_box(height, 9)

# аргументами являются height и 9.

# Параметры функций часто называют параметрическими переменными.

# Внесение изменений в параметры

# Когда аргумент передается в функцию, параметрическая переменная функции будет ссылаться на значение этого аргумента.
# Однако любые изменения, которые вносятся в параметрическую переменную, не будут влиять на аргумент.

# Cледующий программный код:
def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)

# выведет:
# **********
# **********
# 5 7

# В теле функции вносятся изменения в значения параметрических переменных height и width, однако это никак не повлияло
# на значение переменных n и m из основной программы, которые передавались в качестве аргументов в функцию draw_box().

# Примечание

# Примечание 1. Функции в Python могут принимать сколько угодно параметров.
# Примечание 2. Иногда вместо параметров и аргументов говорят о формальных параметрах и фактических параметрах.
# Формальные параметры – переменные, которые мы пишем при описании функции. Фактические параметры – то,
# что реально подставляется при вызове функции.

# Порция данных, которая отправляется в функцию в момент ее вызова, называется
# аргумент

# Особая переменная, которая получает порцию данных, когда вызывается функция называется
# параметр

# Взгляните на приведенный ниже заголовок функции:
def my_function(a, b, c):
    print(a, b, c)
# Теперь взгляните на вызов этой функции:
my_function(3, 2, 1)
# Какие значения будут присвоены параметрам a, b, c когда вызов исполнится?

# a 3
# b 2
# c 1

# Взгляните на приведенное ниже определение функции:
def print_number(a, b, c):
    d = (a + c) // b
    print(d)
print_number(2, 3, 11)

# Какое значение будет показано, после вызова функции print_number(2, 3, 11)?
# 4

# Что покажет приведенная ниже программа?
def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

x = 1
y = 7
print(x, y)
change_us(x, y)
print(x, y)
# 1 7
# 0 0
# 1 7

# Что покажет приведенная ниже программа?
def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1

print_text('Python', 4)
# PythonPythonPythonPython

# Звездный треугольник
# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;

# а затем выводит его.

# Примечание. Гарантируется, что основание треугольника – нечетное число.
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(i * fill)
    for j in range(base // 2, 0, -1):
        print(j * fill)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
# Sample Input 1:
#
# *
# 9
# Sample Output 1:
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# Sample Input 2:
#
# +
# 5
# Sample Output 2:
#
# +
# ++
# +++
# ++
# +
# Sample Input 3:
#
# ?
# 7
# Sample Output 3:
#
# ?
# ??
# ???
# ????
# ???
# ??
# ?

# ФИО
# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;

# а затем выводит на печать ФИО человека.

# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0] + name[0] + patronymic[0])

# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию
print_fio(name, surname, patronymic)
# Sample Input 1:
#
# Александр
# Пушкин
# Сергеевич
# Sample Output 1:
#
# ПАС
# Sample Input 2:
#
# тимур
# Гуев
# ахсарбекович
# Sample Output 2:
#
# ГТА

# Сумма цифр
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(num):
    total = [i for i in str(num)]
    print(sum(total))



# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

# объявление функции
def print_digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10

    print(digit_sum)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

# Sample Input 1:
#
# 12345
# Sample Output 1:
#
# 15
# Sample Input 2:
#
# 12
# Sample Output 2:
#
# 3
# Sample Input 3:
#
# 7
# Sample Output 3:
#
# 7



