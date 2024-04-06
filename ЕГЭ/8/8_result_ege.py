#задание № 8 
from itertools import *

x = set([''.join(i) for i in list(permutations("АВРОРА"))])
z = [i for i in x if not(i[0]==i[1] or i[1]==i[2] or  i[2]==i[3] or  i[3]==i[4] or  i[4]==i[5]) ]
print(len(z))

#Задание № 8 (10710)

result = list()
words = sorted(product('компьютер',repeat= 5))
for i,j in enumerate(words,1):
    if i % 2 != 0 and j[0]!='ь' and j.count('к')==2:
        result.append(i)
print(max(result))

# вариант от яндекса(4)

info = [''.join(i) for i in product('0123456',repeat = 6) if i[0]!='0' and i.count('0') == 1]

result = [i for i in info if sum([i.count(j)for j in '246'])%2==0]
print(len(result))

# вариант от яндекса(5)

info = [''.join(i) for i in product('0123456789abcdef',repeat = 5) if i[0]!='0']

result = [i for i in info if sum([i.count(j) for j in '0123456789'])==1]
print(len(result))


