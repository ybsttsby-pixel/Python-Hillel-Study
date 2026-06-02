# 1 вариант
lst = [1, 2, 3, 4, 5]
mid = (len(lst) + 1) // 2
result = [lst[:mid], lst[mid:]]
print(result)