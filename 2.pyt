import math
# Количество кнопок и количество цифр в коде
buttons = 10
code_digits = 3
total_combinations = math.comb(buttons, code_digits)
probability_first_try = 1 / total_combinations
print(f"Вероятность угадать код с первой попытки:{probability_first_try:.5f}")
