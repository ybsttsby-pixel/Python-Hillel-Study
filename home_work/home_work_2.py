# квадрат числа
import math
slon = input("Введите число: ")
print(math.sqrt(int(slon)))


print(math.sqrt(9))


print(3 * 3) # корень с 9


# среднее значение трех чисел
cifra_1 = input("введите первое любое число: ")
cifra_2 = input("введите второе любое число: ")
cifra_3 = input("введите третье любое число: ")
avrg_val = int(cifra_1) + int(cifra_2) + int(cifra_3)
print(avrg_val / 3)


chislo_1 = 6
chislo_2 = 9
chislo_3 = 11
print(float((chislo_1 + chislo_2 + chislo_3) / 3))


numero_1 = 40
numero_2 = 33
numero_3 = 2
print(int((numero_1 + numero_2 + numero_3) / 3))


import statistics
avrg_val = [2, 4, 6]
print(statistics.mean(avrg_val))


# превращение минут в часы
vopros = input("Назови число от 100 до 1000: ")
znach = ((int(vopros) / 60))
print((znach), "в минутах")


print("Давай узнаем сколько минут в году?")
vopros_2 = input("Сколько в году дней?: ")
vopros_3 = input("сколько минут в часах?: ")
vopros_4 = input("Сколько в сутках часов?: ")
otvet = int(vopros_2) * int(vopros_3) * int(vopros_4)
print((otvet), "минут в году")


# 
