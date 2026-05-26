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
