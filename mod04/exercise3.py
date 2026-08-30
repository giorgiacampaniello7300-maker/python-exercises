biological_gender = input("Enter the biological gender: ")
hemoglobin_value = float(input("Enter the hemoblobin_value (g/l): "))

if biological_gender == "female" and hemoglobin_value < 117:
    print("The hemoglobin value is low.")
elif biological_gender == "female" and 117 <= hemoglobin_value <= 155:
    print("The hemoglobin value is normal.")
elif biological_gender == "female" and hemoglobin_value > 155:
    print("The hemoglobin value is high.")

if biological_gender == "male" and hemoglobin_value < 134:
    print("The hemoglobin value is low.")
elif biological_gender == "male" and 134 <= hemoglobin_value <= 167:
    print("The hemoglobin value is normal.")
elif biological_gender == "male" and hemoglobin_value > 167:
    print("The hemoglobin value is high.")