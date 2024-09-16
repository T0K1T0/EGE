#Задание № 10711
with open('9_10711.csv', 'r') as f:
    file = [list(map(int, i.split(';'))) for i in f]
    counter = 1
    dictionary = dict()
    for i in range(len(file)):
        first_condition = list(filter(lambda x : file[i].count(x) == 2, file[i]))
        second_condition = list(filter(lambda x : file[i].count(x) == 1, file[i]))
        if (len(set(first_condition)) == 2 and len(second_condition) == 3 and
            not max(file[i]) in first_condition):
            dictionary[counter] = file[i]
        counter += 1
    print(sum(dictionary[min(dictionary)]))

#Вариант от Яндекса № 7
with open('9 (3).csv', 'r') as f:
    file = [list(map(int, i.split(';'))) for i in f]
    counter = 0
    for i in range(len(file)):
        condit_1 = list(filter(lambda x : file[i].count(x) == 3, file[i]))
        condit_2 = list(filter(lambda x : file[i].count(x) == 1, file[i]))
        condit_3 = sum(file[i])
        if (len(set(condit_1)) == 1 and 
            len(set(file[i])) == 5 and condit_3 < 502):
            counter += 1
    print(counter)

#Вариант Бахтиева(2024 - 2025)
lenth = 0
with open('kege_contest/data_base/9 (1).csv', 'r') as f:
    matrix = [list(map(int, string.split(';'))) for string in f ]
    for col in matrix:
        condition_1 = sorted(col)
        condition_2 = list(filter(lambda x : str(x)[-1] == '5', col))
        if (2*(sum(condition_1[3:])) > 3*(sum(condition_1[:3])) and 
            len(condition_2) >= 2):
            lenth += 1
    print(lenth)
    