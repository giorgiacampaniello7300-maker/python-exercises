import random

combination_1_number_1 = random.randint(0, 9)
combination_1_number_2 = random.randint(0, 9)
combination_1_number_3 = random.randint(0, 9)

combination_2_number_1 = random.randint(1, 6)
combination_2_number_2 = random.randint(1, 6)
combination_2_number_3 = random.randint(1, 6)
combination_2_number_4 = random.randint(1, 6)

print(f"3-digit code: {combination_1_number_1}{combination_1_number_2}{combination_1_number_3}")
print(f"4-digit code: {combination_2_number_1}{combination_2_number_2}{combination_2_number_3}{combination_2_number_4}")