# для определения переменных (2 задание)

from itertools import *

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

