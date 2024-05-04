text = input("Введите строку: ")
unique_chars = ''.join(set(text.replace(' ', '')))
print("Строка без повторяющихся символов и пробелов:", unique_chars)