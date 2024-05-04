# Ввод списка из 15 вещественных чисел
numbers = []
for i in range(15):
    num = float(input(f"Введите {i+1}-е вещественное число: "))
    numbers.append(num)

max_num = max(numbers)
max_index = numbers.index(max_num)

# Меняем местами наибольший элемент и последний элемент
numbers[-1], numbers[max_index] = numbers[max_index], numbers[-1]

print("Список после замены наибольшего элемента с последним:")
print("numbers =", numbers)
