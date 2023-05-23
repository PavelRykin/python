# # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# # *Пример:*

# # 385916 -> yes
# # 123456 -> no

bilet = int(input("Напишите номер вашего шестизначного билета? "))

if bilet > 999999 or bilet < 100000:
    print("Неправильный номер, нужен шестизначный.") # проверка правальный ли номер
    bilet = int(input("Введите правильный: "))

result1 = bilet // 1000 # разделяем пополам числа номера билета
result2 = bilet % 1000

number1Result1 = result1 // 100
number2Result1 = (result1 % 100) // 10 
number3Result1 = result1 % 10
summaResult1 = number1Result1 + number2Result1 + number3Result1 # считаем сумму первый трёх чисел

number1Result2 = result2 // 100
number2Result2 = (result2 % 100) // 10
number3Result2 = result2 % 10
summaResult2 = number1Result2 + number2Result2 + number3Result2 # считаем сумму последних трёх чисел

if summaResult1 == summaResult2: # проверяем на равенство этих чисел на удачу
    print("Ура!!! ваш билет счастливый!!!")
else:
    print("Увы, ваш билет не счастливый")    