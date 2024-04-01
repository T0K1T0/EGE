# вариант от яндекса № 4

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
