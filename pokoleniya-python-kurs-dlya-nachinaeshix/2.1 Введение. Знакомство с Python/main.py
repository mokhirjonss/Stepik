# 2.1 Введение. Знакомство с Python

# Тема урока: введение в программирование
# История языка Python
# Сильные и слабые стороны Python
# Python 2 VS Python 3
# Установка Python на компьютер
# Установка VS Code и (или) Wing IDE на компьютер
# Аннотация. Что такое программа и какие существуют языки программирования? Чем хорош язык Python? Как установить на компьютер интерпретатор Python и среды разработки VS Code и (или) Wing IDE?
#
# Введение
# Компьютерная программа — список команд (инструкций) для компьютера. Команды могут быть любыми, например:
#
# считать информацию с клавиатуры;
# произвести арифметические вычисления (+, −, *, /);
# вывести информацию на экран.
# В каждом компьютере установлено много разнообразных программ. Например, Google Chrome, через которую вы, скорее всего, проходите этот курс, — это программа-браузер. Она позволяет просматривать страницы сайтов в интернете. Программа Skype позволяет совершать звонки и обмениваться мгновенными сообщениями. В конце концов, сама операционная система, будь то Windows, OS X или Linux, тоже программа.
#
# Для создания программ используются языки программирования. Выбор языка программирования, как правило, продиктован особенностями самой программы.
#
# Язык программирования
# Язык программирования — набор определенных правил, по которым компьютер может понимать команды (инструкции) и выполнять их. Текст программы на любом языке программирования называется программным кодом.
#
# Языки программирования бывают компилируемые и интерпретируемые. Если программа написана на компилируемом языке (C, C++, Pascal), то перед выполнением её нужно полностью проверить на наличие синтаксических ошибок и уже после этого перевести в понятную для компьютера форму — машинный код. Это делает специальная программа, которая называется компилятором.
#
# Если программа написана на интерпретируемом языке (Python, PHP, Ruby), она не переводится в машинный код целиком. Вместо этого специальная программа, которая называется интерпретатором, идет по коду, анализирует его и выполняет каждую отдельную команду.
#
# Существуют языки программирования, которые совмещают оба подхода (C#, Java). В таких языках код исходной программы сначала компилируется в промежуточный код (байт-код), а уже потом, во время выполнения, переводится в машинный код.
#
# Язык Python
# Язык Python разработал голландский программист Гвидо Ван Россум (Guido van Rossum) в 1991 году. Гвидо был фанатом британского комедийного сериала «Monty Python’s Flying Circus», откуда и пришло название языка.
#
# Guido van Rossum OSCON 2006.jpg
# Гвидо Ван Россум
# Картинки по запросу Monty Python’s Flying Circus
# Monty Python’s Flying Circus
# Python 2 VS Python 3
# Основные версии языка Python – Python 2 и Python 3. Версия Python 2 считается устаревающей, версия 3 — более новой и современной. Почему не откажутся от второй версии? Если коротко, Python 3 не имеет полной обратной совместимости с предыдущей версией, а на Python 2 написано очень много программ. У разработчиков нет возможности переписать всё на новую версию.
#
# В нашем курсе мы будем пользоваться только Python 3 и не будем говорить о Python 2.
#
# Преимущества Python
# Это интерпретируемый язык программирования:
# он не требует отдельного этапа компиляции;
# программа на языке Python запускается прямо из исходного кода;
# Это высокоуровневый язык программирования;
# Это платформонезависимый язык:
# программы на Python можно создавать на разных операционных системах (Linux, Windows, OS X);
# программы на Python можно запускать на разных операционных системах (Linux, Windows, OS X);
# Это open source проект;
# Это простой язык;
# Это встраиваемый скриптовый язык;
# Это динамический язык, что упрощает написание несложных программ;
# Для Python существует огромная библиотека классов на любой вкус.
# Недостатки Python
# Низкая скорость выполнения по сравнению с такими языками, как C и C++;
# Динамическая типизация языка — минус при написании сложных программ.
# Задачи, решаемые с помощью Python
# Python подходит для решения широкого спектра задач. Разобьем их на категории:
#
# Системное программирование. Встроенные в  Python интерфейсы доступа к службам операционных систем делают его идеальным инструментом для создания переносимых программ и утилит системного администрирования;
#
# Графические приложения. Простота Python и быстрота разработки делают его отличным средством создания графического интерфейса. В состав Python входит стандартный объектно-ориентированный интерфейс к GUI API;
#
# Веб-приложения. С помощью дополнительных фреймворков на языке Python (Django, Flask, Pyramid) можно создавать полнофункциональные сайты;
#
# Веб-сценарии. Python поставляется вместе со стандартными интернет-модулями, которые позволяют программам выполнять разнообразные сетевые операции как в режиме клиента, так и в режиме сервера;
#
# Интеграция компонентов. Возможность Python расширяться и встраиваться в системы на языке C++ делает его удобным для описания поведения других систем и компонентов;
#
# Приложения баз данных. В Python имеются интерфейсы доступа ко всем основным реляционным базам данных: Sybase, Oracle, Informix, ODBC, MySQL, PostgreSQL, SQLite и многим другим. С их помощью можно создавать приложения баз данных.
#
# Проекты, в которых используется Python
# Компания Google использует Python в своей поисковой системе;
#
# Компании Intel, Cisco, Hewlett-Packard, Seagate, Qualcomm и IBM, используют Python для тестирования аппаратного обеспечения;
#
# Сервис YouTube в значительной степени реализован на Python;
#
# Агентство национальной безопасности (NSA) использует Python для шифрования и анализа данных;
#
# Компании JPMorgan Chase, UBS, Getco и Citadel применяют Python для прогнозирования финансового рынка;
#
# Программа BitTorrent для обмена файлами в пиринговых сетях написана на языке Python;
#
# NASA, Los Alamos, JPL и Fermilab используют Python для научных вычислений.

# Философия Python
# Разработчики языка Python придерживаются определённой философии программирования, называемой «The Zen of Python». Её текст выдаётся интерпретатором Python по команде import this (работает один раз за сессию). Автором этой философии считается Тим Петерс (Tim Peters).
#
# В оригинале
# Beautiful is better than ugly;
# Explicit is better than implicit;
# Simple is better than complex;
# Complex is better than complicated;
# Flat is better than nested;
# Sparse is better than dense;
# Readability counts;
# Special cases aren't special enough to break the rules;
# Although practicality beats purity;
# Errors should never pass silently;
# Unless explicitly silenced;
# In the face of ambiguity, refuse the temptation to guess;
# There should be one — and preferably only one — obvious way to do it;
# Although that way may not be obvious at first unless you're Dutch;
# Now is better than never;
# Although never is often better than *right* now;
# If the implementation is hard to explain, it's a bad idea;
# If the implementation is easy to explain, it may be a good idea;
# Namespaces are one honking great idea — let's do more of those!
# Перевод на русский язык
# Красивое лучше, чем уродливое;
# Явное лучше, чем неявное;
# Простое лучше, чем сложное;
# Сложное лучше, чем запутанное;
# Плоское лучше, чем вложенное;
# Разреженное лучше, чем плотное;
# Читаемость имеет значение;
# Особые случаи не настолько особые, чтобы нарушать правила;
# При этом практичность важнее безупречности;
# Ошибки никогда не должны замалчиваться;
# Если не замалчиваются явно;
# Встретив двусмысленность, отбрось искушение угадать;
# Должен существовать один — и, желательно, только один — очевидный способ сделать это;
# Хотя он поначалу может быть и не очевиден, если вы не голландец;
# Сейчас лучше, чем никогда;
# Хотя никогда зачастую лучше, чем прямо сейчас;
# Если реализацию сложно объяснить — идея плоха;
# Если реализацию легко объяснить — идея, возможно, хороша;
# Пространства имён — отличная вещь! Давайте будем делать их больше!

# Python является интерпретируемым языком

# Преимуществами языка Python являются
# платформонезависимость
#
# встраиваемость
#
# простота
#
# наличие большой библиотеки классов
#
# динамическая типизация (для несложных программ)

# Недостатками языка Python являются
# низкая скорость выполнения программ
# динамическая типизация (для сложных программ)

# Какие задачи можно удобно/эффективно решать, используя язык Python?
# создание приложений баз данных
# создание системных утилит
# создание графических приложений GUI
# создание приложений анализа данных
# создание веб-приложений

