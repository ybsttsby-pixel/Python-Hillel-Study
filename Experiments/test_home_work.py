lst = [0, 1, 7, 2, 4, 8]
even_sum = 0
for i in range(len(lst)):
    if i % 2 == 0:
        even_sum += lst[i]
result = even_sum * lst[-1]
print(result)