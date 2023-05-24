# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# oneNumber = int(input("Первой число загаданное Петей? "))
# twoNumber = int(input("Второе число загаданное Петей? "))

# if oneNumber < 10:
#     for i in range(1, oneNumber + 1):
#         if i + i == oneNumber and i * i == oneNumber:
#             print("Вот подсказка к первому числу! - ", i,i)

# if oneNumber > 10 and oneNumber < 100:
#     x1 = oneNumber // 10
#     x2 = oneNumber % 10
#     for i in range(1, oneNumber + 1):
#         if i + i == x1 and i 

# number = int(input("Введите число: "))
# number1 = number // 10
# number2 = number % 10
# result1 = None
# result2 = None
# for i in range(1, 100):
#     for j in range(2, 100):
#         if i + j == number1:
#             result1 = str(i,j)
#         else:
#             i += j
#             j += i
# for i in range(1, 100):
#     for j in range(2, 100):
#         if i * j == number2:
#             result2 = str(i,j)
                
                    
#         else:
#             i += j
#             j += i

a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))
for i in range(a + b):
    for j in range(a + b):
        if i + j == a and i * j == b:
            print(i, j)
            break







