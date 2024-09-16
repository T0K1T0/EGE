

# Задание №
def c(x):
    return 99 < abs(x) <= 999


with open('17_10100.txt', 'r', encoding='utf-8') as f:
    result = list()
    before = [int(i) for i in f]
    max_coord = max([i for i in before if abs(i) % 100 == 13])
    for i in range(len(before)-2):
        if ((c(before[i+1])+c(before[i])+c(before[i+2])) == 2 and
                sum([before[i], before[i+1], before[i+2]]) <= max_coord):
            result.append(sum([before[i], before[i+1], before[i+2]]))
    print(len(result), max(result))


# Вариант от Яндекса № 4
def f(x):
    return abs(x) % 10 == 3 or abs(x) % 10 == 5


with open('17.txt', 'r') as f:
    result = []
    a = [int(i) for i in f]
    max_coord = max([i for i in a if len(str(i)) == 4])
    for i in range(len(a)-2):
        if ((f(a[i])+f(a[i+2])+f(a[i+1])) > 1 and
                (a[i]*a[i+1]*a[i+2]) <= max_coord**3):
            result.append(sum((a[i], a[i+1], a[i+2])))
    print(max(result), len(result))


# Вариант Бахтиева(2024 - 2025)
with open('kege_contest/data_base/17 (1).txt', 'r') as f:
    numbers = [int(s) for s in f]
    min_elements = min(numbers)
    counter, max_sum, n = 0, 0, len(numbers)
    for i in range(n-1):
        expression = (numbers[i] % 77) + (numbers[i+1] % 77)
        if expression == min_elements:
            max_sum = max(numbers[i]+numbers[i+1], max_sum)
            counter += 1
    print(counter, max_sum)
