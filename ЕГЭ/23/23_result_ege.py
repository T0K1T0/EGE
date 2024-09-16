# Вариант от Яндекса № 7
def f(x, y):
    if x > y or x == 11:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x+1, y) + f(x*3, y) + f(x+4, y)


print(f(7, 27)*f(27, 42))


# Вариант Бахтиева(2024 - 2025)
def func(num_1, num_2):
    if num_1 > num_2 or num_1 == 22:
        return 0
    if num_1 == num_2:
        return 1
    return func(num_1 + 3, num_2) + func(num_1 + 4, num_2)


print(func(num_1=16, num_2=38))
