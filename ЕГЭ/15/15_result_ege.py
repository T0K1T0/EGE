
# задание № 15(12924)
p = [i for i in range(2,21,2)]
q = [i for i in range(3,31,3)]
a = [i for i in range(-100,1000)]
s = set()

for x in a:
    if (((x in a)<=(x in p)) and (not(x in q) <= (not (x in a)))) == True:
        s.add(x)
print(s)

# задание 15 
def f(x,y,a):
    return (x+2*y < a) or (y>x) or (x>60)

for a in range(1000):
    if all(f(x,y,a) for x in range(100) for y in range(100)):
        print(a)
        break

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

# вариант от Яндекса № 4
def f(a):
    for x in range(100):
        s = (x&91==0)or ((x&77==0)<=(x&a!=0))
        if s!=1:
            return 0
    return 1 

for a in range(100):
    if f(a) == 1:
        print(a)
        break


#вариант 7 от Яндекса 

def result(a):
    for x in range(100):
        for y in range(100):
            if (((x >= a) or (121 >= x ** 2)) and ((y ** 2 < 49 ) or (a<y))) == False:
                return False
    return True

for a in range(100,1,-1):
    if result(a):
        print(a)
        break
    