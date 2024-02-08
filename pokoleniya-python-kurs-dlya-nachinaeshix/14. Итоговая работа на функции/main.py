# 14. Итоговая работа на функции

# Какой программный код написан с ошибкой?
# def do_something():
#   a = 1
#   print(a)
#
# a = 0
# do_something()
# print(a)
# def do_something():
#   a = 1
#
# do_something()
# print(a)
# a = 1
#
# def do_something():
#   print(a)
#
# do_something()

# 2

# Какие из переменных в приведенном ниже коде являются локальными?
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

number = int(input())
f = factorial(number)
# i
# res
# n

# Вставить в пропуски слова из списка.
# Примечание. Слова могут использоваться не все и могут повторяться.
# Заполните пропуски
# Python считает переменную локальной для данной функции, если в её коде есть хотя бы одна инструкция,
# модифицирующая значение переменной. В этом случае эта переменная считается локальной и не может быть использована до
# инициализации.

# Звездный треугольник 🌶️
# Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник с основанием и высотой
# равными 15 и 8 соответственно:
#        *
#       ***
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
# Примечание 1. Для вывода треугольника используйте цикл for.
# Примечание 2. Справа от звездочек пробелов нет.

# объявление функции
def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)

# основная программа
draw_triangle()

# Калькулятор доставки
# Интернет-магазин осуществляет экспресс доставку для своих товаров по цене 1000 рублей за первый товар и 120 рублей за
# каждый последующий товар. Напишите функцию get_shipping_cost(quantity), которая принимает в качестве
# аргумента натуральное число quantity – количество товаров в заказе – и возвращает стоимость доставки.

# объявление функции
def get_shipping_cost(quantity):
    total = 880
    for i in range(quantity):
        total += 120
    return total
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# объявление функции
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# Примечание. Следующий программный код:
print(get_shipping_cost(1))
print(get_shipping_cost(3))
# должен выводить:
# 1000
# 1240

# Биномиальный коэффициент 🌶️
# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает
# значение биномиального коэффициента, равного n! / (k! (n - k)!).

# Примечание 1. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть

# n!=1⋅2⋅3⋅…⋅n

# Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую факториал числа, или воспользуйтесь уже
# готовой функцией из модуля math. Обратите внимание, что функция compute_binom(n, k) должна возвращать целое число.

from math import factorial
# объявление функции
def compute_binom(n, k):
    factorial_binom = factorial(n) / (factorial(k) * factorial(n - k))
    return int(factorial_binom)

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))

from math import factorial as f


# объявление функции
def compute_binom(n, k):
    return f(n) // (f(k) * f(n - k))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))

# Число словами 🌶️
# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное число num и возвращает его
# словесное описание на русском языке.

# Примечание 1. Считайте, что число 1≤num ≤99.

# объявление функции
def number_to_words(num):
    before_twenty = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
        'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]
    after_twenty = [
        'двадцать', 'тридцать', 'сорок', 'пятьдесят',
        'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]

    if num < 20:
        res = before_twenty[num]
    else:
        res = after_twenty[num // 10 - 2] + " " + before_twenty[num % 10]

    return res.strip()


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
# Примечание 2. Следующий программный код:
print(number_to_words(7))
print(number_to_words(85))
# должен выводить:
# семь
# восемьдесят пять

# Искомый месяц
# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и
# number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

# объявление функции
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
              'декабрь']

    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

    if language == 'ru':
        a = lng_ru[number - 1]
    else:
        a = lng_en[number - 1]

    return a.strip()

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

# объявление функции
def get_month(language, number):
    en_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                 'october', 'november', 'december']
    ru_months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь',
                 'октябрь', 'ноябрь', 'декабрь']

    if language == 'en':
        return en_months[number - 1]
    else:
        return ru_months[number - 1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
# Примечание. Следующий программный код:
print(get_month('ru', 1))
print(get_month('ru', 12))
print(get_month('en', 1))
print(get_month('en', 10))
# должен выводить:
# январь
# декабрь
# january
# october

# Магические даты
# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, образованному последними двумя цифрами года.

# Напишите функцию is_magic(date), которая принимает в качестве аргумента строковое представление корректной даты и
# возвращает значение True, если дата является магической и False - в противном случае.

# объявление функции
def is_magic(date):
    d, m, g = map(int, date.split('.'))
    if int(d) * int(m) == g % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
# Примечание. Следующий программный код:
print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))
# должен выводить:
# True
# False

# Панграммы
# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов,
# чтобы можно было в одной фразе рассмотреть все глифы.

# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и
# возвращает значение True если текст является панграммой и False в противном случае.

# Примечание 1. Гарантируется, что введенная строка содержит только буквы английского алфавита и пробелы.

# объявление функции
def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    text_set = set(text.lower().replace(" ", ""))
    return alphabet.issubset(text_set)

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))


# объявление функции
def is_pangram(text):
    text = text.lower()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False

    return True


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
# Примечание 2. Следующий программный код:
print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))
# должен выводить:
# True
# True
# False

