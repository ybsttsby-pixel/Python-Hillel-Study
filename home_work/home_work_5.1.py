import keyword
import string
name = input()
result = True
if name[0].isdigit():
    result = False
elif any(ch.isupper() for ch in name):
    result = False
elif " " in name:
    result = False
elif "__" in name:
    result = False
elif keyword.iskeyword(name):
    result = False
else:
    punctuation = string.punctuation.replace("_", "")
    if any(ch in punctuation for ch in name):
        result = False
print(result)