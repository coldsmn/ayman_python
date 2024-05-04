# Ввод списка из 12 вещественных чисел
numbers = []
for i in range(12):
    num = float(input(f"Введите {i+1}-е вещественное число: "))
    numbers.append(num)

min_num = min(numbers)
min_index = numbers.index(min_num)

# Меняем местами наименьший элемент и первый элемент
numbers[0], numbers[min_index] = numbers[min_index], numbers[0]

print("Список после замены наименьшего элемента с первым:")
print("numbers =", numbers)
