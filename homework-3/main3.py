# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

number = int(input("Введите число: "))
list_number = []

print("Вот полученный массив от о до ", number)

for i in range(1, number + 1):
    list_number.append(i)

print(*list_number)

number2 = int(input("Введите число: "))
result = 0
if number2 > len(list_number):
    result = len(list_number)
elif number2 <= len(list_number):
    result = number2 - 1
print(result)