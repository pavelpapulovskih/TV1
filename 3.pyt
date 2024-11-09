import math
# Всего деталей и количество окрашенных
total_parts = 15
colored_parts = 9
total_combinations = math.comb(total_parts, 3)
colored_combinations = math.comb(colored_parts, 3)
probability_all_colored = colored_combinations / total_combinations
print(f"Вероятность того, что все детали окрашены:{probability_all_colored:.5f}")
