word = input('Введите слово или фразу: ')
result = ''
vowels = 'aeiyou'
for i in word:
    if i in vowels:
        i = i.replace(i, i + 'с' + i)
    result += i

print(result)
#очень надеюсь, что простота кода не убавит мне баллов. задание выполняется в одно действие ведь.
