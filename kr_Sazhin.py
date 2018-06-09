import re

def read_file(cut_version):
    with open('C:\Users\Ли\Desktop\test.txt', 'r', encoding='utf-8') as f:
        read = f.read()
        cut_body = read.split('<body>')[1]
        final_cut = cut_body.split('</body>')[0]
        final_string = ''.join(final_cut)
        return final_string
#открываю файл, читаю, спличу с двух сторон боди-парт и перевожу все оставшееся в строку
#почему-то у меня выдает ошибку при открытии файла, и я не могу понять, почему :с
#он ругается на скобочку
    
def count(total):
    total_symbols = 0
    start_symbols = 0
    compiled = re.compile(cut_version)
    while True:
        matches = compiled.search('.', 'final_string')
        if matches is None: return total
        total_symbols += 1
        start_symbols = 1 + matches.start()
    return total_symbols
#беру полученное из первой функции, устанавливаю счетчики, компайлю содержимое для
#удобного поиска, проверяю наличие символов и веду счет

def new_file():
    with open ('new file', 'w', encoding='utf-8') as new:
        counted = new.write(total_symbols)
        return counted
#возвращаю подсчитанное в виде цифры в новый созданный файл


        
        
        
