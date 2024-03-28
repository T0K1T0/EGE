# вариант от яндекса № 4
import re 
with open('24.txt','r') as f:
    inf = ''.join([i for i in f])
    res = list(map(int,re.findall(r'\d+',inf)))
print(max(res))