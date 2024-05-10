#задание № 8 
from itertools import *
'''
res = set()

for i in list(permutations("АВРОРА")):

    if all(True if i[j] != i[j+1] else False for j in range(len(i)-1)):
        res.add(i)

print(len(res))

#Задание № 8 (10710)

result = list()
words = sorted(product('компьютер',repeat= 5))

for i,j in enumerate(words,1):

    if i % 2 != 0 and j[0]!='ь' and j.count('к')==2:
        result.append(i)

print(max(result))

# вариант от яндекса(4)
result = []

for i in product('0123456',repeat = 6):

    if i[0]!='0' and i.count('0') == 1 and sum([i.count(j) for j in '246']) % 2 == 0:
        result.append(i)

print(len(result))

# вариант от яндекса(5)

res = []

for i in product('0123456789abcdef',repeat = 5):

    if sum([i.count(j) for j in '0123456789'])==1 and i[0]!='0':
        res.append(i)

print(len(res))

'''
# вариант 7 от яндекса
res = set()
comb = [''.join(i) for i in product('ВОЗДУХ',repeat=5) ]
chek = [(0,1),(1,0)]
chek_2 = ['ОВ','ВО','ХО','ОХ','УВ','ВУ','УХ','ХУ']
for word in comb:
    if ((word.count('О'),word.count('У')) in chek and not(any(i for i in chek_2 if i in word))):
        res.add(word)

print(len(res))