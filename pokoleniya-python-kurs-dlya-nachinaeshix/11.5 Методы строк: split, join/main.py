# 11.5 Методы строк - split, join

# Тема урока: строковые методы

# Метод split()
# Метод join()

# Аннотация. Строковые методы split() и join().

# В предыдущем модуле мы детально изучили основные строковые методы, однако обошли стороной
# два важных: split() и join(), имеющих отношение к спискам. Они как бы противоположны по смыслу: метод split()
# разбивает строку по произвольному разделителю на список слов, а метод join()
# собирает строку из списка слов через заданный разделитель.

# Метод split()

# Метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов.

# Следующий программный код:
s = 'Python is the most powerful language'
words = s.split()
print(words)
# выведет:
# ['Python', 'is', 'the', 'most', 'powerful', 'language']

# Таким образом, вызов метода split() разбивает строку на слова и возвращает список, содержащий все слова.

# Рассмотрим следующий программный код:
numbers = input().split()

# Если при запуске этой программы ввести строку 1 2 3 4 5, то список numbers будет следующим  ['1', '2', '3', '4', '5'].
# Обратите внимание, что список будет состоять из строк, а не из чисел. Если требуется получить именно список чисел,
# то затем нужно элементы списка по одному преобразовать в числа:
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Необязательный параметр
# У метода split() есть необязательный параметр, который определяет, какой набор символов будет использоваться в
# качестве разделителя между элементами списка. Например, вызов метода split('.') вернет список, полученный разделением
# исходной строки по символу '.'.

# Следующий программный код:
ip = '192.168.1.24'
numbers = ip.split('.')  # указываем явно разделитель
print(numbers)
# ['192', '168', '1', '24']

# выведет список:
# ['192', '168', '1', '24']

# Метод join()
# Метод join() собирает строку из элементов списка, используя в качестве разделителя строку,
# к которой применяется метод.

#  Следующий программный код:
words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
print(s)

# выведет:
# Python is the most powerful language

# Обратите внимание, все слова разделены одним пробелом, поскольку метод join() вызывался на строке,
# состоящей из одного символа пробела ' '.

# Рассмотрим еще пару примеров:
words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words))
print('-'.join(words))
print('?'.join(words))
print('!'.join(words))
print('*****'.join(words))
print('abc'.join(words))
print('123'.join(words))

# Результатом выполнения такого кода будет:
# Мы*учим*язык*Python
# Мы-учим-язык-Python
# Мы?учим?язык?Python
# Мы!учим!язык!Python
# Мы*****учим*****язык*****Python
# МыabcучимabcязыкabcPython
# Мы123учим123язык123Python

# Запомни: Строковый метод split() служит для преобразования строки в список,
# а метод join() — для преобразования списка в строку.

# Примечания
# Примечание 1. Существует большая разница между результатами вызова методов s.split() и s.split(' ').
# Разница в поведении проявляется, когда строка содержит несколько пробелов между словами.

# Следующий программный код:
s = 'Python    is   the  most  powerful  language'
words1 = s.split()
words2 = s.split(' ')
print(words1)
print(words2)

# выведет списки:
# ['Python', 'is', 'the', 'most', 'powerful', 'language']
# ['Python', '', '', '', 'is', '', '', 'the', '', 'most', '', 'powerful', '', 'language']

# Примечание 2. Методы split() и join() являются строковыми методами. Следующий код приводит к ошибке:
# print([1, 2].split())
# print([1, 2].join([3, 4, 5]))

# Примечание 3. Строковый метод join() работает только со списком строк. Следующий код приводит к ошибке:
# numbers = [1, 2, 3, 4]  # список чисел
# s = '*'.join(numbers)
# print(s)

# С помощью функции list() можно из строки получить список ее символов, а с помощью функции join()
# можно склеить элементы списка, вставляя между ними разделитель.

# Что будет выведено в результате выполнения следующего программного кода?
s = 'BEEGEEK'
chars = list(s)
s = '**'.join(chars)
print(s)
# B**E**E**G**E**E**K

# Построчный вывод

# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.

# Формат входных данных
# На вход программе подается строка текста.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

text = input()
for i in text.split():
    print(i)

seq = input().split()
print(*seq, sep="\n")
# Sample Input:
#
# У лукоморья дуб зеленый златая цепь на дубе том
# Sample Output:
#
# У
# лукоморья
# дуб
# зеленый
# златая
# цепь
# на
# дубе
# том

# Инициалы

# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека. Напишите программу,
# которая выводит инициалы человека.

# Формат входных данных
# На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
total = []
text = input()
words = text.split()
for i in words:
    total.append(i[0])
print('.'.join(total), end='.')

full_name = input().split()
print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")
# Sample Input:
#
# Владимир Семенович Высоцкий
# Sample Output:
#
# В.С.В.

# Windows OS
# В операционной системе Windows полное имя файла состоит из буквы диска,
# после которого ставится двоеточие и символ  "\",  затем через такой же символ перечисляются подкаталоги (папки),
# в которых находится файл, в конце пишется имя файла (C:\Windows\System32\calc.exe).

# На вход программе подается одна строка с корректным именем файла в операционной системе Windows. Напишите программу,
# которая разбирает строку на части, разделенные символом "\". Каждую часть вывести в отдельной строке.

# Формат входных данных
# На вход программе подается одна строка.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. В Python символ \ обычно используется для создания специальных символьных последовательностей,
# которые представляют собой управляющие символы или экранированные последовательности.
# Например, \n представляет символ новой строки, \t представляет символ табуляции и т.д.
# Однако если символ \ используется как часть строки, его следует экранировать, т.е. использовать два обратных слэша \\.

text = input().split('\\')
print(*text, sep='\n')
# Sample Input:
#
# C:\Windows\System32\calc.exe
# Sample Output:
#
# C:
# Windows
# System32
# calc.exe

# Диаграмма
# На вход программе подается строка текста, содержащая целые числа. Напишите программу,
# которая по заданным числам строит столбчатую диаграмму.

# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, разделенных символом пробела.

# Формат выходных данных
# Программа должна вывести столбчатую диаграмму.

text = input().split()
for i in text:
    print(int(i) * '+')
# Sample Input 1:
#
# 1 2 3 4 5
# Sample Output 1:
#
# +
# ++
# +++
# ++++
# +++++
# Sample Input 2:
#
# 5 3 1 7 10 2
# Sample Output 2:
#
# +++++
# +++
# +
# +++++++
# ++++++++++
# ++

# Корректный ip-адрес

# На вход программе подается строка текста, содержащая
# 4
# 4 целых неотрицательных числа, разделенных точкой. Напишите программу, которая определяет,
# является ли введенная строка текста корректным ip-адресом.

# Формат входных данных
# На вход программе подается строка текста, содержащая 4 целых числа, разделенных точкой.

# Формат выходных данных
# Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.

# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.
flag = True
ipaddres = input().split('.')
for i in ipaddres:
    if 0 <= int(i) <= 255:
        flag = True
    else:
        flag = False
        break
if flag == True:
    print('ДА')
else:
    print('НЕТ')

seq = input().split(".")

for el in seq:
    if not (0 <= int(el) <= 255):
        print("НЕТ")
        break
else:
    print("ДА")

# Sample Input 1:
#
# 192.168.0.3
# Sample Output 1:
#
# ДА
# Sample Input 2:
#
# 192.168.0.300
# Sample Output 2:
#
# НЕТ

# Добавь разделитель
# На вход программе подается строка текста и строка-разделитель. Напишите программу, которая вставляет указанный
# разделитель между каждым символом введенной строки текста.

# Формат входных данных
# На вход программе подается строка текста и строка-разделитель, каждая на отдельной строке

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
total = []
text = input()
delimiter = input()  # разделитель
for i in text:
    total.append(i)
print(delimiter.join(total))

seq = input()
sep = input()

res = sep.join(list(seq))
print(res)
# Sample Input 1:
#
# 1234567
# *
# Sample Output 1:
#
# 1*2*3*4*5*6*7
# Sample Input 2:
#
# qwerty and password
# **
# Sample Output 2:
#
# q**w**e**r**t**y** **a**n**d** **p**a**s**s**w**o**r**d

# Количество совпадающих пар
# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

# Формат входных данных
# На вход программе подается строка текста, содержащая целые числа, отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести одно число – количество пар элементов, равных друг другу.
total = 0
text = input().split()
for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            total += 1
print(total)

num, count = input().split(), 0

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            count += 1

print(count)
# Sample Input 1:
#
# 1 7 5 7 5
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 3 3 3 3 3
# Sample Output 2:
#
# 10
# Sample Input 3:
#
# 8 7 6
# Sample Output 3:
#
# 0

