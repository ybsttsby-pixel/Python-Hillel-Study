import string
text = input()
for char in string.punctuation:
    text = text.replace(char, "")
words = text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)
hashtag = hashtag[:140]
print(hashtag)