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
'''
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
