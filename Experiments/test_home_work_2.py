print("Тест на жадность")
tovari_sum = input("Введите стомость товара: ")
skidka = input("Какую скидку хотите: от 10 до 100% ?: ")
tovari_sum = int(tovari_sum)
skidka = int(skidka)
if skidka <= 40:
    print("Good boy!➡️", tovari_sum - skidka, "монеток к оплате")
if skidka >= 40:
    print("Zhadina!➡️", tovari_sum - skidka,"монеток к оплате")



