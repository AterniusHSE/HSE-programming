f = open("C:/Users/Aternius/Desktop/text.txt", "w", encoding="utf-8")
a = input ("Введите латинское слово: ")
word = a
while word != "":
    if word.endswith("re") or word.endswith("ri"):
            f.write(word+"\n")
    word = input ("Введите латинское слово: ")
f.close()
            
