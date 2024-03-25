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
