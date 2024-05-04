a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

count_negatives = 0
if a < 0:
    count_negatives += 1
if b < 0:
    count_negatives += 1
if c < 0:
    count_negatives += 1

print("Количество отрицательных чисел среди a, b, c:", count_negatives)