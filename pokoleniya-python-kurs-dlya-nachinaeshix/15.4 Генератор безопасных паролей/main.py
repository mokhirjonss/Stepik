# 15.4 Генератор безопасных паролей

# Генератор безопасных паролей

# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

# Составляющие проекта:

# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.

# Заголовок программы

# Подключите модуль random;
# Создайте строковые константы:

# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.

# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

# Считывание пользовательских данных
# Программа должна запрашивать у пользователя следующую информацию:

# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?

# Настройка генерируемых паролей
# На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут
# быть в генерируемом пароле.

# Генерации пароля
# Напишите функцию generate_password(), которая принимает два аргумента:
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
# Используя цикл for, сгенерируйте необходимое количество паролей.

# Друзья, делитесь в комментариях своей реализацией проекта =)

# 1. Заголовок программы:
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
# 2.  Считывание пользовательских данных:
n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo00? (д = да, н = нет) ').strip()
# 3. Настройка генерируемых паролей:
if add_digit.lower() == 'д':
    chars += digits
if add_lowercase.lower() == 'д':
    chars += lowercase_letters
if add_uppercase.lower() == 'д':
    chars += uppercase_letters
if add_punctuation.lower() == 'д':
    chars += punctuation
if remove_badsymbols.lower() == 'д':
    for c in 'il1Lo00':
        chars = chars.replace(c, '')
# 4. Функция генерации пароля:
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password
# 5. Генерация нужного количества паролей:
for _ in range(n):
    generate_password(length, chars)
    