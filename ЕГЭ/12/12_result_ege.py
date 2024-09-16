#Задание № 12921
for i in range(4, 10000):
    s = '5' + '2'*i
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if sum(map(int, s)) % 10 == 7:
        print(i)
        break

#Вариант Бахтиева(2024 - 2025)
string = '9'*68
while '22222' in string or '9999' in string:
    if '22222' in string:
        string = string.replace('22222', '99', 1)
    else:
        string = string.replace('9999', '29', 1)
print(string.count('9'))
