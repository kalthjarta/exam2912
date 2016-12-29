#Наталья Энгель, БКЛ-153
import re
import os
import urllib.request  
req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')

file = open('C:/Users/natal/Desktop/raw.txt', 'w', encoding = 'utf-8') #записываем слова в файл для майстема
result = re.findall(u' [сС]\w+', html)
for x in result:
    print(x)
    file.write(x + '\n')
    
file.close()


os.system(r"C:/Users/natal/Desktop/mystem.exe " + '-ni -e utf8 ' + r"C:/Users/natal/Desktop/raw.txt" + r" C:/Users/natal/Desktop/words.txt")
f4 = open('C:/Users/natal/Desktop/words.txt', 'r', encoding = 'utf-8') 
reg = f4.read()
f4.close()

f5 = open('C:/Users/natal/Desktop/verbs.txt', 'w', encoding = 'utf-8') #ищем и записываем глаголы
mas = reg.split('\n')
d = {}
for elem in mas:
    if '?' not in elem:
        resv = re.search('^(\w.+)\{.+?=V.+?', elem)
        if resv != None:
            bi = resv.group(1)
            if bi in d:
                continue
            else:
                d[bi] = 1

for word in d:
    f5.write(word + '\n')
    print(word + '\n') #выводим глаголы на экран

f5.close()

os.system(r"C:/Users/natal/Desktop/mystem.exe " + '-ni -e utf8 ' + r"C:/Users/natal/Desktop/raw.txt" + r" C:/Users/natal/Desktop/wlpovs.txt")
f6 = open('wlpovs.txt', 'r', encoding = 'utf-8') #промежуточный файлик
lines = f6.read()
f6.close()
myst = re.findall('(.+?)\{(.+?)(\|.+?)?(\|.+?)?\}\\n', lines, flags = re.DOTALL)
f7 = open('sqltable.txt', 'a', encoding = 'utf-8') #инсерты

#дальше с таблицами не успелось и не срослось

f7.close()

        


