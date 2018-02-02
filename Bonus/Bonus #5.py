word = input('Введите слово: ')
result = ''
cons = 'qwrtplkjhgfdszxcvbnm'
for i in word:
    if i in cons:
        i = i.replace(i, i + 'aig')
    result += i

print(result)
#также надеюсь, что простота кода ни на что не повлияет.