# 7.9 Вложенные циклы. Часть 2

# Численный треугольник 2

# Дано натуральное число n.
# Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.

# Примечание. Используйте вложенный цикл for.

number = int(input())
total = 0
for i in range(number):
    for j in range(i + 1):
        total += 1
        print(total, end=' ')
    print()
# Sample Input:
#
# 3
# Sample Output:
#
# 1
# 2 3
# 4 5 6

# Численный треугольник 3
# Дано натуральное число n.
# Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:

# 1
# 121
# 12321
# 1234321
# 123454321
# ...

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.

# Примечание. Используйте вложенный цикл for.

number = int(input())
for i in range(1, number + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()
# Sample Input 1:
#
# 2
# Sample Output 1:
#
# 1
# 121
# Sample Input 2:
#
# 3
# Sample Output 2:
#
# 1
# 121
# 12321
# Sample Input 3:
#
# 5
# Sample Output 3:
#
# 1
# 121
# 12321
# 1234321
# 123454321

# Делители-1 🌶️
# На вход программе подается два натуральных числа b (a< b).
# Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой
# делителей и сумму его делителей. Если таких чисел несколько, то выведите наибольшее из них.

# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом: число с максимальной суммой делителей и
# сумму его делителей.

a, b = int(input()), int(input())

mx_num = -1
mx_sum = -1
for cur_num in range(a, b + 1):
    cur_sum = 0
    for j in range(1, cur_num + 1):
        if cur_num % j == 0:
            cur_sum += j

    if cur_sum >= mx_sum:
        mx_num = cur_num
        mx_sum = cur_sum

print(mx_num, mx_sum)
# Sample Input 1:
#
# 1
# 10
# Sample Output 1:
#
# 10 18
# Sample Input 2:
#
# 1
# 100
# Sample Output 2:
#
# 96 252

# Делители-2

# На вход программе подается натуральное число n.
# Напишите программу, выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести графическое изображение чисел от 1 до n, каждое на отдельной строке

number = int(input())
for i in range(1, number + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(i, '+' * count, sep='')
# Sample Input:
#
# 5
# Sample Output:
#
# 1+
# 2++
# 3++
# 4+++
# 5++

# Цифровой корень

# На вход программе подается натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа,
# затем все цифры найденной суммы и повторять этот процесс до тех пор, пока в результате
# не будет получено однозначное число (цифра), которое и называется цифровым корнем изначального числа.

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести цифровой корень введенного числа.

# Примечание. Используйте вложенные циклы while.

number = int(input())
while number > 9:
    total = 0
    while number > 0:
        last_digit = number % 10
        total += last_digit
        number //= 10
    number = total
print(number)
# Sample Input:
#
# 192
# Sample Output:
#
# 3

# Сумма факториалов

# Дано натуральное число n.
# Напишите программу, которая выводит значение суммы 1!+2!+3!+…+n!.

# Формат входных данных
# На вход программе подается одно натуральное число.

# Формат выходных данных
# Программа должна вывести значение суммы 1!+2!+3!+…+n!.

# Примечание 1. Факториалом натурального числа n, называется произведение всех натуральных чисел от 1 до n, то есть

# n!=1⋅2⋅3⋅…⋅n

# Примечание 2. Задачу можно решить без вложенного цикла. Напишите две версии программы =)
from math import *
number = int(input())
total = 0
for i in range(1, number + 1):
    total += factorial(i)
print(total)
# Sample Input 1:
#
# 3
# Sample Output 1:
#
# 9
# Sample Input 2:
#
# 1
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# 2
# Sample Output 3:
#
# 3

# Простые числа

# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит все простые числа от a до b включительно.

# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести все простые числа от a до b включительно, каждое на отдельной строке.

# Примечание. Число 1 простым не является.

a, b = int(input()), int(input())
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1
    if total == 2:
        print(j)
# Sample Input 1:
#
# 2
# 15
# Sample Output 1:
#
# 2
# 3
# 5
# 7
# 11
# 13
# Sample Input 2:
#
# 1
# 5
# Sample Output 2:
#
# 2
# 3
# 5



