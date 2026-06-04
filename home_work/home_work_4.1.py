lst = [0, 1, 0, 12, 3]
zeros = []
prime = []
for num in lst:
    if num == 0:
        zeros.append(num)
for num in lst:
    if num != 0:
            prime.append(num)
print(prime + zeros)