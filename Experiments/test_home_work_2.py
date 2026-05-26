print("🚨 All Sale- up to 50% 🚨")
tovari = input("Укажите стомость первого товара: ")
tovari_2 = input("Укажите стомость второго товара: ")
tovari_3 = input("Укажите стомость третьего товара: ")
tovari_total = int(tovari) + int(tovari_2) + int(tovari_3)
print("Ответьте на доп вопрос и получити доп скидку 40%")
voprosik = input("Сколько дней в году?: ")
if voprosik == "365":
    print("Win Win Win",
          (300 - (tovari_total / 100) * 90), "к оплате")
else:
    print("u lose",
          (300 - (tovari_total / 100) * 50), "к оплате")

