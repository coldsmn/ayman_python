# Ввод списка из 10 вещественных чисел
numbers = []
for i in range(10):
    num = float(input(f"Введите {i+1}-е вещественное число: "))
    numbers.append(num)

numbers.sort(reverse=True)  # Сортировка по убыванию

print("Список после упорядочивания по убыванию:")
print("numbers =", numbers)
