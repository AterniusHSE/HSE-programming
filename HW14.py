import re

def read_file():
    with open ('file.txt', 'r', encoding='utf-8') as f:
        get_text = f.read()
        return get_text

def split_and_punct(get_text):
    sentences = re.split(r'[.?!]\s*', get_text)
    no_punct = re.sub(r'[.,:;()[]]','',sentences) #очень надеюсь, что этой пунктуации хватает
    return no_punct

def dictionary(get_text):
    sentences = re.split(r'[.?!]\s*', get_text)
    key_dict = {i: len(i) for i in sentences}
    main_dict = {sentences: key_dict}
    return main_dict

