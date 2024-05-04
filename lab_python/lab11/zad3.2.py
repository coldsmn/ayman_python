# Ввод списка из 10 целых чисел
numbers = []
for i in range(10):
    num = int(input(f"Введите {i+1}-е целое число: "))
    numbers.append(num)

min_num = min(numbers)
min_index = numbers.index(min_num)

# Меняем местами наименьший элемент и последний элемент
numbers[-1], numbers[min_index] = numbers[min_index], numbers[-1]

print("Список после замены наименьшего элемента с последним:")
print("numbers =", numbers)
