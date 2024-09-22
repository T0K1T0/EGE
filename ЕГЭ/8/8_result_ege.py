from itertools import product, permutations


# Задание № 10710
result = list()
words = sorted(product('компьютер', repeat=5))
for i,word in enumerate(words, 1):
    if i % 2 != 0 and word[0] != 'ь' and word.count('к') == 2:
        result.append(i)
print(max(result))


# Вариант от Яндекса № 4
result = []
for i in product('0123456', repeat=6):
    if i[0]!='0' and i.count('0') == 1 and sum([i.count(j) for j in '246']) % 2 == 0:
        result.append(i)
print(len(result))


# Вариант от Яндекса № 5
res = []
for i in product('0123456789abcdef', repeat=5):
    if sum([i.count(j) for j in '0123456789']) == 1 and i[0] != '0':
        res.append(i)
print(len(res))


# Вариант от Яндекса № 7
res = set()
comb = [''.join(i) for i in product('ВОЗДУХ', repeat=5)]
chek = [(0, 1), (1, 0)]
chek_2 = ['ОВ', 'ВО', 'ХО', 'ОХ', 'УВ', 'ВУ', 'УХ', 'ХУ']
for word in comb:
    if ((word.count('О'), word.count('У')) in chek and not any(i for i in chek_2 if i in word)):
        res.add(word)
print(len(res))


# Вариант Бахтиева(2024 - 2025)
result = []
letters = 'БЕНРСТЬЯ'
for i, letter in enumerate(product(letters, repeat=5), 1):
    if i % 2 == 0 and letter[0] == 'Р' and not 'Ь' in letter:
        result.append(i)
print(max(result))


# Вариант Бахтиева(2024 - 2025) -> № 2
letters = 'люстра'
words = set()
for combinations in product(letters, repeat=5):
    if (combinations.count('ю') <= 2 and 
        not combinations[-1]  in 'лстр'):
        words.add(combinations)