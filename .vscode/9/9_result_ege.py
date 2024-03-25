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