# import this
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
user_name = "Stah"
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

