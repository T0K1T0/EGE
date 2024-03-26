# 2
def f(s,n,m):
    if s+n>=175:
        return m%2 == 0
    if  m == 0:
        return 0
    h = [f(s+1,n,m-1),f(s*3,n,m-1),f(s,n*3,m-1),f(s,n+1,m-1)] 
    return any(h) if m%2!=0 else all(h)

print([n for n in range(1,155) if not f(19,n,1) and f(19,n,3) ])


# 1
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

