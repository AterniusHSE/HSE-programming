import re

def open_text():
    with open('txt.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        text2 = text.lower()
    return text2

def open_forms():
    with open('forms.txt', 'r', encoding='utf-8') as file:
        forms = file.read()
        forms_list = forms.split('\n')
    forms_list_ex = []
    for word in forms_list:
        word2 = '\W(' + word + 'с?[ья]?)\W'
        forms_list_ex.append(word2)
    return forms_list_ex

def searching(txt, forms):
    results = []
    for form in forms:
        res = re.findall(form, txt)
        results.extend(res)
    result = []
    for form in results:
        if form not in result:
            result.append(form)
    print('\n'.join(result))

def main():
    txt = open_text()
    frms = open_forms()
    searching(txt, frms)

if __name__ == '__main__':
    main()