from itertools import (product, permutations)


# Вариант № 5 от Яндекса
def f(x, w, y):
    return (x and (w <= y)) == 1


for i in product([0, 1], repeat=16):
    table = [
            (i[0], 0, i[1]), (i[2], i[3], 0),
            (i[4], 0, i[5]), (i[6], 0, i[7]),
            (i[8], 0, i[9]), (i[10], 1, i[11]),
            (i[12], i[13], 1), (i[14], 1, i[15])
            ]
    if len(table) == len(set(table)):
        for j in permutations('xwy'):
            if ([f(**dict(zip(j, k))) for k in table] ==
                    [0, 0, 0, 0, 0, 1, 1, 1]):
                print(j)


# Вариант № 7 от Яндекса
def F(x, y, w, u):
    return (not ((y <= w) == x)) and u


for com in product([0, 1], repeat=3):
    table = [
            (0, 1, 0, com[0]),
            (0, 1, 1, 1),
            (1, 0, 1, com[1]),
            (1, com[2], 1, 1)
            ]
    if len(table) == len(set(table)):
        for p in permutations('xywu'):
            if [F(**dict(zip(p, j))) for j in table] == [0, 0, 1, 1]:
                print(p)


# Вариант Бахтиева(2024 - 2025) -> № 1
def get_combination(x, w, z, y):
    return (y <= x) and not (w) and z


for el in product([0, 1], repeat=4):
    tables = [(1, 0, 1, 1), (1, 0, el[0], 1), (el[1], el[2], el[3], 1)]
    if len(tables) == len(set(tables)):
        for p in permutations('xwzy'):
            if ([get_combination(**dict(zip(p, table)))
                    for table in tables] == [1, 1, 1]):
                print(p)


# Вариант Бахтиева(2024 - 2025) -> № 2
def f(w, x, y, z):
    return y and (x or z) and (not (y or z)) or w


for i in product([0, 1], repeat=4):
    table = [
            (1, i[0], 0, 1),
            (i[1], 1, 0, i[2]),
            (0, 0, i[3], 1)
            ] 
    if len(table) == len(set(table)):
        for j in permutations('wxyz'):
            if ([f(**dict(zip(j, k))) for k in table] ==
                    [0, 0, 0]):
                print(j)
                break