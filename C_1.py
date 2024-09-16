##Вариант Бахтиева(2024 - 2025)
# from itertools import * 

## 2
# def get_combination(x, w, z, y):
#     return (y <= x) and not(w) and z

# for el in product([0, 1], repeat=4):
#     tables = [(1, 0, 1, 1), (1, 0, el[0], 1), (el[1], el[2], el[3], 1)]
#     if len(tables) == len(set(tables)):
#         for p in permutations('xwzy'):
#             if ([get_combination(**dict(zip(p, table)))
#                    for table in tables] == [1, 1, 1]):
#                 print(p)
## 5
# result = []
# for n in range(1, 1000):
#     r = bin(n)[2::]
#     if sum(map(int, r)) % 2 == 0:
#         r = r + '11'
#     else:
#         r = r + '10'

#     r = int(r, 2)
#     if r > 61:
#         result.append(r)

# print(min(result))
    
## 8
# result = []
# letters = 'БЕНРСТЬЯ'

# for number, letter in enumerate(product(letters, repeat=5), 1):
#     if number % 2 == 0 and letter[0] == 'Р' and not 'Ь' in letter:
#         result.append(number)

# print(max(result))

## 9
# lenth = 0
# with open('kege_contest/data_base/9 (1).csv', 'r') as f:
#     matrix = [list(map(int, string.split(';'))) for string in f ]
#     for col in matrix:
#         condition_1 = sorted(col)
#         condition_2 = list(filter(lambda x:str(x)[-1] == '5', col))
#         if 2*(sum(condition_1[3:])) > 3*(sum(condition_1[:3])) and len(condition_2) >= 2:
#             lenth += 1

#     print(lenth)

## 12
# string = '9' * 68
# while '22222' in string or '9999' in string:
#     if '22222' in string:
#         string = string.replace('22222', '99', 1)
#     else:
#         string = string.replace('9999', '29', 1)
        
# print(string.count('9'))

## 14
# def quarterly_system(number):
#     result = ''
#     while number: 
#         result += str(number % 4)
#         number //= 4

#     return result[::-1]

# expression = 4**464 + 4**432 + 16**35 - 64**3
# print(quarterly_system(expression).count('3'))

## 15
# def matematical_expression(A):
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if ((x <= 19) or (y < 2*x + A - 50) or (y > 17)) == False:
#                 return False
#     return True

# for A in range(0, 1000):
#     if matematical_expression(A):
#         print(A)
#         break
## 16
# def func(n):
#     if n > 400:
#         return n*n
#     else:
#         return n + 6 + func(n+12)

# print(func(72)-func(108))    
# # 17
# with open('kege_contest/data_base/17 (1).txt','r') as f:
#     numbers = [int(s) for s in f]
#     min_elements = min(numbers)
#     counter, max_sum, n = 0, 0, len(numbers)

#     for i in range(n-1):
#         expression = (numbers[i] % 77) + (numbers[i+1] % 77)
#         if expression == min_elements:
#             max_sum = max(numbers[i] + numbers[i+1], max_sum)
#             counter += 1
#     print(counter,max_sum)
    
## 23
# def func(num_1, num_2):
#     if num_1 > num_2 or num_1 == 22:
#         return 0
#     if num_1 == num_2:
#         return 1
#     return func(num_1 + 3, num_2) + func(num_1 + 4, num_2)
# print(func(num_1=16, num_2=38))

## 25
# from fnmatch import fnmatch

# for number in range(2025, 10**10, 2025):
#     if fnmatch(str(number), '21?3*145?5'):
#         print(number, number // 2025)

## 19 - 21

# def game_stone(s1, m):
#     if s1 >= 54:
#         return m == 0

#     if m == 0:
#         return 0

#     h = [game_stone(s1+2, m-1), game_stone(s1*2, m-1)]

#     return any(h) if m % 2 != 0 else all(h)

# print([s1 for s1 in range(1, 54) if game_stone(s1, 2)])

# def game_stone(s1, m):
#     if s1 >= 54:
#         return m == 0

#     if m == 0:
#         return 0

#     h = [game_stone(s1+2, m-1),game_stone(s1*2, m-1)]

#     return any(h) if m % 2 != 0 else all(h)

# print([s1 for s1 in range(1, 54) if  not(game_stone(s1, 1)) and game_stone(s1, 3)])

## 13
# from ipaddress import *

# net = ip_network('228.172.236.0/255.255.240.0', 0)
# count = 0
# for ip in net:
#     if bin(int(ip))[2::].count('1') % 5:
#         count += 1
# print(count)

## 24
# with open('kege_contest/data_base/24 (3).txt', 'r') as f:
#     text = [j for i in f for j in i]
#     j = 1
#     max_lenth = 0
#     for i in range(len(text)-1):
#         if (text[i] + text[i+1]) in ['++', '**', '+*', '*+']:
#             max_lenth = max(max_lenth, j)
#             j = 1
#         else:
#             j += 1
#     max_lenth = max(max_lenth, j)   

# print(max_lenth)

#№17(13882)

def get_sum(numbers):
    res = []
    for num in numbers:
        res.append(sum(map(int, str(num))))# [100,672,3989] --> '100' --> [1, 0, 0] --> 1
    return res

with open(r'kege_contest/data_base/17_13882.txt', 'r') as f:
    numbers = [int(string) for string in f]
    max_elements = max([num for num in numbers if num % 401 == 0])
    min_sum, counter = float('inf'), 0
    for i in range(len(numbers)-2):
        trio = [numbers[i], numbers[i+1], numbers[i+2]]

        if len(set(get_sum(trio))) == 3  and sum(trio) > max_elements:
            min_sum = min(min_sum, sum(trio))
            counter += 1

    print(counter, min_sum)
