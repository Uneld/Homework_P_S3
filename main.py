from random import randint

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

listDctr = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {" V ": "S009"},
    {" VIII ": "S007"},
]
print(listDctr)

setItems = set()
for item in listDctr:
    for val in item.values():
        setItems.add(val)
print(setItems)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
# 0 -1 5 2 3

inputInt = [int(i) for i in input("Введите числа через пробел: ").split(" ")]
print(inputInt)

# Способ 1
resList = [
    inputInt[i] for i in range(1, len(inputInt)) if inputInt[i] > inputInt[i - 1]
]
print(len(resList))

# Способ 2
res = 0
for i in range(1, len(inputInt)):
    if inputInt[i] > inputInt[i - 1]:
        res += 1
print(res)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите число N: "))
inputList = [randint(1, N) for i in range(N)]
print(inputList)
X = int(input("Введите число X: "))

# Способ 1
cnt = 0
for num in inputList:
    if num == X:
        cnt += 1
print(cnt)
# Способ 2
print(inputList.count(X))


# Задача №18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите число N: "))
inputList = [randint(1, N) for i in range(N)]
print(inputList)
X = int(input("Введите число X: "))

diff = 0
oldDiff = max(inputList)
resNum = 0
for num in inputList:
    diff = X - num
    if abs(diff) < abs(oldDiff):
        resNum = num
    oldDiff = diff
print(resNum)

# Задача №20. В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

eng = "qwertyuiopasdfghjklzxcvbnm"

rus = "йцукенгшщзхъфывапролджэячсмитьбюё"

list_English = {
    1: "AEIOULNSTR",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}
list_Russian = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФШЪ",
}

word = input("Введите слово на русском или английском языке: ")

if word[0].lower() in eng:
    summa = 0
    for letter in word:
        for key, value in list_English.items():
            if letter.upper() in value:
                summa += key
    print(f"стоимость введенного английского слова = {summa}")
else:
    if word[0].lower() in rus:
        summa = 0
        for letter in word:
            for key, value in list_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f"стоимость введенного русского слова = {summa}")
