
text = open('AI.txt', 'r')

dictionary = []

for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(' ')

    for word in words:
        if word in dictionary:
            dictionary[word]+= int(1)
        else:
            dictionary[word]= int(1)


for key in dictionary:
    print(key, ': ', dictionary[key])

print(dictionary)

text.close()