def open_file():
    select_file = input('Введите название файла, пожалуйста: ')
    with open(select_file, 'r', encoding='utf-8') as f:
        text = f.read()
        stripped = text.strip(':;,.-?!')
        # я надеюсь, что я все знаки препинания ввел. не видел смысла вводить '...' (есть ли он?)
        # и кавычки со скобками
        splited = stripped.split()
    return splited

def search_ed(words):
    count_ed = 0
    for word in words:
        if word.endswith('ed'):
            count_ed += 1
    return count_ed

def search_ied(words):
    count_ied = 0
    for word in words:
        if word.endswith('ied'):
            count_ied += 1
    return count_ied

def result():
    words = open_file()
    print('Количество слов, оканчивающихся на -ed: ', search_ed(words))
    print('Количество слов, произошедших от глагола на -y и -e, заканчивающихся на -ed: ', search_ied(words))

result()