# Если операция плюс - сложить.
# Иначе если минус - вычесть.
# Иначе если умножение - умножить.
# Иначе если деление - проверить делитель.
# Если делитель не ноль - делить.
# Иначе сообщить об ошибке.
# Если операция вообще неизвестна - вывести error.


num_1 = int(input('enter 1st number: '))
num_2 = int(input('enter 2nd number: '))
operation = input('enter expression (+, -, /, *,): ')
if operation == '+':
    print(num_1 + num_2)
elif operation == '-':
    print(num_1 - num_2)
elif operation == '*':
    print(num_1 * num_2)
elif operation == '/':
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print('деление на ноль')
else:
    print('error')