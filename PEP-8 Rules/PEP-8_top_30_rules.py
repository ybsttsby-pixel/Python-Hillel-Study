пук пук
# "Простой хуже сложного"
# это из Zen of Python
import this
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


# Имена и Переменные

# Имена переменных через snake_case
# ВЕРНО
user_name = "Stas"
total_price = 100

# НЕ ВЕРНО
userName
TotalPrice


# Константы CAPS_LOCK
# CORRECT
MAX_USERS = 100
PI = 3.1415926

# WRONG
max_users = 100
pi = 3.1415926


# Классы через CAMEL_CASE
class UserProfile:
    pass


# Имена должны быть понятнымт
# CORRECT
user_age = 15
user_name = "bob"

# WRONG
x = 15
a = "Bob"


# Не используй I O l (и, о, эл) как переменные
# потому что l похожа на 1
# буква 0 похожа на цирфру 0


# Пробелы spaces
# Один пробел вокруг операторов
# CORRECT
x = 5 + 3

# WRONG
x=5+3


# После запятой ставь пробел
# CORRECT
print(a, b, c)


# Не ставь пробелы внутри скобок
# CORRECT
print(x)

# WRONG
print( x )


# Длина строк
# в строке не должно быть больше 79-88 символов
# Если строка огромная то разешен перенос
message = (
    "Очень длинный текст"
    "который лучше перенести"
)


# ФУНКЦИИ
# между функциями оставляй 2 пустые строки
def hello():
    pass


def bye():
    pass


# НАЗВАНИЯ ФУНКЦИЙ = ГЛАГОЛЫ
# CORRECT
get_user(user_name)
calculate_total(total_price)
send_email()


# Функция должна делать одну вещь
# Если функция:
# - считает
# - отправляет имейл
# - вызывает сатану
# ЭТО УЖЕ ЧЕТЫРЕ ФУНКЦИИ


# Не делай функции по 200 строк
# Новочики любят писать "mega_final_functions_v2"
# НЕ НАДО


# ИМПОРТЫ
# Импортировать всегда сверху файла
# CORRECT
import os
import json


# Один импорт = одна строка
# CORRECT
import os
import json

# WRONG
import os, json


# Сначала стандартные библиотеки, потом внешние
import os
import json

import request


# УСЛОВИЯ
# Не сравнивай bool через ==True
# CORRECT
if is_admin:

# WRONG
if is_admin == True


# Проверка на None через is
# CORRECT
if value is None

# WRONG
if value == None


# СПИСКИ И СТРОКИ
# Используйте join вместо конкатенации в цикле
# CORRECT
result = "".join(words)

# WRONG
results = ""

for word in words:
    result += word


# List comprehension только если читаемо
# CORRECT
numbers = [x * 2 for x im range(10)]

# WRONG
numbers = [x * 2 if x > esle x + 100 for x in ragne(1000)  if x != 5]


# КОММЕНТАРИИ
# Комментарии обьясняют ПОЧЕМУ, а не то ЧТО
#
# WRONG
# увеличиваем х на 1
x = += 1


# # Пиши docstring для функций
# docstring ≠ обычный комментарий.
# Это скорее официальное описание функции, класса или модуля.
# В чём разница?
# Комментарий:
# * просто заметка
# * Python его игнорирует
#
# Docstring:
# * является частью объекта
# * Python умеет его читать
# * IDE показывает его как подсказку
# * используется в документации

def add(a,b):
    """складывает два числа"""
    return a + b


# ОТСТУПЫ
# 4 пробела, не ТАБы
#
# Пайтон буквально постороен на отступах


# Одинаковые отступы везде
# WRONG
if True
    print("a")
       print("b")


# СТРУКТУРА
# Не пиши все в одном файле
# Когда файл:
# - 3000 строк
# - 18 классов
# - 42 фукнции
# это уже не код, а археологичесий памятник


# Группируй связанный код
# Не раскидывай функции хаотично


# ОБРАБОТКА ОШИБОК
# Не используй голый except
# CORRCET
except ValueError

# WRONG
except:


# Не скривай ошибки молча
# WRONG
except:
   pass
# Ты буквально закапываешь пробоему под ковёр


СТИЛЬ
Код должен читаться как текст
Хороший Пайтон:
- простой
- очевидный
- читаемый
