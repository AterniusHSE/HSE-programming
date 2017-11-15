x = input("Введите слово: ")
for b in x:
    x = x[-1] + x[:-1]
    print(x)
if x == "":
    print("Введите слово, пожалуйста!")
    x = input("Введите слово: ")
    for b in x:
        x = x[-1] + x[:-1]
        print(x)
