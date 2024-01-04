# 9.1 Индексация

# Тема урока: строки

# Индексация строк
# Итерирование строк
# Решение задач

# Аннотация. Строковый тип данных. Вспомним основные операции над строками, научимся работать с отдельными символами,
# а также перебирать (итерировать) символы строк.

# Повторение материала

# Строки в Python используются когда надо работать с текстовыми данными.

# Создание строки. Для создания строк, мы используем парные кавычки '' или "":
s1 = 'Python'
s2 = "Pascal"

# Считывание строки. Для считывания текстовых данных в строковую переменную, мы используем функцию input():

s = input()  # считали текст
num = int(input())  # считали текст и преобразовали его в целое число

# Пустая строка. Для создания пустой строки, мы пишем s = '' или s = "". Пустая строка – это аналог числа 0.

# Длина строки. Для определения длины строки (количества символов), мы используем встроенную функцию len():
s = 'Hello'
n = len(s)  # значение переменной равно 5
print(n)

# Конкатенация и умножение на число. Операторы + и * можно использовать для строк.
# Оператор + сцепляет две и более строк. Это называется конкатенацией строк.
# Оператор * повторяет строку указанное количество раз.

# Выражение	Результат
# 'AB' + 'cd'	'ABcd'
# 'A' + '7' + 'B'	'A7B'
# 'Hi'* 4	'HiHiHiHi'

# Оператор принадлежности in. С помощью оператора in, мы можем проверять, находится ли одна строка в составе другой.
# То есть, является ли одна строка подстрокой другой:
s = 'All you need is love'
if 'love' in s:
    print('YES')
else:
    print('NO')
# Так как строка s содержит подстроку 'love', то будет выведен YES

#  В Python можно использовать смайлики emoji👍

# Индексация строк

# Очень часто бывает необходимо обратиться к конкретному символу в строке. Для этого в Python используются квадратные
# скобки [], в которых указывается индекс (номер) нужного символа в строке.

# Пусть s = 'Python'. Таблица ниже, показывает как работает индексация:

# Выражение	Результат	Пояснение
# s[0]	P	первый символ строки
# s[1]	y	второй символ строки
# s[2]	t	третий символ строки
# s[3]	h	четвертый символ строки
# s[4]	o	пятый символ строки
# s[5]	n	шестой символ строки

# Обратите внимание первый символ строки равен s[0], а не s[1]. В Python индексация начинается с 0,
# по аналогии с функцией range(n), которая генерировала последовательность натуральных чисел от 0 до n - 1.

# В отличие от многих языков программирования, в Python есть возможность работы с отрицательными индексами.
# Если первый символ строки имеет индекс 0, то последнему элементу присваивается индекс -1.

# Выражение	Результат	Пояснение
# s[-6]	P	первый символ строки
# s[-5]	y	второй символ строки
# s[-4]	t	третий символ строки
# s[-3]	h	четвертый символ строки
# s[-2]	o	пятый символ строки
# s[-1]	n	шестой символ строки

# Таким образом, получаем

# Положительные индексы	0	1	2	3	4	5
# Строка	P	y	t	h	o	n
# Отрицательные индексы	-6	-5	-4	-3	-2	-1

# Частая ошибка у начинающих программистов — обращение по несуществующему индексу в строке.

# Например, если s = 'Python', и мы попытаемся обратится к s[17], то мы получим ошибку:
# IndexError: string index out of range

# Ошибка возникает, поскольку строка содержит всего 6 символов.

# Обратите внимание: если длина строки s равна len(s), то при положительной нумерации слева направо,
# последний элемент имеет индекс равный len(s) - 1, а при отрицательной индексации справа налево, первый элемент
# имеет индекс равный -len(s).

# Итерирование строк

# Очень часто нужно просканировать всю строку целиком, обрабатывая каждый ее символ. Для этого удобно
# использовать цикл for. Напишем программу, которая выводит каждый символ строки на отдельной строке:
s = 'abcdef'
for i in range(len(s)):
    print(s[i])
# Результатом выполнения такой программы будут строки:

# a
# b
# c
# d
# e
# f

# Мы передаем в функцию range() длину строки len(s). В нашем случае длина строки s, равна 6. Таким образом,
# вызов функции range(len(s)) имеет вид range(6) и переменная цикла i последовательно перебирает
# все значения от 0 до 5. Это означает, что выражение s[i] последовательно вернет все символы строки s.
# Такой способ итерации строки удобен, когда нам нужен не только сам элемент s[i], но и его индекс i.

# Если нам не нужен индекс самого символа, то мы можем использовать более короткий способ итерации:
s = 'abcdef'
for c in s:
    print(c)
# a
# b
# c
# d
# e
# f

# Этот цикл пройдет по строке s, придавая переменной цикла c значение каждого символа (!) в отличие от предыдущего
# цикла, в котором переменная цикла «бегала» по индексам строки.

# Обратите внимание на обозначение переменных цикла. В первом цикле мы используем имя i, что соответствует стандартной
# идеологии наименования переменных цикла. Во втором цикле,
# мы назвали переменную буквой c – первая буква слова char (символ).

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[0] + s[2] + s[4] + s[6])
# aceg

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)
# aaagggdddd

# Что покажет приведенный ниже фрагмент кода?
s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
# 051217

# Дополните приведенный код, используя индексатор, так чтобы он вывел символ запятой.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[7])
# ,

# Дополните приведенный код, используя индексатор, так чтобы он вывел символ w.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."

print(s[-10])
# w

# В столбик 1

# На вход программе подается одна строка. Напишите программу,
# которая выводит элементы строки с индексами 0, 2, 4, ... в столбик.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести элементы строки с индексами 0, 2, 4, ..., каждое на отдельной строке.

words = input()
for i in range(0, len(words), 2):
    print(words[i])
# Sample Input:
#
# abcdefghijklmnop
# Sample Output:
#
# a
# c
# e
# g
# i
# k
# m
# o

# В столбик 2

# На вход программе подается одна строка.
# Напишите программу, которая выводит в столбик элементы строки в обратном порядке.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести в столбик элементы строки в обратном порядке.

words = input()
for i in range(1, len(words) + 1):
    print(words[-i])
# Sample Input:
#
# abc
# Sample Output:
#
# c
# b
# a

# ФИО

# На вход программе подаются три строки: имя, фамилия и отчество. Напишите программу, которая выводит инициалы человека.

# Формат входных данных
# На вход программе подаются три строки, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести ФИО человека.

# Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.

surname, name, patronymic = input(), input(), input()
print(name[0] + surname[0] + patronymic[0])
# Sample Input:
#
# Тимур
# Гуев
# Ахсарбекович
# Sample Output:
#
# ГТА

# Цифра 1

# На вход программе подается одна строка состоящая из цифр. Напишите программу,
# которая считает сумму цифр данной строки.

# Формат входных данных
# На вход программе подается одна строка состоящая из цифр.

# Формат выходных данных
# Программа должна вывести сумму цифр данной строки.
total = 0
numbers = input()
for i in range(len(numbers)):
    total += int(numbers[i])
print(total)

# Sample Input:
#
# 2514
# Sample Output:
#
# 12

# Цифра 2

# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек),
# если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
flag = 'Цифр нет'
words = input()
for i in range(len(words)):
    if words[i] in '0123456789':
        flag = 'Цифра'
        break
print(flag)
# Sample Input 1:
#
# Hi Python
# Sample Output 1:
#
# Цифр нет
# Sample Input 2:
#
# Hi 17 Python
# Sample Output 2:
#
# Цифра

# Сколько раз?
# На вход программе подается одна строка. Напишите программу, которая определяет,
# сколько раз в строке встречаются символы + и *.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести сколько раз встречаются символы + и * в строке.

words = input()
total_plus = 0
total_umno = 0
for i in range(len(words)):
    if words[i] == '+':
        total_plus += 1
    if words[i] == '*':
        total_umno += 1
print(f"Символ + встречается {total_plus} раз\n"
      f"Символ * встречается {total_umno} раз")
# Sample Input:
#
# bcd+a++++**31415
# Sample Output:
#
# Символ + встречается 5 раз
# Символ * встречается 2 раз

# Одинаковые соседи

# На вход программе подается одна строка.
# Напишите программу, которая определяет сколько в ней одинаковых соседних символов.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести количество одинаковых соседних символов.
total = 0
words = input()
for i in range(len(words) - 1):
    if words[i] == words[i + 1]:
        total += 1
print(total)
# Sample Input 1:
#
# abcd
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# aabbcc
# Sample Output 2:
#
# 3
# Sample Input 3:
#
# aaa
# Sample Output 3:
#
# 2

# Гласные и согласные

# На вход программе подается одна строка с буквами русского языка. Напишите программу,
# которая определяет количество гласных и согласных букв.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести количество гласных и согласных букв.

# Примечание. В русском языке 10 гласных букв и 21 согласная буква:
# ауоыиэяюёе
# бвгджзйклмнпрстфхцчшщ
total_glas = 0
total_sog = 0
text = input()
for i in range(len(text)):
    if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        total_glas += 1
    if text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        total_sog += 1
print(f"Количество гласных букв равно {total_glas}\n"
      f"Количество согласных букв равно {total_sog}")
# Sample Input:
#
# Вдохновение – это умение приводить себя в рабочее состояние!
# Sample Output:
#
# Количество гласных букв равно 25
# Количество согласных букв равно 24

# Decimal to Binary

# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести число записанное в двоичной системе счисления.

numbers = int(input())
numbers = format(numbers, 'b')
print(numbers)
# Sample Input 1:
#
# 5
# Sample Output 1:
#
# 101
# Sample Input 2:
#
# 128
# Sample Output 2:
#
# 10000000


