#первое задание

# duration = int(input('Введите целое значение: '))
# sek = duration
# minute = duration // 60
# hour = minute // 60
# day = hour // 24
# final_duration = duration % 60
# print((day), "дней", (hour), "часов", (minute), "минут", (final_duration),"секунд" )

# # второе задание
# # list1 = [i**3 for i in range (1,100,2)]
# # print(list1)
# # list = list(range(1,1000,2))
# # print(list)
# # list = []
# # for i in range (1, 1000,2):
# #                 list.append(i)
# # print(list)
# list = [i for i in range (1, 1000,2)] #тоже самое разными словами, список кубов нечетных чисел
# print(list)
# list_1 = [sum(i%7 for i in list)]
# print(list_1)
# # list_2 = [i+17 for i in list] #первое решение
# # print(list_2)
# list_2 = [(i+17)%7 for i in list]
# print (sum(list_2))
#
# # list_3 = [sum(i%7 for i in list_2)]
# # print(list_3)

#3 задание
a = int(input('введите число до 234 :'))
for i in range (1,a+1):
    if i % 10==1 and i % 100 != 11 and i % 1000 != 11:
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i% 10 == 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')















