text = input("Введите английский текст: ")
words = text.split()
b_words = sum(1 for word in words if word.lower().startswith('b'))
print("Количество слов, начинающихся с 'b':", b_words)
