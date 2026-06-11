import random
list1 = []
for i in range(random.randint(3, 10)):
    list1.append(random.randint(1, 100))
list2 = [list1[0], list1[2], list1[-2]]
print(list1, "==", list2)