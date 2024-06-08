
from itertools import *
'''
#задание № 8 

x = set([''.join(i) for i in list(permutations("АВРОРА"))])
z = [i for i in x if not(i[0]==i[1] or i[1]==i[2] or  i[2]==i[3] or  i[3]==i[4] or  i[4]==i[5]) ]
print(len(z))

#10717(№15)

def geometry(k,m,n):
    arr = [k,m,n]
    if max((arr))<sum(sorted(arr,reverse=True)[1:]):
        return True
    return False

def moment(a):
    for k in range(1,10000):
        stop = not((geometry(k, 11, 18) == (not(max(k, 5) > 68))) and geometry(k, a, 5))
        if stop!=1:
            return 0
    return 1

for a in range(100,1,-1):
    if moment(a) == 1:
        print(a)
        break


#задание № 16 
import functools as fn
@fn.lru_cache
def f(n):
    if n < 3: return n
    if n > 2: return (2*n-1)*(f(n-1)+f(n-2))
print(f(69)%(10**9+7))

#задание № 17 
with open('17_10100.txt','r',encoding='utf-8') as f:
    result = list()
    counter=0
    before = [int(i) for i in f]
    max_coord = max([i for i in before if abs(i)%100 == 13])
    for i in range(len(before)-2):
        if ((99 < abs(before[i]) <= 999)+ (99 < abs(before[i+1])<=999) + (99<abs(before[i+2])<=999))==2 and sum([before[i],before[i+1],before[i+2]])<=max_coord:
           counter+=1
           result.append(sum([before[i],before[i+1],before[i+2]]))
    print(counter,max(result))

# задание 15 
def f(x,y,a):
    return (x+2*y < a) or (y>x) or (x>60)

for a in range(1000):
    if all(f(x,y,a) for x in range(100) for y in range(100)):
        print(a)
        break
# задание № 9 
with open("9_9892.csv",'r') as f:
    a,k,counter = 0,0,0
    arr = [list(map(int,i.split(','))) for i in f ]

    for i in range(len(arr)):
        k+=1
        x = sorted(arr[i])
        if len(set(x)) == len(x) and 2 *(x[0]*x[1]) <sum(sorted(x[2:])):
            a +=k
            counter+=1
    print(a//counter)
#Задание № 5 (11562)
def f(x):
    res = ''
    while x!=0:
        res+=str(x%6)
        x//=6
    return res[::-1]

arr = []
for n in range(1,1000):
    i = f(n)
    if n % 3 == 0:
        i  = i + i[:2]
    else:
        i = i + f(n%3*10)

    if int(i,6)>680:
        arr.append(int(i,6))
print(min(arr))

#Задание № 8 (10710)

result = list()
words = sorted(product('компьютер',repeat= 5))
for i,j in enumerate(words,1):
    if i % 2 != 0 and j[0]!='ь' and j.count('к')==2:
        result.append(i)
print(max(result))

#Задание № 9 (10711)
with open('9_10711.csv','r') as f:
    file = [list(map(int,i.split(';'))) for i in f]
    counter = 1
    dictionary = dict()
    for i in range(len(file)):
        #Условие № 1
        first_condition = list(filter(lambda x : file[i].count(x)==2,file[i]))
        second_condition = list(filter(lambda x : file[i].count(x)==1,file[i]))
        if len(set(first_condition)) == 2 and len(second_condition)==3 and not max(file[i]) in first_condition:
            dictionary[counter] = file[i]
        counter+=1
    print(sum(dictionary[min(dictionary)]))

# Задание № 14(11564)


for x in range(149,0,-1):
    if (5*(150**4) + 1*(150**3) + x*(150**2) + 2*(150**1)+ 9*(150**0) + x * (150**3) + 2 *(150) +3)%149==0:
        print((5*(150**4) + 1*(150**3) + x*(150**2) + 2*(150**1)+ 9*(150**0) + x * (150**3) + 2 *(150) +3)//149)


#вариант от яндекса 2 (25 задание эффективный поиск делителей числа)

def deliter(n):
    large_divisors = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
           yield divisor

k = 0
for i in range(650000,10**6):
  s = list(map(int,list(deliter(i))))
  if len(s)==6 and len(str(max(s)+min(s)))==4 and k <= 4:
    print(i,min(s)+max(s))
    k+=1


# Задание № 5 (12914)
res = []
for n in range(1,100):
    r = bin(n)[2::]
    if n % 3 == 0:
        r = r.replace('0','11')
    else:
        r = r.replace('1','10')
    if int(r,2) <=161:
        res.append(int(r,2))
print(max(res))



#задание № 8 (12917)

inf = set(permutations('просто'))
res = set()

for i in inf:
    if all([True if  i[j]!=i[j+1] else False for j in range(len(i)-1) ]):
        res.add(i)

print(len(res))

#задание № 9 (12918)
with open('EGE/9_12918.csv','r') as f:

    file_info = [list(map(int,i.split(';'))) for i in f]

    for i in file_info:

        arr_condition_1 = set(filter(lambda x: i.count(x) == 2,i))
        arr_condition_2 = set(filter(lambda x: i.count(x) == 1,i))
        arr_condition_3 = sorted(i)

        if  len(arr_condition_1) == 2 and len(arr_condition_2) == 2 and not arr_condition_3[-1] in arr_condition_1 and (arr_condition_3[0]*arr_condition_3[-1])>sum(arr_condition_3[1:-1]):
            print(sum(arr_condition_3))
            break


# задание № 15(12924)
p = [i for i in range(2,21,2)]
q = [i for i in range(3,31,3)]
a = [i for i in range(-100,1000)]
s = set()

for x in a:
    if (((x in a)<=(x in p)) and (not(x in q) <= (not (x in a)))) == True:
        s.add(x)
print(print(s))


# задание № 16(12925)

from math import factorial

print(factorial(2024)//factorial(2022))





combination = set(product('01',repeat = 3))
k = 0
for i in combination:
    s = '00010' + ''.join(i)
    if not '101' in s:
        k+=1

print(k)
'''
# для определения переменных (2 задание)
