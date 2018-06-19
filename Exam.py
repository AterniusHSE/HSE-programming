import re
import os
import csv
    
    
def open_files():
    path = 'C:\\Users\\Ли\\Desktop\\news\\news'
    for file_names in os.listdir(path):
        with open (os.path.join(path, file_names), 'r', encoding='windows-1251') as files:
            text = files.read()
            splitted = text.split('\n')
            return text, splitted
        #читаю все файлы в папке, спличу полученное

def find_info(splitted):
    doc_id = {}
    title = {}
    author = {}
    created = {}
    topic = {}
    tagging = {}
#создаю словари, которые будут содержать слова, идущие в одной строке с нужными тегами
    for line in splitted:
        tagging_search = re.search('<meta content="([a-z]*)"\sname="(tagging)"', line)
        if tagging_search:
            result = search.group(1)
            if result in tagging:
                tagging[result] += 1
            else:
                tagging[result] = 1
#добавляю слова в словарь
    for line in splitted: 
        doc_id_search = re.search('content="([a-z]*)".*(doc_id)', line) 
        if doc_id_search: 
            result = search.group(1) 
            if result in doc_id: 
                doc_id[result] += 1 
            else: 
                doc_id[result] = 1 
    for line in splitted: 
        title_search = re.search('content="([a-z]*)".*(title)', line) 
        if title_search: 
            result = search.group(1) 
            if result in title: 
                title[result] += 1 
            else: 
                title[result] = 1 
    for line in splitted: 
        author_search = re.search('content="([a-z]*)".*(author)', line) 
        if author_search: 
            result = search.group(1) 
            if result in author:
                author[result] += 1 
            else: 
                author[result] = 1 
    for line in splitted: 
        created_search = re.search('content="([a-z]*)".*(created)', line) 
        if created_search: 
            result = search.group(1) 
            if result in created: 
                created[result] += 1 
            else: 
                created[result] = 1 
    for line in splitted: 
        topic_search = re.search('content="([a-z]*)".*(topic)', line) 
        if topic_search: 
            result = search.group(1) 
            if result in topic: 
                topic[result] += 1 
            else: 
                topic[result] = 1
    return topic, doc_id, author, title, tagging, created
#получаю словари на выходе

def create_csv():
    with open('new.csv', 'a') as CSV:
        writer = csv.writer(CSV)
        writer.writerow(doc_id)
        writer.writerow(title)
        writer.writerow(author)
        writer.writerow(created)
        writer.writerow(topic)
        writer.writerow(tagging)
#создаю строки в csv файле


def append_csv(doc_id, author, created, title, topic, tagging):
    with open ('new.csv', 'w') as writeFile:
        

def main():
    splitted, info = open_files()
    tagging = find_info(splitted)
    csv(doc_id, author, created, title, topic, tagging)

if __name__ == '__main__':
    main()



