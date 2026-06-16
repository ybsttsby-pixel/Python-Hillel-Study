import string
letters = string.ascii_letters
start, end = input().split('-')
i = letters.index(start)
j = letters.index(end)
print(letters[i:j + 1])