#задание № 17 

with open('17_10100.txt','r',encoding='utf-8') as f:

    def c(x):
        return 99<abs(x)<=999
            

    result = list()
    before = [int(i) for i in f]
    max_coord = max([i for i in before if abs(i)%100 == 13])

    for i in range(len(before)-2):
        if (c(before[i+1])+ c(before[i])+c(before[i+2]))==2 and sum([before[i],before[i+1],before[i+2]])<=max_coord:
           result.append(sum([before[i],before[i+1],before[i+2]]))

    print(len(result),max(result))


# 4 вариант от Яндекса 
with open('17.txt','r') as  f:

    result = []
    a = [int(i) for i in f]
    max_coord = max([i for i in a if len(str(i)) == 4])

    def f(x):
        return abs(x) % 10 == 3 or abs(x) % 10 == 5

    for i in range(len(a)-2):
        if (f(a[i]) + f(a[i+2]) + f(a[i+1]))>1 and (a[i]*a[i+1]*a[i+2])<=max_coord**3:
            result.append(sum((a[i],a[i+1],a[i+2])))

    print(max(result),len(result))