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
print((int(vopros) / 60))


vorpos_2 = input("Сколько в году дней?: ")
result = (((int(vorpos_2) * 24) * 60))
print(result, "минут в году")
