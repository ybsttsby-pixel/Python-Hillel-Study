# квадрат числа
# 1й вариант
import math
slon = input("Введите число: ")
print(int(slon) * int(slon))

# 2й вариант
puk = int(slon)
print(puk * puk)

# 3й вариант
print(int(slon) ** 2)


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


# расчет скидки
print("🚨 All Sale- up to 50% 🚨")
tovari = input("Укажите стомость первого товара: ")
print("👍")
tovari_2 = input("Укажите стомость второго товара: ")
print("👍")
tovari_3 = input("Укажите стомость третьего товара: ")
print("👍")
tovari_total = int(tovari) + int(tovari_2) + int(tovari_3)
print("Ответьте на доп вопрос и получити доп скидку 40%")
voprosik = input("Сколько дней в году?: ")
if voprosik == "365":
    print("🌟 Win Win Win 🌟",
          (300 - (tovari_total / 100) * 90), "к оплате")
else:
    print("😈 u lose 😈",
          (300 - (tovari_total / 100) * 50), "к оплате")

    print("Тест на жадность")
    tovari_sum = input("Введите стомость товара: ")
    skidka = input("Какую скидку хотите: от 10 до 100% ?: ")
    tovari_sum = int(tovari_sum)
    skidka = int(skidka)
    if skidka <= 40:
        print("Good boy!➡️", tovari_sum - skidka, "монеток к оплате")
    if skidka >= 40:
        print("Zhadina!➡️", tovari_sum - skidka, "монеток к оплате")


# последняя цифра числа
# возможно я тут что то не понял но кажется этого достаточно
age = input("Какой у вас рост?: ")
puk = int(age) % 10
print("Длинна члена", puk)


# периметр треугольника
print("Доставайте ваш прямоугольничек")
print("Измерили его длину?")
dlina = input("Введите длину прямоугольника: ")
print("Измерили его ширину?")
shirina = input("Введите ширину прямоугольника: ")
perimetr_1 = 2 * (int(dlina) + int(shirina))
otvet = input("Хотите узнать результат? Да или Нет?: ")
if otvet == "Да":
    print(perimetr_1)
else:
    print("(((")







