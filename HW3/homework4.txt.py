a = open("text.txt", encoding="utf-8")
text = a.read()
a.close()
text = text.split(" ")
n1 = 0
n2 = 0
for word in text:
    b = len(word)-1
    if word[b] == ".":
        n1 += 1
    if word[b] == ",":
        n1 += 1
    else:
        n2 += 1
fin = n2/(n2+n1)*100
print ("Процент слов, оканчивающихся на точку или запятую, от всех слов: ", fin, "%")
