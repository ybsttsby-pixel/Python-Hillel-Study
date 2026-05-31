#1.
num_1 = int(input("enter 1st number: ")
num_2 = int(input("enter 2nd number: ")
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)

#2.
item = int(input("введите число: ")
print(item ** 2)
print(item * item * item)

#3.
dlina = int(input("введите длину прямоугольника: ")
shirina = int(input("введите ширину прямоугольника: ")
ploschad = dlina * shirina
perimetr = 2 * (dlina + shirina)
print(ploschad)
print(perimetr)

#4.
age = int(input("Сколько тебе лет?: "))
result = age + 10
print("Через 10 лет тебе будет", result, "лет")

#5.
num_1 = int(input("enter 1st number: "))
num_2 = int(input("enter 2nd number: "))
print(num_1 / num_2)
print(num_1 // num_2)
print(num_1 % num_2)

#6.
secunds = int(input("Введите сколько то секунд: "))
print(secunds)
minuts = (secunds // 60)
print(minuts)
rest_sec = secunds % 60
print(rest_sec)
print(minuts, "минут", rest_sec, "секунд")


#7. я не пойму как получить десятки и еденицы
num = int(input("Enter a number: "))
sotni = num // 100
print(sotni)
desyatki = num % 100
print(desyatki)


#8.
price = int(input("Price: "))
discount = int(input("Discount: "))
total_price =(price - (price / 100) * discount)
print(total_price)


#9.
num = int(input("введите число: "))
answer = num % 2
if answer == 0:
    print("четное")
else:
    print("нечетное")


#10.
cash = int(input("введите сумму доходов: "))
sotni = cash // 100
ostatoc = cash % 100
print("всего сотен", sotni, "и остаток", ostatoc)


#11.
cels = int(input("температура в цельсий: "))
farn = ((cels * 9) / 5) + 32
print(farn)


#12.
speed = int(input("введите скорость: "))
time = int(input("введите время: "))
dist = speed * time
print(dist)


#13.
value = int(input("введите количество минут: "))
hours = value // 60
minutes = value % 60
print(hours, "часов", minutes, "минут")


#14.
S = input("введите 4ех число: ")
len(S)
num_1 = S[0]
num_2 = S[1]
num_3 = S[2]
num_4 = S[3]
otvet = int(num_1) + int(num_2) + int(num_3) + int(num_4)
print(otvet)


#15.
dni = int(input("введите кол-во дней: "))
week = dni // 7
rest_days = dni % 7
print(week, "недели", rest_days, "и оставшихся дней")