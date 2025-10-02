array_len = int(input("Введите желаемое колво чисел в массиве"))

array = []
for i in range(array_len):
    num = int(input())
    array.append(num)
print(array) #Массив до сортировки

#Сортировка пузырьком
for i in range(array_len - 1):
    for j in range(array_len - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array) #Массив после сортировки