import random

def article_1():
    with open('articles_1.txt','r', encoding='utf-8') as f:
        text = f.read()
        lines1_art = text.splitlines()
    return random.choice(lines1_art)

def noun_2():
    with open('noun2_masc.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_masc = text.splitlines()
    with open('noun2_fem.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_fem = text.splitlines()
    with open('noun2_plural.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_plural = text.splitlines()
    article_1()
    if article_1() == 'le':
        return random.choice(lines_masc)
    elif article_1() == 'la':
        return random.choice(lines_fem)
    else:
        return random.choice(lines_plural)

def noun_3():
    with open('noun3_masc.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_masc = text.splitlines()
    with open('noun3_fem.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_fem = text.splitlines()
    with open('noun3_plural.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_plural = text.splitlines()
    article_1()
    if article_1() == 'le':
        return random.choice(lines_masc)
    elif article_1() == 'la':
        return random.choice(lines_fem)
    else:
        return random.choice(lines_plural)


def verb_2():
    with open('verb_2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines2_verb = text.splitlines()
        return random.choice(lines2_verb)

def preposition_1():
    with open('preposition_1.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines1_prep = text.splitlines()
        return random.choice(lines1_prep)

def preposition_2():
    with open('preposition_2.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines2_prep = text.splitlines()
        return random.choice(lines2_prep)

def conjunction_1():
    with open('conjunction_1.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines_conj = text.splitlines()
        return random.choice(lines_conj)

def verse1():
    return article_1() + ' ' + noun_2() + ' ' + verb_2()

def verse2():
    return preposition_1() + ' ' + article_1() + ' ' + noun_2() + ' ' + conjunction_1() + ' ' + verb_2()

def verse3():
    return preposition_2() + ' ' + noun_3() 

def make_haiku():
    print(verse1() + '\n' + verse2() + '\n' + verse3())

make_haiku()