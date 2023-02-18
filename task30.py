first_number = int(input("Введите первый элемент прогрессии: "))
step_number = int(input("Введите разность элементов(шаг): "))
numbers_of_digits = int(input("Введите количество элементов: "))

list_1 = []

for i in range(numbers_of_digits):
    result = first_number + i * step_number
    list_1.append(result)
print(list_1)
