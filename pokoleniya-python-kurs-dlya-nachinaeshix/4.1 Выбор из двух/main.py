# 4.1 Выбор из двух
from calendar import c

import a
from six import b

# Тема урока: условный оператор

# Условный оператор
# Отступы
# Операторы сравнения
# Решение задач

# Аннотация. Урок посвящен условному оператору if-else.

# Условный оператор if-else

# Мы познакомились с базовыми строительными блоками программ, научились писать программы, обеспечивающие ввод, обработку и вывод данных. Более того, умеем работать со строками и числами, как мы делаем это в математике. Теперь научимся управлять ходом выполнения программы.
#
# Программы должны уметь выполнять разные действия в зависимости от введенных данных. Для принятия решения программа проверяет, истинно или ложно определенное условие.
#
# В Python существует несколько способов проверки, и в каждом случае возможны два исхода: истина (True) или ложь (False).
#
# Проверка условий и принятие решений по результатам этой проверки называется ветвлением (branching). Программа таким способом выбирает, по какой из возможных ветвей ей двигаться дальше.
#
# В Python проверка условия осуществляется при помощи ключевого слова if.
#
# Рассмотрим следующую программу:
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')

# Программа просит пользователя ввести текст и проверяет результат ввода. Если введенный текст равен строке «Python», то выводит пользователю текст:
# Верно! Мы ботаем Python =)
# Python - отличный язык!

# Двоеточие (:) в конце строки с инструкцией if сообщает интерпретатору Python, что дальше находится блок команд. В блок команд входят все строки с отступом под строкой с инструкцией if, вплоть до следующей строки без отступа.
#
# Если условие истинно, выполняется весь расположенный ниже блок. В предыдущем примере блок инструкций составляет третья и четвёртая строки программы.

# Блоком кода называют объединённые друг с другом строки. Они всегда связаны с определённой частью программы (например, с инструкцией if). В Python блоки кода формируются при помощи отступов.

# Предыдущая программа выводит текст в случае, если условие истинно. Но если условие ложно, то программа ничего не выводит. Для того, чтобы обеспечить возможность выполнять что-либо, если условие оказалось ложным, мы используем ключевое слово else.

answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')

# В новой программе мы обрабатываем сразу два случая: если условие истинно (пользователь ввел «Python»), и если условие ложно (пользователь ввел что угодно, кроме «Python»).

# Отступы
# В некоторых языках программирования отступы — дело личного вкуса, и можно вообще обходиться без них. Однако в Python они неотъемлемая часть кода. Именно отступ сообщает интерпретатору Python, где начинается и где заканчивается блок кода.
# Отступ — небольшое смещение строки кода вправо. В начале такой строки находятся пробелы, и поэтому она на несколько символов отстоит от левого края.
# Некоторым инструкциям в Python (например, инструкции if) именно блок кода сообщает, какие действия следует предпринять. После if блок кода информирует интерпретатор Python, как действовать, если условие истинно, и как — если оно ложно

# Операторы сравнения
# Можно заметить, что в проверке условия мы использовали двойное равенство (==), вместо ожидаемого одиночного (=). Не стоит путать оператор присваивания (=) с условным оператором (==).
#
# Оператор присваивания (=) присваивает переменным значения:
num = 1992
s = 'I love Python'

# Для проверки двух элементов на равенство Python использует удвоенный знак равно (==). Вот так:
# if answer == 'Python':
#
# if name == 'Gvido':
#
# if temperature == 40:

# Путаница с операторами == и = является одной из самых распространенных ошибок в программировании. Эти символы используются не только в Python, и каждый день множество программистов используют их неправильно.
# В Python существует 6 основных операторов сравнения.
# Выражение  	Описание
# if x > 7	если x больше 7
# if x < 7	если x меньше 7
# if x >= 7	если x больше либо равен  7
# if x <= 7	если x меньше либо равен  7
# if x == 7	если x равен  7
# if x != 7	если x не равен  7

# Рассмотрим пример:
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:                   # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)


# Цепочки сравнений

# Операторы сравнения в Python можно объединять в цепочки (в отличии от большинства других языков программирования, где для этого нужно использовать логические связки), например, a == b == c или 1 <= x <= 10. Следующий код проверяет, находится ли значение переменной age в диапазоне от 3 до 6:
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')

# Код, проверяющий равенство трех переменных, может выглядеть так:
if a == b == c:
    print('Числа равны')
else:
    print('числа не равны')

# Транзитивность

# Операция равенства является транзитивной. Это означает, что если a == b и b == c, то из этого следует, что a == c. Именно поэтому предыдущий код, проверяющий равенство трёх переменных, работает как полагается.

# Из курса математики вам могут быть знакомы другие примеры транзитивных операций:

# Отношение порядка: если a > b и b > c, то a > c:
# Параллельность прямых: если a || b и b || c, то a || c:
# Делимость: если a делится на b и b делится на c, то a делится на c.

# Наглядно транзитивность отношения порядка можно понять на таком примере: если сосед слева старше вас
# (a > b), а вы старше соседа справа (b > c), то сосед слева точно старше соседа справа (a > c).

# Операция неравенства (!=) в отличие от операции равенства (==), является нетранзитивной. То есть из того, что
# a != b и b != c, вовсе не следует, что a != c. Действительно, если вас зовут не так, как соседа слева и не так, как соседа справа, то нет гарантии, что у обоих соседей не окажутся одинаковые имена.

# Таким образом, следующий код вовсе не проверяет тот факт, что все три переменные различны:
a, b, c = int(input()), int(input()), int(input())
if a != b != c:
    print('числа не равны')
else:
    print('числа равны')
# 1
# 2
# 3
# числа не равны

# 1
# 2
# 2
# числа равны

# 1
# 1
# 2
# числа равны

# Код, проверяющий, что значения трёх переменных различны, мы научимся писать немного позже.

# Решение задач
# Задача 1. Напишите программу, которая считывает одну строку. Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».
# Решение. Программа, решающая поставленную задачу, может иметь вид:
word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')
# Python
# ДА

# Java
# НЕТ

# Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр. Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».
# Решение. Программа, решающая поставленную задачу, может иметь вид:
num = int(input())
last_digit = num % 10  # последняя цифра число
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
# 11
# ДА

# 12
# НЕТ

# Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
# Решение. Программа, решающая поставленную задачу, может иметь вид:
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)
# 4
# 5
# 6

# 2

# Работа каких фрагментов кода правильно определяет, чётное или нет число содержится в переменной i?
i = int(input())
if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

if i % 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')

# Пароль
# При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.
#
# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».

# Формат входных данных
# На вход программе подаются две строки.
#
# Формат выходных данных
# Программа должна вывести одну строку в соответствии с условием задачи.

password1 = input()
password2 = input()
if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')
# qwerty
# qwerty

# Пароль принят

# qwerty
# Qwerty
#
# Пароль не принят

# Четное или нечетное?
# Напишите программу, которая определяет, является число четным или нечетным.
#
# Формат входных данных
# На вход программе подаётся одно целое число.
#
# Формат выходных данных
# Программа должна вывести «Четное», если число четное, и «Нечетное» — если число нечетное.

number = int(input())
if number % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
# 10
#
# Четное

# 17
#
# Нечетное

# Соотношение
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
number = int(input())
first_digit = number // 1000
second_digit = (number % 1000) // 100
third_digit = (number % 100) // 10
fourth_digit = number % 10
if first_digit + fourth_digit == second_digit - third_digit:
    print('ДА')
else:
    print('НЕТ')
# 1614
#
# ДА

# 1234
#
# НЕТ

# Роскомнадзор
# Напишите программу, которая определяет, разрешен ли пользователю доступ к интернет-ресурсу или нет.
#
# Формат входных данных
# На вход программе подаётся целое число — возраст пользователя.
#
# Формат выходных данных
# Программа должна вывести текст «Доступ разрешен», если возраст не менее 18, и «Доступ запрещен» - в противном случае.

how_old_are_you = int(input())
if how_old_are_you >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')
# 16
#
# Доступ запрещен

# 18
#
# Доступ разрешен

# Арифметическая прогрессия

# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.

# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.

a1 = int(input())
a2 = int(input())
a3 = int(input())
if a3 == a2 + (a2 - a1):
    print('YES')
else:
    print('NO')
# 1
# 2
# 3
#
# YES

# Наименьшее из двух чисел

# Напишите программу, которая определяет наименьшее из двух чисел.

# Формат входных данных
# На вход программе подаётся два различных целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.

number1 = int(input())
number2 = int(input())
if number1 > number2:
    print(number2)
else:
    print(number1)
# 8
# 11
#
# 8

# Наименьшее из четырёх чисел 🌶️

# Напишите программу, которая определяет наименьшее из четырёх чисел.

# Формат входных данных
# На вход программе подаётся четыре целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

# Примечание. Учитывайте, что минимальные числа могут повторяться (cмотрите тест №5).

number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())

number1number2 = 0
number3number4 = 0

if number1 <= number2:
    number1number2 = number1
else:
    number1number2 = number2

if number3 <= number4:
    number3number4 = number3
else:
    number3number4 = number4

if number1number2 <= number3number4:
    print(number1number2)
else:
    print(number3number4)
# 1
# 2
# 3
# 4
#
# 1

# Возрастная группа

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно - детство
# от 14 до 25 - молодость
# от 25 до 59 - зрелость
# от 60 - старость

# Формат входных данных
# На вход программе подаётся одно целое число – возраст пользователя.

# Формат выходных данных
# Программа должна вывести название возрастной группы.

your_age = int(input())

if your_age <= 13:
    print('детство')
else:
    if 14 <= your_age <= 24:
        print('молодость')
    else:
        if 25 <= your_age <= 59:
            print('зрелость')
        else:
            print('старость')

# Sample Input 1:
#
# 4
# Sample Output 1:
#
# детство
# Sample Input 2:
#
# 91
# Sample Output 2:
#
# старость
# Sample Input 3:
#
# 40
# Sample Output 3:
#
# зрелость

# Только + 🌶️
# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

# Формат входных данных
# На вход программе подаются три целых числа.

# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.

# Примечание. Если положительных чисел нет, то следует вывести 0.

number1 = int(input())
number2 = int(input())
number3 = int(input())

total = 0

if number1 > 0:
    total += number1
if number2 > 0:
    total += number2
if number3 > 0:
    total += number3

print(total)

# Sample Input 1:
#
# 4
# -22
# 1
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# 33
# 55
# 63
# Sample Output 2:
#
# 151
# Sample Input 3:
#
# -1
# 37
# 62
# Sample Output 3:
#
# 99






