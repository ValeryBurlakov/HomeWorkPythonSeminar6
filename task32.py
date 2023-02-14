import random
array_length = int(input("Введите длину массива: "))
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# for i in range(array_length):
#     # list_1.append(int(input("вводите элементы массива: ")))
#     list_1.append(random.randint(-9, 9))
print(list_1)
list_2 = []
list_3 = []
list_4 = []
range_start = int(input("Задайте начало диапазона: "))
end_of_range = int(input("Введите конец диапазона: "))


print(f"индексы элементов, значения которых принадлежат диапазону {range_start}:{end_of_range}: ")
for i in range(1, len(list_1) - 1):
    if range_start <= list_1[i] <= end_of_range:
        list_4.append(list_1[i])
        print(i, end= "\t")
print()



for i in range(1, len(list_1) - 1):
    if range_start <= list_1[i] <= end_of_range:
        list_3.append(list_1[i])
        print(list_1[i], end= "\t")
# print(f"Диапазон в значениях: {list_3}")
print()
for i in range(range_start, end_of_range):
    list_2.append(list_1[i])
print(f"Диапазон в индексах: {list_2}")