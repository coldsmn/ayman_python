# Введите непустую последовательность символов
print("Введите непустую последовательность символов:")
sequence = input()

# Построим множество из букв от 'A' до 'Z' и цифр от '0' до '5', встречающихся в последовательности
letters_digits_set = {char for char in sequence if char.isalnum() and (char.isalpha() and char.upper() <= 'Z') or (char.isdigit() and int(char) <= 5)}
print("Множество букв от 'A' до 'Z' и цифр от '0' до '5':", letters_digits_set)
