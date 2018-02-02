number = input('Введите число:')
count = 0
sum = 0
amount = list()
while number != '':
    count += 1
    to_amount = float(number)
    add = amount.append(to_amount)
    sum += to_amount
    number = input('Введите число:')

max = max(amount)
min = min(amount)
#не помню, были ли у нас функции min и max, но я нашел их в гугле,
#они довольно простые и self-explanatory. надеюсь нормально.
average = sum / count
print('Среднее арифметическое значение: ', average)
print('Наибольшее из введенных чисел: ', max)
print('Наименьшее из введенных чисел: ', min)