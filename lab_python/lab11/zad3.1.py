# Ввод списка из 20 целых чисел
numbers = []
for i in range(20):
    num = int(input(f"Введите {i+1}-е целое число: "))
    numbers.append(num)

max_num = max(numbers)
max_index = numbers.index(max_num)

# Меняем местами наибольший элемент и первый элемент
numbers[0], numbers[max_index] = numbers[max_index], numbers[0]

print("Список после замены наибольшего элемента с первым:")
print("numbers =", numbers)
