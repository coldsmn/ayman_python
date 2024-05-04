m = int(input("Введите целое число m: "))
n = int(input("Введите целое число n: "))

if m != n:
    max_num = max(m, n)
    m = max_num
    n = max_num
else:
    m = 0
    n = 0

print("Измененные значения m и n:", m, n)
