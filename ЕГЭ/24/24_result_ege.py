# вариант от яндекса № 4
'''
import re 

with open('24.txt','r') as f:
    inf = ''.join([i for i in f])
    res = list(map(int,re.findall(r'\d+',inf)))
print(max(res))

#14100
with open('24-14100_14100.txt','r') as s:

    s = ''.join([i for i in s])
    arr = [''] * len(s)
    prim = ['ABA', 'CB', 'AC' , 'BB', 'ABC', 'BCB', 'BA', 'AB']

    for i in range(1, len(s)):
        for j in prim:
            if i >= len(j) - 1:
                if s[i-len(j)+1:i+1]==j:
                    arr[i] = max(dp[i], arr[i-len(j)] + j,key=len)

print(len(max(arr, key = len)))

with open('24 (1).txt') as f:
    p = ''.join([i for i in f])
    max_len = 0
    cur_len = 4
    for i in range(4, len(p)):
        if p[i- 4] == "A" and p[i - 3] == "H" and p[i - 2] == "A" and p[i-1] == "H" and p[i]=="A":
            if max_len < cur_len:
                max_len = cur_len
            cur_len = 4
        else:
            cur_len += 1
    if max_len < cur_len:
        max_len = cur_len
    print(max_len)
'''
#вариант № 6 от яндекса
with open('24 (2).txt','r') as f:

    s = ''.join([i for i in f]).replace('E','A').replace('O','A').replace('U','A').replace('L','B').replace('N','B').replace('M','B').replace('K','B')

    max_lenth,now_lenth = 0,0
    for i in range(len(s)-1):
        if 'AA' in s[i]+s[i+1] or 'BB' in s[i]+s[i+1]:
            max_lenth = max(max_lenth,now_lenth+1)
            now_lenth = 0
        else:
            now_lenth+=1


        max_lenth = max(max_lenth,now_lenth)

    print(max_lenth)