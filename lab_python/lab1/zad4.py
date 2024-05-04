import random

random_number = random.randint(100, 999)
digits = [int(digit) for digit in str(random_number)]
print(*digits, sep=", ")
