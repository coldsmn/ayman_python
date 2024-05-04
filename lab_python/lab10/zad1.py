# Введите два множества чисел
print("Введите первое множество чисел через пробел:")
set1 = set(map(int, input().split()))

print("Введите второе множество чисел через пробел:")
set2 = set(map(int, input().split()))

# Найдем все различные числа в этих множествах
unique_numbers = set1.union(set2)
print("Уникальные числа в обоих множествах:", unique_numbers)

# Найдем числа, которые входят как в первое, так и во второе множество
common_numbers = sorted(set1.intersection(set2))
print("Числа, входящие в оба множества в порядке возрастания:", common_numbers)
