#Задание № 9 (10711)

with open('9_10711.csv','r') as f:
    file = [list(map(int,i.split(';'))) for i in f]
    counter = 1
    dictionary = dict()
    for i in range(len(file)):
        #Условие № 1
        first_condition = list(filter(lambda x : file[i].count(x)==2,file[i]))
        second_condition = list(filter(lambda x : file[i].count(x)==1,file[i]))
        if len(set(first_condition)) == 2 and len(second_condition)==3 and not max(file[i]) in first_condition:
            dictionary[counter] = file[i]
        counter+=1
    print(sum(dictionary[min(dictionary)]))


#вариант 7 от яндекс
with open('9 (3).csv') as f:
    file = [list(map(int,i.split(';')))for i in f]
    counter = 0
    for i in range(len(file)):
        condit_1 = list(filter(lambda x : file[i].count(x) == 3,file[i]))
        condit_2 = list(filter(lambda x : file[i].count(x) == 1,file[i]))
        condit_3 = sum(file[i])

        if len(set(condit_1)) == 1 and len(set(file[i])) == 5 and condit_3 < 502:
            counter+=1

    print(counter) 