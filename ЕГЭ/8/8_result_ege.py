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
