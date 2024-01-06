# 9.2 Срезы

# Тема урока: строки

# Срезы строк
# Изменение символов строки
# Решение задач

# Аннотация. Снова строковый тип данных. Учимся делать строковые срезы, а также изменять символы в строке.

# Срезы строк

# В предыдущем уроке мы научились работать с конкретными символами строки с помощью индексов []. Иногда нужно бывает
# работать с целыми частями строки, в таком случае мы используем срезы (slices).
# Срезы похожи на комбинацию индексации и функции range().

# Рассмотрим строку s = 'abcdefghij'.
s = 'abcdefghij'
# Положительные индексы	0	1	2	3	4	5	6	7	8	9
# Строка	a	b	c	d	e	f	g	h	i	j
# Отрицательные индексы	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1

# С помощью среза мы можем получить несколько символов исходной строки, создав диапазон индексов,
# разделенных двоеточием s[x:y].

# Следующий программный код:
print(s[2:5])
print(s[0:6])
print(s[2:7])
# выводит:
# cde
# abcdef
# cdefg

# При построении среза s[x:y] первое число – это то место, где начинается срез (включительно),
# а второе – это место, где заканчивается срез (невключительно). Разрезая строки, мы создаем подстроку,
# которая по сути является строкой внутри другой строки.

# Срез до конца, от начала

# Если опустить второй параметр в срезе s[x:] (но поставить двоеточие), то срез берется до конца строки.
# Аналогично если опустить первый параметр s[:y], то можно взять срез от начала строки.
# Срез s[:] совпадает с самой строкой s.

# Следующий программный код:
print(s[2:])
print(s[:7])
# выводит:
# cdefghij
# abcdefg

# Срез s[:] возвращает исходную строку.

# Отрицательные индексы в срезе
# Мы также можем использовать отрицательные индексы для создания срезов. Как уже говорилось ранее, отрицательные
# индексы строки начинаются с -1 и отсчитываются до достижения начала строки. При использовании отрицательных
# индексов первый параметр среза должен быть меньше второго, либо должен быть пропущен.

# Следующий программный код:
print(s[-9:-4])
print(s[-3:])
print(s[:-3])
# выводит:
# bcdef
# hij
# abcdefg

# Удалить из строки последний символ можно при помощи среза s[:-1].

# Шаг среза

# Мы можем передать в срез третий необязательный параметр, который отвечает за шаг среза.
# К примеру, срез s[1:7:2] создаст строку bdf,
# состоящую из каждого второго символа (индексы 1,3,5, правая граница не включена в срез).

# Отрицательный шаг среза

# Если в качестве шага среза указать отрицательное число, то символы будут идти в обратном порядке.

# Следующий программный код:
print(s[::-1])
# выводит:
# jihgfedcba

# Следующий программный код:
print(s[1:7:2])
print(s[3::2])
print(s[:7:3])
print(s[::2])
print(s[::-1])
print(s[::-2])
# выводит:

# bdf
# dfhj
# adg
# acegi
# jihgfedcba
# jhfdb

# Подводя итог
# s = 'abcdefghij'
# Программный код	Результат	Пояснение
# s[2:5]	cde	строка состоящая из символов с индексами 2,3,4
# s[:5]	abcde	первые пять символов строки
# s[5:]	fghij	строка состоящая из символов с индексами от 5 до конца
# s[-2:]	ij	последние два символа строки
# s[:]	abcdefghij	вся строка целиком
# s[1:7:2]	bdf	строка состоящая из каждого второго символа с индексами от 1 до 6
# s[::-1]	jihgfedcba	строка в обратном порядке, так как шаг отрицательный

# Изменение символа строки по индексу

# Предположим, у нас есть строка s = 'abcdefghij' и мы хотим заменить символ с индексом 4 на 'X'.
# Можно попытаться написать код:
s[4] = 'X'

# Однако такой код не работает. В Python строки являются неизменяемыми,
# то есть мы не можем менять их содержимое с помощью индексатора.

# Если мы хотим поменять какой-либо символ строки s, мы должны создать новую строку.
# Следующий код использует срезы и решает поставленную задачу:
s = s[:4] + 'X' + s[5:]

# Мы создаем два среза: от начала строки до 5-го символа (не включительно) и с 6-го символа (включительно) по конец
# строки, а между ними вставляем нужный нам символ, который встанет на 5-ю позицию (4 индекс).

# Примечания

# Примечание 1. Синтаксис срезов строк очень похож на синтаксис функции range().
#
# Примечание 2. Если первый параметр среза больше второго, то срез создает пустую строку.

#  Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[2:5])
# cde

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[3:])
# defg

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[:3])
# abc

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[:])
# abcdefg

# Что покажет приведенный ниже фрагмент кода?
s = 'abcdefg'
print(s[::-3])
# gda

# Дополните приведенный код, используя срезы, так чтобы он вывел первые 12 символов строки s.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# Дополните приведенный код, используя срезы, так чтобы он вывел последние 9 символов строки s.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# Дополните приведенный код, используя срезы, так чтобы он вывел каждый 7 символ строки s (начиная с 0-го индекса).

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# Дополните приведенный код, используя срезы, так чтобы он вывел строку s в обратном порядке.

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# Палиндром

# На вход программе подается одно слово, записанное в нижнем регистре. Напишите программу, которая определяет,
# является ли оно палиндромом.

# Формат входных данных
# На вход программе подается одно слово в нижнем регистре.

# Формат выходных данных
# Программа должна вывести «YES», если слово является палиндромом, и «NO» в противном случае.

# Примечание. Палиндром считается слово, которое читается одинаково в обоих направлениях. Например,
# слово «потоп» является палиндромом.

say = input()
if say[:] == say[::-1]:
    print('YES')
else:
    print('NO')
# Sample Input 1:
#
# потоп
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# анекдот
# Sample Output 2:
#
# NO

# Делаем срезы 1

# На вход программе подается одна строка. Напишите программу, которая выводит:

# общее количество символов в строке;
# исходную строку, повторенную
# 3
# 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символом.

# Формат входных данных
# На вход программе подается одна строка, длина которой больше 3 символов.

# Формат выходных данных
# Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

text = input()
print(len(text))  # общее количество символов в строке;
print(text * 3)  # исходную строку, повторенную 3 раза;
print(text[0])  # первый символ строки;
print(text[:3])  # первые три символа строки;
print(text[-3:])  # последние три символа строки;
print(text[::-1])  # строку в обратном порядке;
print(text[1:-1])  # строку с удаленным первым и последним символом.
# Sample Input:
#
# abcdefghijklmnopqrstuvwxyz
# Sample Output:
#
# 26
# abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
# a
# abc
# xyz
# zyxwvutsrqponmlkjihgfedcba
# bcdefghijklmnopqrstuvwxy

# Делаем срезы 2

# На вход программе подается одна строка. Напишите программу, которая выводит:

# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.

# Формат входных данных
# На вход программе подается одна строка, длина которой больше 5 символов.

# Формат выходных данных
# Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

text = input()
print(text[2])  # третий символ этой строки;
print(text[-2])  # предпоследний символ этой строки;
print(text[:5])  # первые пять символов этой строки;
print(text[:-3])  # всю строку, кроме последних двух символов;
print(text[::2])  # все символы с четными индексами;
print(text[1::2])  # все символы с четными индексами;
print(text[::-1])  # все символы в обратном порядке;
print(text[::-2])  # все символы строки через один в обратном порядке, начиная с последнего.
# Sample Input:
#
# abcdefghijklmnopqrstuvwxyz
# Sample Output:
#
# c
# y
# abcde
# abcdefghijklmnopqrstuvwx
# acegikmoqsuwy
# bdfhjlnprtvxz
# zyxwvutsrqponmlkjihgfedcba
# zxvtrpnljhfdb

# Две половинки

# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части,
# переставит их местами и выведет на экран.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Если длина строки нечетная, то длина первой части должна быть на один символ больше.

text = input()
if len(text) % 2 == 0 and len(text) != 0:
    print(text[-int(len(text) / 2):] + text[:int(len(text) / 2)])
elif len(text) == 1:
    print(text)
else:
    print(text[-int(len(text) // 2):] + text[:int(len(text) // 2) + 1])
# Sample Input 1:
#
# abcdef
# Sample Output 1:
#
# defabc
# Sample Input 2:
#
# abcdefg
# Sample Output 2:
#
# efgabcd
# Sample Input 3:
#
# a
# Sample Output 3:
#
# a
s = input()
n = len(s)

a = s[:(n + 1) // 2]
b = s[(n + 1) // 2:]

print(b + a)




