gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender.lower() == "male":
    if hemoglobin >= 134 and hemoglobin <= 167:
        print("Your hemoglobin is normal.")
    elif hemoglobin > 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")

if gender.lower() == "female":
    if hemoglobin >= 117 and hemoglobin <= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobin > 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")

if gender.lower() != "male" and gender.lower() != "female":
    print("Invalid gender.")