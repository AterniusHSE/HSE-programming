import random

word = input('Введите латинское слово: ')
result = ''
cons = 'qwrtpsdfghkljzxcvbnm'
vowels = 'aeyuoi'
#беру лишь буквы латиницы, ведь нужно латинское слово

if word[0] in cons:
    end = word[0].replace(word[0], word[0] + 'ay')
    form = word[1:]
    begin = form + end

if word[0] and word[1] in cons:
    part_end = word[1].replace(word[1], word[1] + 'ay')
    end = word[0] + part_end
    form = word[2:]
    begin = form + end

if word [0] in vowels:
        begin_1 = word + 'ay'
        begin_2 = word + 'way'
        begin_list = (begin_1, begin_2)
        begin = random.choice(begin_list)
#Алена сказала не париться по поводу альтернативного способа образования слов с гласной в начале.
#то бишь, не учитывать способ "гласная + согласная/сочетание согласных".

result = begin
print(result)