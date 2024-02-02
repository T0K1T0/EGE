'''
#задание № 8 
from itertools import *
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
'''