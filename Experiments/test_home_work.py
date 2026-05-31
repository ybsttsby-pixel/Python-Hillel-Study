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