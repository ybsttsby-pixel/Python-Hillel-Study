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
tovari_sum = input("Введите стомость товара")
