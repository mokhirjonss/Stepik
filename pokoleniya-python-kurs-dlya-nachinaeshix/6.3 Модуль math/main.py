# 6.3 Модуль math

# Тема урока: модуль math

# Модуль math
# Решение задач

# Аннотация. Урок посвящен модулю math, который содержит математические функции по работе с вещественными числами.

# Модули

# Как уже говорилось, одним из преимуществ языка Python является множество разнообразных функций,
# которые уже реализованы и готовы к использованию. Такие функции упакованы в модули.
# В Python модулем называется библиотека функций, которую можно подключать к своим программам.

# Модуль math

# Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для проведения вычислений
# с вещественными числами (числами с плавающей точкой).

# Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:

import math

# программный код

# После подключения модуля мы можем использовать его функции. Пусть мы хотим:

# вычислить 2**(1/2) (корень квадратный из двух)
# округлить число 3.8 до ближайшего целого числа вверх и вниз

# Соответствующий программный код, решающий задачи выглядит так:

import math

num1 = math.sqrt(2)  # вычисление квадратного корня из двух
num2 = math.ceil(3.8)  # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

# и выводит:

# 1.4142135623730951
# 4
# 3

# Особенности подключения модулей

# Как можно заметить из примера выше, для вызова функции мы вынуждены указывать название модуля и символ точки.
# С другой стороны, если функции используются достаточно часто, то такой вызов
# (постоянное указание названия модуля и символа точки) может усложнить программу и сделать её менее читабельной.
# Для того, чтобы не указывать название модуля и символ точки при вызове функций, мы пишем следующий код:

from math import *

num1 = math.sqrt(2)  # вычисление квадратного корня из двух
num2 = math.ceil(3.8)  # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

# Таким образом, подключение модуля следующим образом:

from math import *

# позволяет не писать название модуля и символ точки. При таком способе подключения,
# импортируются абсолютно все функции модуля math.

# Если нужно использовать только некоторые функции модуля, то мы можем импортировать только их следующим образом:

from math import sqrt, ceil

# Теперь мы можем вызывать функции sqrt() и ceil() без префикса math., однако мы не можем вызвать функцию floor(),
# так как она не подключена:

from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

# print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена

# Список функций модуля math

# Список наиболее часто используемых функций модуля math:

# Функция	Описание
# Округления
# int()	Округляет число в сторону нуля
# round(x)	Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
# round(x, n)	Округляет число x до n знаков после точки
# floor(x)	Округляет число x вниз («пол»)
# ceil(x)	Округляет число x вверх («потолок»)
# abs(x)	Модуль числа x (абсолютная величина)
# Корни, логарифмы, степени и факториал
# sqrt(x)	Квадратный корень числа x
# pow(x, n)	Возведение числа x в степень n
# log(x)	Натуральный логарифм числа x. Основание натурального логарифма равно числу e
# log10(x)	Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
# log(x, b)	Логарифм числа x по основанию b
# factorial(n)	Факториал натурального числа n
# Тригонометрия
# degrees(x)	Преобразует угол x, заданный в радианах, в градусы
# radians(x)	Преобразует угол x, заданный в градусах, в радианы
# cos(x)	Косинус угла x, задаваемого в радианах
# sin(x)	Синус угла x, задаваемого в радианах
# tan(x)	Тангенс угла x, задаваемого в радианах

# Для извлечения квадратного корня можно воспользоваться кодом n ** 0.5, вместо math.sqrt(n).

# Список констант модуля math

# Модуль math предоставляет ряд встроенных математических констант:

#  Константа Описание
# pi Число π = 3.141592653589793
# e	 Число e = 2.718281828459045 (константа Эйлера)

# Примечания

# Примечание 1. Все функции модуля math возвращают значение, которое можно вывести на экран, присвоить другой
# переменной или использовать в математическом выражении.

# Примечание 2. Для использования функций int(), float(), abs(), min(), max(), round() подключать модуль math нет
# необходимости. Это так называемые встроенные функции.

# Примечание 3. Вызов функций pow(x, n) можно заменить использованием оператора возведения в степень: x**n.

# Евклидово расстояние

# На плоскости евклидово расстояние между двумя точками
# (x1; y1) и (x2; y2) определяется так p = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2).

# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

# Формат входных данных
# На вход программе подается четыре вещественных числа, каждое на отдельной строке –
# x1, y1, x2, y2.

from math import *
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt((pow(x1 - x2, 2) + (pow(y1 - y2, 2)))))
# Sample Input 1:
#
# 2.0
# 2.5
# 44.155
# 100.50
# Sample Output 1:
#
# 106.68197610187018
# Sample Input 2:
#
# 5.5
# 2.4
# 4.9
# 6.3
# Sample Output 2:
#
# 3.9458839313897713
# Sample Input 3:
#
# 150.0
# 100.0
# 50.0
# 10.0
# Sample Output 3:
#
# 134.5362404707371

# Площадь и длина

# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.

# Формат входных данных
# На вход программе подается одно вещественное число R

# Формат выходных данных
# Программа должна вывести два числа – площадь круга и длину окружности радиуса R.

# Примечание. Используйте константу math.pi.

from math import *
r = float(input())  # радиус круга
print(pi * pow(r, 2))  # площадь круга
print(2 * pi * r)  # длина окружности

# Sample Input 1:
#
# 554.6
# Sample Output 1:
#
# 966294.7126386268
# 3484.654571361799
# Sample Input 2:
#
# 3.14
# Sample Output 2:
#
# 30.974846927333925
# 19.729201864543903
# Sample Input 3:
#
# 5.5
# Sample Output 3:
#
# 95.03317777109125
# 34.55751918948772

# Средние значения

# В математике выделяют следующие средние значения:
# среднее арифметическое чисел a и b: (a + b) / 2
# среднее геометрическое чисел a и b: (a * b)**(1/2)
# среднее гармоническое чисел a и b: (2 * a * b) / (a + b)
# среднее квадратичное чисел a и b: ((a**2 + b**2) / 2)**(1/2)

# Формат входных данных
# На вход программе подается два вещественных числа a и b, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *
a, b = float(input()), float(input())
print((a + b) / 2, sqrt(a * b), (2 * a * b) / (a + b), sqrt((pow(a, 2) + pow(b, 2)) / 2), sep='\n')

# Sample Input 1:
#
# 1.0
# 2.0
# Sample Output 1:
#
# 1.5
# 1.4142135623730951
# 1.3333333333333333
# 1.5811388300841898
# Sample Input 2:
#
# 35.1
# 40.3
# Sample Output 2:
#
# 37.7
# 37.61023796787252
# 37.52068965517241
# 37.78954881974644
# Sample Input 3:
#
# 50.0
# 25.5
# Sample Output 3:
#
# 37.75
# 35.70714214271425
# 33.77483443708609
# 39.687844486693905

# Тригонометрическое выражение

# Напишите программу, вычисляющую значение тригонометрического выражения
# sinx + cosx + tan**2x
# по заданному числу градусов x.

# Формат входных данных
# На вход программе подается одно вещественное число x измеряемое в градусах

# Формат выходных данных
# Программа должна вывести одно число – значение тригонометрического выражения.

# Примечание 1. Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы,
# воспользуйтесь формулой
# r = x * pi / 180

# Примечание 2. Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.

from math import *
x = radians(float(input()))
print(sin(x) + cos(x) + tan(x) * tan(x))
# Sample Input 1:
#
# 30.0
# Sample Output 1:
#
# 1.6993587371177719
# Sample Input 2:
#
# 45.0
# Sample Output 2:
#
# 2.414213562373095
# Sample Input 3:
#
# 60.0
# Sample Output 3:
#
# 4.3660254037844375

# Пол и потолок
# Напишите программу, вычисляющую значение |x| + |x| по заданному вещественному числу x.

# Формат входных данных
# На вход программе подается одно вещественное число x.

# Формат выходных данных
# Программа должна вывести одно число – значение указанного выражения.

# Примечание. [x] - потолок числа, [x] - пол числа.

from math import *
x = float(input())
print(floor(x) + ceil(x))
# Sample Input 1:
#
# 5.5
# Sample Output 1:
#
# 11
# Sample Input 2:
#
# 5.4
# Sample Output 2:
#
# 11
# Sample Input 3:
#
# -12.2
# Sample Output 3:
#
# -25

# Квадратное уравнение 🌶️🌶️
# Даны три вещественных числа a, b, c.
# Напишите программу, которая находит вещественные корни квадратного уравнения
# ax**2 + bx + c = 0.
# Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

# Формат входных данных
# На вход программе подается три вещественных числа a != 0, b, c, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести вещественные корни уравнения каждый на отдельной строке, если они существуют,
# или текст «Нет корней» в противном случае.

from math import *
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c
if d > 0:
    print(min((-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)))
    print(max((-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)))
elif d == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')
# Sample Input 1:
#
# 1
# 2
# 1
# Sample Output 1:
#
# -1.0
# Sample Input 2:
#
# 1
# -7.5
# 3
# Sample Output 2:
#
# 0.4239663260874824
# 7.076033673912518

# Правильный многоугольник
# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Площадь правильного многоугольника с длиной стороны  a и количеством сторон n вычисляется по формуле:
# s = (n * a**2) / (4 * tg(pi/n))

# Даны два числа: натуральное число n и вещественное число a.
# Напишите программу, которая находит площадь указанного правильного многоугольника.

# Формат входных данных
# На вход программе подается два числа n и a, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести вещественное число – площадь многоугольника.

from math import *
n = int(input())
a = float(input())
s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)
# Sample Input:
#
# 3
# 2.0
# Sample Output:
#
# 1.7320508075688779

#
