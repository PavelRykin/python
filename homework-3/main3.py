# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
number = int(input("Введите число: "))

list_1 = []

for i in range(1, number + 1, 1):
    list_1.append(i)

print(*list_1)

number2 = int(input("Введите число, а я проверю сколько раз оно встречается в данном массиве: "))
count = 0
for i in list_1:
    if number2 == i:
        count += 1

print("Данное число встречается ", count, "раз" )
