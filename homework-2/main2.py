# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

summaMonet = int(input("Сколько всего монет на столе? "))

reshka = 0
orel = 0

for i in range(1, summaMonet + 1):
    print(i, " эта монета лежит стороной решка? ")
    question = str(input("да или нет? "))
    if question == "да":
        reshka += 1
    elif question == "нет":
        orel += 1

if reshka > orel:
    print("Переверните ", orel, " монет орла!")
elif reshka < orel:
    print("Переверните ", reshka, " монет решки!")

