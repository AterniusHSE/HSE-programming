import random


def get_words():
    my_dict = {}
    with open('Words.csv','r', encoding='utf-8') as f:
        for lines in f:
            lines_stripped = lines.strip('\ufeff \n')
            lines_new = lines_stripped.split(',')
            word, hint = lines_new
            my_dict[word] = hint
            word = list(my_dict.keys())
            choice = random.choice(word)

        print(my_dict[choice])
    user_answer = input('Введите отгадку: ')
    if user_answer == choice:
        print('Молодец, правильно!')
    else:
        print('Прости, ты не угадал :с')

get_words()

#не смог перевести в функции - банально не получается (ни с подсказками, ни с конспектом) обратиться к переменной в другой функции
#не успел сделать задание с "количеством точек сколько слов в подсказке"
#я слишком долго сидел над этой штукой, и словари мне не даются вообще. Не вижу, как переносить что-то в словарь из файла, как
#связать слово, выбранное рандомом, с таким же словом в словаре, чтобы выдал мне подсказку.
#я не знаю, что делать :с