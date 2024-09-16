#Вариант Бахтиева(2024 - 2025)
def quarterly_system(number):
    result = ''
    while number: 
        result += str(number % 4)
        number //= 4
    return result[::-1]

expression = 4**464 + 4**432 + 16**35 - 64**3
print(quarterly_system(expression).count('3'))