# 13.5 Функции с возвратом значения. Часть 2

# Тема урока: функции с возвратом значения
# Функции с возвратом значения
# Решение задач

# Аннотация. Кроме функций, возвращающих числовые значения, можно писать и возвращающие логические,
# строковые и другие значения.

# Возвращение булевых значений

# Python позволяет писать булевы функции, возвращающие либо истину (True), либо ложь (False).
# Булеву функцию можно применять для проверки условия, тогда значения True и False
# будут сигнализировать о его выполнении.

# Булевы функции широко применяются для упрощения сложных условий,
# проверяемых в структурах принятия решения и структурах с повторением.
# Например, напишем программу, которая просит пользователя ввести число и определяет, четное оно или нечетное.

# Это можно сделать так:
number = int(input())
if number % 2 == 0:
    print('Это число четное.')
else:
    print('Это число нечетное')
# 3
# Это число нечетное

# Этот фрагмент кода будет легче понять, если написать булеву функцию is_even(), которая принимает число в качестве
# аргумента и возвращает True, если оно четное, и False если нечетное.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
# Теперь можно переписать инструкцию if-else основной программы так, чтобы она для определения четности переменной
# number вызывала функцию is_even():
number = int(input())
if is_even(number):
    print('Это число четное.')
else:
    print('Это число нечетное.')
# 4
# Это число четное.

# Так логику программы легче понять, а функцию можно вызывать в программе всякий раз,
# когда необходимо проверить четность числа.

# Использование булевых функций для валидации входных данных

# Булевы функции можно также использовать для упрощения сложного кода валидации входных данных.
# Например в программе, предлагающей пользователю ввести номер модели изделия,
# где возможны только значения 100, 200 или 300, можем написать такой код:

model = int(input())

while model != 100 and model != 200 and model != 300:
    print('Допустимыми номерами моделей являются 100, 200 или 300.')
    model = int(input())
# Цикл валидации использует длинное составное булево выражение, и повторяется до тех пор,
# пока model не будет равняться 100, 200 или 300.

# Вместе с тем, цикл валидации можно упростить, написав булеву функцию проверки переменной model и вызывая ее в цикле.
# Напишем функцию is_invalid(), которая принимает один параметр model и возвращает значение True, если модель
# недопустима и False в противном случае. Тогда цикл валидации можно переписать следующим образом:

while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())

# После этого изменения цикл становится легче читать. Теперь вполне очевидно, что цикл повторяется до тех пор,
# пока номер модели недопустим. Приведенный ниже фрагмент кода показывает, как можно было бы написать
# функцию is_invalid(). Она принимает номер модели в качестве аргумента, и если аргумент не равен 100, 200 или 300,
# то эта функция возвращает True, говоря, что он недопустимый. В противном случае функция возвращает False.
def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False

# Создание функций, реализующих такую простую логику, — не всегда оптимальное решение, так как увеличивает размер кода
# и ведет к затратам времени на вызов функции и возврат обратно результата, что может сказаться негативно на
# производительности программы.

# Is Valid Triangle?

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов три натуральных
# числа, и возвращает значение True если существует невырожденный треугольник со сторонами side1, side2, side3 и False
# в противном случае.

# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.

# объявление функции
def is_valid_triangle(side1, side2, side3):
    if a + b > c and c + a > b and c + b > a:
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

# Примечание 2. Следующий программный код:
print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
# должен выводить:
# True
# False
# True

# объявление функции
def is_valid_triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])  # создаём отсортированный список из сторон

    return sides[0] + sides[1] > sides[2]  # проверяем, минимальная и средняя стороны больше максимальной


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

# Примечание 2. Следующий программный код:
print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))
# должен выводить:
# True
# False
# True

# Is a Number Prime? 🌶️

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение
# True если число является простым и False в противном случае.

# объявление функции
def is_prime(num):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# Примечание. Следующий программный код:
print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
# должен выводить:
# False
# False
# True

# Next Prime 🌶️🌶️

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает
# первое простое число большее числа num.

# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

def is_prime(num):
    if num == 1:
        return False  # число 1 не является простым

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель

    return True


# объявление функции
def get_next_prime(num):
    cur_num = num + 1  # начинаем искать следующее простое число

    while not is_prime(cur_num):  # если следующее число непростое, то увеличиваем на 1
        cur_num += 1

    return cur_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
# Примечание 2. Следующий программный код:
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
# должен выводить:
# 7
# 11
# 17

# Good password 🌶️

# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является надежным и False - в противном случае.

# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
# Примечание. Следующий программный код:
print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
# должен выводить:
# True
# False

# Ровно в одном

# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False
# в противном случае.

# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        return False
    total = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            total += 1

    return total == 1
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# объявление функции
def is_one_away(word1, word2):
    mismatches = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1

        return mismatches == 1

    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# Примечание. Следующий программный код:
print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
# должен выводить:
# True
# True
# False
# False

# Палиндром 🌶️

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы,
# а также символы , . ! ? -.

# объявление функции
def is_palindrome(text):
    # Преобразование текста к нижнему регитстру
    text = text.lower()

    # Удаление пробелов и символов пунктуации.
    for i in ' ,.!?-':
        text = text.replace(i, '')



    # Сравнение текста с его обратным
    return text == text[::-1]
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# Примечание 3. Следующий программный код:
print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
# должен выводить:
# True
# True
# False

# BEEGEEK

# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и
# False - в противном случае.

# объявление функции
def is_valid_password(password):
    password = password.split(':')
    a = password[0]
    b = int(password[1])
    c = int(password[2])
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    if len(password) == 3:
        flag1 = True
    if a == a[::-1]:
        flag2 = True
    for i in range(2, b):
        if b % i == 0:
            break
        else:
            flag3 = True
    if c % 2 == 0:
        flag4 = True
    return flag1 and flag2 and flag3 and flag4
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def is_even(num):
    return num % 2 == 0


# объявление функции
def is_valid_password(password):
    seq = password.split(":")

    if len(seq) == 3:
        seq = [int(el) for el in seq]
        a, b, c = seq[0], seq[1], seq[2]

        return is_palindrome(a) and is_prime(b) and is_even(c)

    return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
# Примечание. Следующий программный код:
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
# должен выводить:
# True
# False
# False
# False

# Правильная скобочная последовательность 🌶️

# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text, состоящую из
# символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной
# последовательностью и False в противном случае.

# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка (при этом каждая открывающая скобка должна быть
# левее соответствующей ей закрывающей скобки).

# объявление функции
def is_correct_bracket(text):
    if not text:
        return False

    total = 0
    for i in text:
        if i == '(':
            total += 1
        elif i == ')':
            total -= 1
            if total < 0:
                return False

    return total == 0

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# объявление функции
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")

    return text == ""


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
# Примечание 2. Следующий программный код:
print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
# должен выводить:
# True
# False

# Змеиный регистр
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».

# Примечание 1. Почитать подробнее о стилях именования можно тут.

# объявление функции
def convert_to_python_case(text):
    result = []
    for i, char in enumerate(text):
        if char.isupper() and i != 0:
            result.append("_")
        result.append(char.lower())

    return "".join(result)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
# Примечание 2. Следующий программный код:
print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
# this_is_camel_cased
# is_prime_number

