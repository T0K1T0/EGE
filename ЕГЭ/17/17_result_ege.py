#задание № 17 
with open('17_10100.txt','r',encoding='utf-8') as f:
    result = list()
    counter=0
    before = [int(i) for i in f]
    max_coord = max([i for i in before if abs(i)%100 == 13])
    for i in range(len(before)-2):
        if ((99 < abs(before[i]) <= 999)+ (99 < abs(before[i+1])<=999) + (99<abs(before[i+2])<=999))==2 and sum([before[i],before[i+1],before[i+2]])<=max_coord:
           counter+=1
           result.append(sum([before[i],before[i+1],before[i+2]]))
    print(counter,max(result))