file = open("sample.txt", "r")
text = file.read()
file.close()

words = text.split()
count = {}

for word in words:
    word = word.lower()
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in sorted(count):
    print(word, ":", count[word])
