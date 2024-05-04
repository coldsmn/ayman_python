words = input("Введите строку слов, разделенных пробелами: ").split()
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)
