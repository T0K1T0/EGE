#Вариант Бахтиева(2024 - 2025)
def func(n):
    if n > 400:
        return n*n
    else:
        return n + 6 + func(n+12)
print(func(72)-func(108))  