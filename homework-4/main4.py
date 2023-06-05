# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

count_one = int(input("Введите количество элементов в первом множестве: "))
count_two = int(input("Введите количество элементов во втором множестве: "))

array_one = []
array_two = []

for i in range(count_one):
    array_one.append(int(input("Введите элемент первого множества: ")))

for j in range(count_two):
    array_two.append(int(input("Введите элемент второго множества: ")))

array_three = []

for i in array_one:
    if i in array_two and i not in array_three:
        array_three.append(i)

array_three.sort()

print(array_three)
