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


# так ведь тоже можно?
num_input_1 = int(input('enter first number: '))
num_input_2 = int(input('enter second number: '))
operator = input('enter operator: ')
if num_input_1 == 0 and num_input_2 ==0 and operator == '/':
    print('ноль на ноль не делится')
elif operator == '/':
    print(num_input_1 / num_input_2)
elif operator == '+':
    print(num_input_1 + num_input_2)
elif operator == '-':
    print(num_input_1 - num_input_2)
elif operator == ('*'):
    print(num_input_1 * num_input_2)