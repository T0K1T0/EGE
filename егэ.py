'''x = {}

for n in range(1,1000):
    i = bin(n)[2::]
    i ='1' + i[2::] + '0' if sum(map(int, i)) % 2 == 0 else '11' + i[2::] + '1'
    if int(i,2) > 49:  
        x[int(i,2)] = n
print(x[min(x)])

from itertools import * 
x = product('САКУРА', repeat = 5)
z = set([i for i in x if ''.join(i).count('А')<=1 and ''.join(i).count('У')<=1])#188
print(len(z))

from itertools import * 
x = product('wsda', repeat=4)
z = set([i for i in x if i[0]!='w' and i[1]!=i[2]])#150
print(len(z))

from itertools import * 
x = product('КАРКАС',repeat = 6)
z = [i for i in x if i.count('К') + i.count('Р') + i.count('С')>=3]#148
print(len(set(z)))

from itertools import * 
x = product('012345678',repeat = 7)
z = set([i for i in x if i.count('8') == 1 and (i[0] in '2468') and (i[-1] in '1357')])
print(len(z))

x = []
for i in range(1,1000):
    n = bin(i)[2::]
    n = n[:len(n)//2] + '000' + n[-(len(n)//2):] if len(n) % 2 == 0 else '1' + n + '01'
    x.append(i) if int(n,2) > 100 else None
print(min(x))

def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2 * f(n-1) + (n-2) * f(n-2)
print(f(6))

from itertools import * 
x = product('012345678',repeat = 6)
a = [''.join(i) for i in x if int(''.join(i),9)%2==0 and ''.join(i)[0]!='0']
x = [i for i in a if (i.count('8') + i.count('6')+ i.count('4')+i.count('2')+i.count('0'))<=2]
print(len(x))

x = []
for i in range(1,1000):
    r=g=''
    k = 0
    while i > 1:
        r=str(i%6) + r
        i = i//6
    if i % 4 == 0:
        r = r + r[:3]
    else:
        k=(i%4)*3
        while k > 1:
            g = str(k%6) + g
            k = k//6
        r = r + g
    if int(r,6) < 119:
        x.append(int(r,6))
print(max(x))

#6779

x = []
for i in range(1,1000):
    n = bin(i)[2::]
    n = '101'+n[3:] + '0' if n.count('1') % 2 == 0 else '10'+n[2:] + '11' 
    x.append(i) if int(n,2) > 68 else None
print(min(x))

x = []
for i in range(1,10000):
    res = ''
    n = bin(i)[2::]
    for j in n:
        if j == '0':
            res = res + '1'
        else:
            res = res + '0'
    if i - int(res,2) == 979:
        x.append(i)
print(min(x))

def find_outlier(integers):
    chet = [i for i in integers if i % 2 == 0]
    not_chet = [j for j in integers if j % 2 != 0]
    return chet[0] if len(chet) == 1 else not_chet[0]
print(find_outlier([2, 4, 6, 8, 10, 3]))

from itertools import *
x = set([''.join(i) for i in list(permutations("АВРОРА"))])
z = [i for i in x if not(i[0]==i[1] or i[1]==i[2] or  i[2]==i[3] or  i[3]==i[4] or  i[4]==i[5]) ]
print(len(z))

a = []
for i in range(1,1000):
    n = bin(i)[2::]
    if n.count('1') % 4 == 0:
        n = '10'+ n 
    else:
        n = '11' + n
    if n.count('1') % 2 == 0:
        n = n + '1'
    else:
        n = n + '0'
    if int(n,2)<=250:
        a.append(i)
print(max(a))
#457 

for n in range(10,100):
    s = ''
    x = ''.join([s+'0'*(4-len(bin(int(i))[2:]))+bin(int(i))[2:] if len(bin(int(i))[2:])<4 else s+bin(int(i))[2:] for i in str(n)])
    result = ''.join(['1' if i=='0' else '0'for i in x])

'''
#10717
'''
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


#10100
with open('17_10100.txt','r',encoding='utf-8') as s:
    after = [int(i) for i in s ]
    max_digit = max([int(i) for i in s if i[-2::] == '13'])
    after = [after[i+1] + after[i] + after[i+2] for i in range(len(after)-2) if ((100<=after[i]<=999) and (100<=after[i+1]<=999)and(100<=after[i+2]<=999)) == 2 and (after[i+1] + after[i] + after[i+2]) < max_digit ]
    print(len(after),max(after))
'''
#10771
'''
with open('17_10771.txt','r',encoding='utf-8') as s:
    befor = [int(i) for i in s]
    count = [(befor[i] + befor[i+1] +befor[i+2])for i in range(len(befor)-2) if (('3' in str(befor[i])) and('3' in str(befor[i+1])) and ('3' in str(befor[i+2])))==True ]
    after = [count[i]for i in range(1,len(count)) if len([j for j in range(1,30000) if count[i] % j == 0])==2 ]
    print(len(after),min(after))

import functools as fn
@fn.lru_cache
def f(n):
    if n < 3: return n
    if n > 2: return (2*n-1)*(f(n-1)+f(n-2))
print(f(69)%(10**9+7))
'''
'''from itertools import *
s = list(product('01',repeat = 4))
for i in s:
    if (int(i[0]) and (int(i[1])or int(i[2])) or not((int(i[0])or int(i[2]))) or int(i[3]))==False:
        print(i)

with open('17_12249.txt','r',encoding='utf-8') as f:
    result = list()
    counter=0
    before = [int(i) for i in f]
    max_coord = max([i for i in before if abs(i)%10 == 3 and len(str(abs(i)))==5])
    for i in range(len(before)-2):
        if any([abs(before[i])%10 ==3,abs(before[i+1])%10 ==3,abs(before[i+2])%10 ==3]) and sum([before[i],before[i+1],before[i+2]])<=max_coord:
           counter+=1
           result.append(sum([before[i],before[i+1],before[i+2]]))
    print(counter,max(result))

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
'''
# 15 

'''def f(x,y,a):
    return (x+2*y < a) or (y>x) or (x>60)
for a in range(1000):
    if all(f(x,y,a) for x in range(100) for y in range(100)):
        print(a)
        break''' 
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
