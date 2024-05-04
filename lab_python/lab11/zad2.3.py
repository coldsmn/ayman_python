# Создаем последовательность из 16 элементов
sequence = [3, 5, 7, 9, 2, 4, 6, 8, 1, 3, 5, 7, 9, 2, 4, 6]

even_indices_values = [sequence[i] for i in range(len(sequence)) if i % 2 == 0]

print("Исходная последовательность:", sequence)
print("Список значений под четными номерами:", even_indices_values)
