with open('24 (1).txt') as f:
    p = f.read()
    max_len = 0
    cur_len = 4
    for i in range(4, len(p)):
        if (p[i-4] == "A" and p[i-3] == "H" and
                p[i-2] == "A" and p[i-1] == "H" and
                p[i] == "A"):
            if max_len < cur_len:
                max_len = cur_len
            cur_len = 4
        else:
            cur_len += 1
    if max_len < cur_len:
        max_len = cur_len

    print(max_len)


# Вариант Бахтиева(2024 - 2025)
with open('kege_contest/data_base/24 (3).txt', 'r') as f:
    text = [j for i in f for j in i]
    j = 1
    max_lenth = 0
    for i in range(len(text)-1):
        if (text[i] + text[i+1]) in ['++', '**', '+*', '*+']:
            max_lenth = max(max_lenth, j)
            j = 1
        else:
            j += 1
    max_lenth = max(max_lenth, j)

print(max_lenth)
