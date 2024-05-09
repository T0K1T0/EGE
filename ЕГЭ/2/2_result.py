# для определения переменных (2 задание)

from itertools import *
'''
def g(x,y,z):
    return (not(x) and y and z) or (not(x) and not(z))

table = [(0,0,0),(1,0,0),(1,1,0)]

for i in permutations('xyz'):
    if [g(**dict(zip(i,p)))for p in table ] == [1,1,1]:
        print(i)


#для определения переменных (2 задание) + подстановка числовых значенией

def f(x,y,z,w):
    return ((y<=x) or ((not z) and w)) == (w==x)

for a in product([0,1],repeat=3):
    tables = [(a[0],1,0,0),(0,0,0,1),(0,1,a[1],a[2])]
    if len(tables) == len(set(tables)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,k))) for k in tables] == [1,1,1]:
                print(p)


# вариант от Яндекса № 5 
def f(x,w,y):
    return (x and (w<=y)) == 1


for i in product([0,1],repeat=16):
    table = [(i[0],0,i[1]),(i[2],i[3],0),(i[4],0,i[5]),(i[6],0,i[7]),(i[8],0,i[9]),(i[10],1,i[11]),
            (i[12],i[13],1),(i[14],1,i[15])]

    if len(table) == len(set(table)):
        for j in permutations('xwy'):
            if [f(**dict(zip(j,k))) for k in table] == [0,0,0,0,0,1,1,1]:
                print(j)

'''
# вариант № 7
def F(x,y,w,u):
    return (not((y<=w)==x)) and u

for com in product([0,1],repeat= 3):
    table = [(0,1,0,com[0]),(0,1,1,1),(1,0,1,com[1]),(1,com[2],1,1)]
    if len(table) == len(set(table)):
        for p in permutations('xywu'):
            if [F(**dict(zip(p,j))) for j in table] == [0,0,1,1]:
                print(p)

                