from sys import setrecursionlimit


# Вариант Бахтиева(2024 - 2025)
def func(n):
    if n > 400:
        return n*n
    else:
        return n + 6 + func(n+12)
print(func(72)-func(108)) 


# Вариант Бахтиева(2024 - 2025) -> № 2
limit = setrecursionlimit(4040)
def function(n):
    if n < 5:
        return 4**4
    if n > 4:
        return 4 * function(n-4) + 4

print(function(4048)//function(4036))