# Вариант яндекс 4(работает и для двух куч)
'''
def f(a,n,m):
    if a+n>=180:
        return m%2 == 0
    if  m == 0:
        return 0
    h = [f(a+2,n,m-1),f(a,n+2,m-1),f(a+n,n,m-1),f(a,n+a,m-1)] 
    return any(h) if m%2!=0 else all(h)
print([n for n in range(1,155) if  not f(18,n,1)  and f(18,n,3)])


# 1 куча(шаблон)
def f(s,m):
    if s>=84:
        return m == 0
    if  m == 0:
        return 0
    h = [f(s+1,m-1)]
    if s%2==0:
        h+=[f(s*1.5,m-1)]
    else:
        h+=[f(s*2,m-1)]
    return any(h) if m%2!=0 else all(h)

print([n for n in range(1,83) if f(n,2) ])
'''
# вариант 7 от яндекса
# 19

def f(a,n,m):
    if a+n >=150:
        return m == 0

    if m == 0:
        return 0

    h = [f(a+2,n,m-1),f(a*3,n,m-1),f(a,n+2,m-1),f(a,n*3,m-1)]

    return any(h)if m%2!=0 else any(h)

print([n for n in range(1,134) if f(16,n,2)  ])
#20
def f(a,n,m):
    if a+n >=150:
        return m == 0

    if m == 0:
        return 0

    h = [f(a+2,n,m-1),f(a*3,n,m-1),f(a,n+2,m-1),f(a,n*3,m-1)]

    return any(h)if m%2!=0 else all(h)

print([n for n in range(1,134) if not f(16,n,1) and f(16,n,3) ])
