#вариант номер 7 от Яндекса
'''


def deliter(num):
    max_arr = []
    for d in range(1,int(num**0.5)+1):
        if num % d == 0 and d % 2 == 0:
            yield d
        
        if d * d!=num:
            max_arr.append(num / d)

    for r in reversed(max_arr):
        if r % 2 == 0 :
            yield r


def result():
    for i in range(397438,443520+1):
        arr = list(deliter(i))[:-1]
        if len(arr) > 141:
            print(len(arr),max(arr))


result()

'''
#вариант 8 от яндекса 
def deliter(num):
    max_arr = []
    for d in range(2,int(num**0.5)+1):
        if num % d == 0:
            yield d
        
            if d *d!=num:
                max_arr.append(num / d)

    for r in reversed(max_arr):
        yield r


counter = 0

for i in range(424244,10**9):

    arr = list(deliter(i))

    if counter == 8:
        break

    if arr and (max(arr) + min(arr))% 2024 == 42:
        counter+=1
        print(i,max(arr) + min(arr))

