# Задание № 5900
from re import *

def number(string):
    res = 0
    for i in 'аеоуыяэёюиАУОЕЁИЭЯЫЮ':
        res += string.count(i)
    return res

with open('10.txt', 'r') as f:
    counter = 0
    file = findall(r'[а-яА-ЯёЁ]+', ''.join([i for i in f]))
    for word in file:
        if len(word) != 1:
            counter += number(word)
    print(counter)
