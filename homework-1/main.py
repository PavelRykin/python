# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число, а я найду сумму этих чисел: "))

result1 = number // 100
result2 = number % 100
result2 = result2 // 10
result3 = number % 10

print("Сумма этих чисел числа ", number, " равна: ", result1, "+", result2, "+", result3, "=", result1 + result2 + result3)

