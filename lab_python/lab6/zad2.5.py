n = 25
sum_numbers = 0
product_numbers = 1

for i in range(n):
    number = float(input(f"Введите число {i + 1}: "))
    sum_numbers += number
    product_numbers *= number

print("Сумма введенных чисел:", sum_numbers)
print("Произведение введенных чисел:", product_numbers)