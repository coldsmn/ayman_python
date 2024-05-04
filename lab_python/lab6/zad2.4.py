k = 3
sum_four_digit_multiples = 0

for num in range(1000, 10000):
    if num % k == 0:
        sum_four_digit_multiples += num

print("Сумма всех 4-значных чисел, кратных", k, ":", sum_four_digit_multiples)
