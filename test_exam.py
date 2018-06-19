import re

def open_file():
    with open ('Karenina.xml', 'r', encoding='utf-8') as file:
        text = file.read()
        splitted = text.split('\n')
    return splitted, text

def counter(text):
    counter_ana = re.findall('<ana', text)
    counter_w = re.findall('<w>', text)
    relation = len(counter_ana)/len(counter_w)
    print('Шо то хуйня, шо это хуйня, но вот вам отношение: ', relation)

def parts_of_speech(splitted):
    freq = {}
    for line in splitted:
        search = re.search('gr="([A-Z]*)', line)
        if search:
            result = search.group(1)
            if result in freq:
                freq[result] += 1
            else:
                freq[result] = 1
    return freq

def new(freq):
    with open ('Res.txt', 'w', encoding='utf-8') as new:
        for line in sorted(freq, key=freq.get, reverse=True):
            new.write(line + '\t' + str(freq[line]) + '\n')

def last(splitted):
    words = []
    for num, line in enumerate(splitted):
        if re.search('gr="S,[^"]+твор', line):
            search = re.search(r'>([А-Яа-яЁё]+)<', line)
            word = [num, search.group(1)]
            words.append(word)
    return words

def new_last(words):
    with open ('new_last.txt', 'w', encoding='utf-8') as new_last:
        
    


def main():
    splitted, text = open_file()
    counter(text)
    freq = parts_of_speech(splitted)
    new(freq)
    words = last(splitted)

if __name__ == '__main__':
    main()
    
    
        
