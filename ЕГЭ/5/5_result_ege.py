# Задание № 11562
def six(x):
    res = ''
    while x:
        res += str(x%6)
        x //= 6
    return res[::-1]

arr = []
for n in range(1, 1000):
    i = six(n)
    if n % 3 == 0:
        i  = i + i[:2]
    else:
        i = i + six((n%3) * 10)

    if int(i, 6) > 680:
        arr.append(int(i, 6))
print(min(arr))

# Задание № 12914
res = []
for n in range(1, 100):
    r = bin(n)[2::]
    if n % 3 == 0:
        r = r.replace('0', '11')
    else:
        r = r.replace('1', '10')
    if int(r,2) <= 161:
        res.append(int(r, 2))
print(max(res))

# Вариант от Яндекса № 4
def three(x):
    res = ''
    if x == 0:
        return '0'
    while x:
        res += str(x%3)
        x //= 3
    return res[::-1]

for i in range(1000, 1, -1):
    r = three(i)
    r+=three(r.count('2'))
    r+=three(r.count('1'))
    r+=three(r.count('0'))

    if int(r, 3) < 1000:
        print(i)
        break

# Вариант от Яндекса № 5
for n in range(1000, 10**4):
    t = sum(map(int, str(n)))
    ost = sorted([str(t % int(i)) if i != '0' else '' for i in str(n)])[::-1]
    if int(''.join(ost)) > 2000:
        print(n)
        break

# Вариант от Яндекса № 7
def seven(n):
    res = ''
    while n:
        res += str(n%7)
        n //= 7
    return res[::-1]

for i in range(100, 1, -1):
    n = seven(i)
    if i % 7 == 0:
        n += n[-2:]
    else:
        n += seven((i%7) * 2)
    if int(n, 7) < 220:
        print(i)
        break

# Вариант Бахтиева(2024 - 2025)
result = []
for n in range(1, 1000):
    r = bin(n)[2::]
    if sum(map(int, r)) % 2 == 0:
        r = r + '11'
    else:
        r = r + '10'
    r = int(r, 2)
    if r > 61:
        result.append(r)
print(min(result))