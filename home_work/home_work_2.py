# квадрат числа
# 1й вариант
slon = input("Введите число: ")
print(int(slon) * int(slon))

# 2й вариант
puk = int(slon)
print(puk * puk)

# 3й вариант
print(int(slon) ** 2)


# среднее значение трех чисел
# 1й вариант
cifra_1 = input("введите первое любое число: ")
cifra_2 = input("введите второе любое число: ")
cifra_3 = input("введите третье любое число: ")
avrg_val = int(cifra_1) + int(cifra_2) + int(cifra_3)
print(avrg_val / 3)


# 2й вариант
chislo_1 = 6
chislo_2 = 9
chislo_3 = 11
print(float((chislo_1 + chislo_2 + chislo_3) / 3))


# 3й вариант
numero_1 = 40
numero_2 = 33
numero_3 = 2
print(int((numero_1 + numero_2 + numero_3) / 3))

# 4й вариант
import statistics
avrg_val = [2, 4, 6]
print(statistics.mean(avrg_val))


# 5й вариант
cifra_1 = int(input("введите первое любое число: "))
cifra_2 = int(input("введите второе любое число: "))
cifra_3 = int(input("введите третье любое число: "))
print(cifra_1 + cifra_2 + cifra_3)


# превращение минут в часы
# 1й варианр
minuts = int(input("Назови число от 100 до 1000: "))
hours, minuts = divmod(minuts, 60)
print(hours,"часа", minuts, 'минут')


# 2й вариан
minuts = int(input("Назови число от 100 до 1000: "))
hours = minuts // 60
minuts = minuts % 60
print(hours, 'часов', minuts, 'минут')


# расчет скидки
# 1й вариант
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

# 2й вариант
print("Тест на жадность")
tovari_sum = input("Введите стомость товара: ")
skidka = input("Какую скидку хотите: от 10 до 100% ?: ")
tovari_sum = int(tovari_sum)
skidka = int(skidka)
    if skidka <= 49:
        print("Good boy!➡️", tovari_sum - (tovari_sum * skidka / 100), "монеток к оплате")
    if skidka >= 51:
        print("Zhadina!➡️", tovari_sum - (tovari_sum * skidka / 100), "монеток к оплате")
    if skidka == 50:
        print("OK!➡️", tovari_sum - (tovari_sum * skidka / 100), "монеток к оплате")


# последняя цифра числа
# возможно я тут что то не понял но кажется этого достаточно
height = int(input("Какой у вас рост?: "))
item_1 = height % 10
print("Длинна члена", item_1)


# периметр треугольника
print("Доставайте ваш прямоугольничек")
print("Измерили его длину?")
dlina = input("Введите длину прямоугольника: ")
print("Измерили его ширину?")
shirina = input("Введите ширину прямоугольника: ")
perimetr = 2 * (int(dlina) + int(shirina))
otvet = input("Хотите узнать результат? Y или N ?: ")
if otvet == "Y":
    print(perimetr)
else:
    print("Ну, ладно...")


# вывод числа в столбик











