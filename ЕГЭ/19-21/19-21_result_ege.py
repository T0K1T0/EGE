# Вариант от Яндекса № 7
# 19
def f(a, n, m):
    if a + n >= 150:
        return m == 0
    if m == 0:
        return 0
    h = [
        f(a+2, n, m-1),
        f(a*3, n, m-1),
        f(a, n+2, m-1),
        f(a, n*3, m-1)
        ]
    return any(h) if m % 2 != 0 else any(h)


print([n for n in range(1, 134) if f(16, n, 2)])


# 20
def f(a, n, m):
    if a + n >= 150:
        return m == 0
    if m == 0:
        return 0
    h = [
        f(a+2, n, m-1),
        f(a*3, n, m-1),
        f(a, n+2, m-1),
        f(a, n*3, m-1)
        ]
    return any(h) if m % 2 != 0 else all(h)

print([n for n in range(1, 134) if not f(16, n, 1) and f(16, n, 3)])


# Вариант Бахтиева(2024 - 2025)
# 19
def game_stone(s1, m):
    if s1 >= 54:
        return m == 0
    if m == 0:
        return 0
    h = [game_stone(s1+2, m-1), game_stone(s1*2, m-1)]
    return any(h) if m % 2 != 0 else all(h)


# 20
def game_stone(s1, m):
    if s1 >= 54:
        return m == 0
    if m == 0:
        return 0
    h = [game_stone(s1+2, m-1), game_stone(s1*2, m-1)]
    return any(h) if m % 2 != 0 else all(h)


print([s1 for s1 in range(1, 54) if game_stone(s1, 2)])
print([s1 for s1 in range(1, 54) if not (game_stone(s1, 1)) and
       game_stone(s1, 3)])