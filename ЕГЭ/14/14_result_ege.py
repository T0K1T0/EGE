# Вариант Бахтиева(2024 - 2025)
def quarterly_system(number):
    result = ''
    while number: 
        result += str(number % 4)
        number //= 4
    return result[::-1]

expression = 4**464 + 4**432 + 16**35 - 64**3
print(quarterly_system(expression).count('3'))


# Вариант Бахтиева(2024 - 2025) -> № 2
def function(number, sys):
    res, i = 0, -1
    for n in number[::-1]:
        i += 1
        if n.isdigit():
            res = res + sys**i * int(n)
        else:
            res = res + sys**i * x
    return res


for x in range(0, 24):
    expression = (
                function('12x734', 24) 
                + function('8x95x3', 24)
                + function('24x796', 24)
                )
    if expression % 23 == 0:
        print(expression // 23)