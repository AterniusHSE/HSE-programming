from os import spisokdir
import re

files_spisok = spisokdir()
counter = 0
for file in files_spisok:
    if re.match('^[A-Za-z]*\.[A-Za-z]*$', file): #считаем, что у файла всегда указан формат через точку
        counter += 1
        
print(counter, 'файлов и папок.')

print('\nСписок всех файлов и папок без повторов:')
files_spisok = set(files_spisok)
for file in files_spisok:
    print(file)

#простите, что опять не в функциях, но они как-то снова у меня не получаются :с