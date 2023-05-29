# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# letter = {'english': {'A': 1,
#                       'E': 1,
#                       'I': 1,
#                       'O': 1,
#                       'U': 1,
#                       'L': 1,
#                       'N': 1,
#                       'S': 1,
#                       'T': 1,
#                       'R': 1}
#           'russian': {'А': 1,
#                       'В': 1}          
#           }


list_letter = {
    1: 'AEIOULNSTRАВЕИНОРСТ',
    2: 'DGДКЛМПУ',
    3: 'BCMPБГЁЬЯ',
    4: 'FHVWYЙЫ',
    5: 'KЖЗХЦЧ',
    8: 'JXШЭЮ',
    10: 'QZФЩЪ'
}

name_one = input("Первый игрок! Представьтесь, как вас зовут? ")
name_two = input("Второй игрок! Представьтесь, а как зовут вас? ")
print(name_one, "=)))")
letter1 = input("Введите своё слово: ").upper()
result1 = 0
print(name_two, "=)))")
letter2 = input("Теперь вы введите своё слово: ").upper()
result2 = 0

for i in letter1:
    for k, v in list_letter.items():
        if i in v:
            result1 += k

for i in letter2:
    for k, v in list_letter.items():
        if i in v:
            result2 += k

if result1 > result2:
    print("Выйграл", name_one, "!!!, так как ", name_one, " имеет ", result1, " очков, а ", name_two, " имеет ", result2, " очков")
elif result1 < result2:
    print("Выйграл ", name_two, "!!!, так как", name_one, " имеет ", result1, " очков, а ", name_two, " имеет ", result2, " очков")
elif result1 == result2:
    print("Победила ничья!!!")



















# word = input("Введите слово: ").upper()
# summa = 0
# for i in word:
#     for k, v in list_letter.items():
#         if i in v:
#             summa += k

# print("У вас ", summa, " очков!")

# letter_input = input("Введите слово: ").upper()
# letter = []
# result = 0

# for i in letter_input:
#     letter.append(i)

# for i in letter:
#     if i == list_letter
