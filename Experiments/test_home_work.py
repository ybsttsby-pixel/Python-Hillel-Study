
lst = [12, 3, 7, 123]
last = lst.pop()
lst.insert(0, last)
print(lst)


lst = [12, 3, 7, 123]
if len(lst) > 1:
    last = lst.pop()
    lst.insert(0, last)
print(lst)