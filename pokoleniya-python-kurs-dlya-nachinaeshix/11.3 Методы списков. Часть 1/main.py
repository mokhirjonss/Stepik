# 11.3 Методы списков. Часть 1

# Тема урока: методы добавления и удаления элементов

# Метод добавления элемента append()
# Метод расширения списка extend()
# Оператор del
# Решение задач

# Аннотация. Добавление элементов в список. Оператор del, удаляющий элементы по заданному индексу.

# Добавление элементов

# Мы научились создавать статические списки, то есть списки, элементы которых известны на этапе создания.
# Следующий шаг – научиться добавлять элементы в уже существующие списки.

# Метод append()

# Для добавления нового элемента в конец списка используется метод append().

# Следующий программный код:
numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список

numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка

print(numbers)

# выведет:
# [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Обратите внимание, для того чтобы использовать метод append(), нужно, чтобы список был создан
# (при этом он может быть пустым).

# Следующий программный код:
numbers = []  # создаем пустой список

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers)

# выведет:
# [1, 2, 3]

# Важно: мы не можем использовать индексаторы для установки значений элементов списка, если список пустой.
# Следующий программный код:

# numbers = []  # создаем пустой список
#
# numbers[0] = 1
# numbers[1] = 2
# numbers[2] = 3

# print(numbers)

# приводит к ошибке:

# IndexError: list assignment index out of range

# Метод extend()

# Можно также расширить список другим списком путем вызова метода extend().
# Следующий программный код:
numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds)
print(numbers)

# выведет:
# [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

# Метод extend() как бы расширяет один список, добавляя к нему элементы другого списка.
# Отличие между методами append() и extend() проявляется при добавлении строки к списку.
# Следующий программный код:

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)

# выведет:
# ['iq option', 'stepik', 'beegeek', 'python']
# ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

# Метод append() добавляет строку 'python' целиком к списку, а метод extend() разбивает строку 'python' на
# символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка.

# Удаление элементов
# С помощью оператора del можно удалять элементы списка по определенному индексу.
# Следующий программный код:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]  # удаляем элемент имеющий индекс 5

print(numbers)

# выведет:
# [1, 2, 3, 4, 5, 7, 8, 9]

# Элемент под указанным индексом удаляется, а список перестраивается.

# Обратите внимание на синтаксис удаления, так как он отличается от обычного вызова метода. При удалении элементов
# не надо передавать аргумент внутри круглых скобок.

# Оператор del работает и со срезами: мы можем удалить целый диапазон элементов списка.

# Следующий программный код:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]  # удаляем элементы с 2 по 6 включительно

print(numbers)

# выведет:
# [1, 2, 8, 9]

# Мы можем удалить все элементы на четных позициях (0, 2, 4, ...) исходного списка.
# Следующий программный код:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]

print(numbers)

# выведет:
# [2, 4, 6, 8]

# Допустим, программа состоит из строки кода:
names = []
# Какую из приведенных ниже инструкций следует применить для добавления в список по 0 индексу
# строкового значения 'Chromatica'?

# names.append('Chromatica')

# Что будет выведено в результате выполнения следующего программного кода?
numbers = [4, 2, 8, 6, 5]
numbers.append(7)
numbers.append(1)
print(numbers)
# [4, 2, 8, 6, 5, 7, 1]

# Что будет выведено в результате выполнения следующего программного кода?
numbers = [4, 2]
numbers.extend([1, 2, 3])
numbers.extend([7, 17, 777])
print(numbers)
# [4, 2, 1, 2, 3, 7, 17, 777]

# Что будет выведено в результате выполнения следующего программного кода?
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
del colors[2]
del colors[6]
print(colors)
# ['red', 'orange', 'green', 'blue', 'purple', 'brown']

# Все сразу 1 🌶️

# Дополните приведенный код, чтобы он:

# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел YES, если список содержит числа 17, и NO в противном случае;
# Вывел список с удаленными первым и последним элементами.

# Примечание. Каждый вывод осуществлять с новой строки.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))  # длина списка
print(numbers[-1])  # последний элемент списка
print(numbers[::-1])  # список в обратном порядке
if '5' and '17' in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)

# Список строк
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список и выводит его.

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести список состоящий из указанных строк.
total = []
numbers = int(input())
for i in range(numbers):
    text = input()
    total.append(text)
print(total)
# Sample Input:
#
# 5
# C#
# C++
# C
# Python
# F#
# Sample Output:
#
# ['C#', 'C++', 'C', 'Python', 'F#']

# Алфавит
# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

# Формат выходных данных
# Программа должна вывести указанный список.

# Примечание 1. Последний элемент списка должен состоять из 26 символов z.

# Примечание 2. Английский алфавит (для копирования) 😇:
# abcdefghijklmnopqrstuvwxyz

total = []
for i in range(26):
    total.append(chr(ord('a') + i)*(i+1))
print(total)

# Список кубов
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список их кубов.

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести список, состоящий из кубов указанных чисел.
total = []
numbers = int(input())
for i in range(numbers):
    num = int(input())
    total.append(num**3)
print(total)
# Sample Input 1:
#
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
#
# [1, 8, 27, 64, 125]
# Sample Input 2:
#
# 2
# -5
# -2
# Sample Output 2:
#
# [-125, -8]
# Sample Input 3:
#
# 1
# 100
# Sample Output 3:
#
# [1000000]

# Список делителей
# На вход программе подается натуральное число n.
# Напишите программу, которая создает список, состоящий из делителей введенного числа.

# Формат входных данных
# На вход программе подается натуральное число n.

# Формат выходных данных
# Программа должна вывести список, состоящий из делителей введенного числа.
total = []
numbers = int(input())
for i in range(1, numbers + 1):
    if numbers % i == 0:
        total.append(i)
print(total)
# Sample Input 1:
#
# 17
# Sample Output 1:
#
# [1, 17]
# Sample Input 2:
#
# 25
# Sample Output 2:
#
# [1, 5, 25]
# Sample Input 3:
#
# 36
# Sample Output 3:
#
# [1, 2, 3, 4, 6, 9, 12, 18, 36]

# Суммы двух
# На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел.
# Напишите программу, которая создает из указанных чисел список,
# состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести список, состоящий из сумм соседних чисел.
total = 0
count = []
numbers = int(input())
for i in range(numbers):
    num = int(input())
    total += num
    count.append(total)
    total = num
print(count[1:])

seq = []
for _ in range(int(input())):
    seq.append(int(input()))

res = []
for i in range(len(seq) - 1):
    res.append(seq[i] + seq[i + 1])

print(res)

# Sample Input 1:
#
# 5
# 1
# 2
# 3
# 4
# 5
# Sample Output 1:
#
# [3, 5, 7, 9]
# Sample Input 2:
#
# 2
# 10
# 9
# Sample Output 2:
#
# [19]

# Удалите нечетные индексы
# На вход программе подается натуральное число n, а затем n целых чисел.
# Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по
# нечетным индексам, а затем выводит полученный список.

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести список в соответствии с условием задачи.

# Примечание. Используйте оператор del.
total = []
numbers = int(input())
for i in range(numbers):
    num = int(input())
    total.append(num)

del total[1::2]
print(total)
# Sample Input 1:
#
# 10
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Sample Output 1:
#
# [0, 2, 4, 6, 8]
# Sample Input 2:
#
# 1
# 8
# Sample Output 2:
#
# [8]
# Sample Input 3:
#
# 2
# 9
# 6
# Sample Output 3:
#
# [9]

# k-ая буква слова 🌶️🌶️
# На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

# Формат входных данных
# На вход программе подается натуральное число n, далее n строк, каждая на отдельной строке.
# В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером,
# то такие строки при выводе нужно игнорировать.
numbers = int(input())
cloud = []
string = ''
for i in range(numbers):
    text = input()
    cloud.append(text)
k = int(input())
for i in range(len(cloud)):
    m = cloud[i]
    if k <= len(m):
        x = m[k - 1]
        string += x
print(string)
# Sample Input:
#
# 5
# abcdef
# bcdefg
# cdefgh
# defghi
# efghij
# 2
# Sample Output:
#
# bcdef

# Символы всех строк
# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает список из символов всех строк, а затем выводит его.

# Формат входных данных
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.

# Формат выходных данных
# Программа должна вывести список состоящий из символов всех введенных строк.

# Примечание. В результирующем списке могут содержаться одинаковые символы.
total = []
numbers = int(input())
for i in range(numbers):
    text = input()
    total.extend(text)
print(total)
# Sample Input:
#
# 3
# abc
# def
# ghi
# Sample Output:
#
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


