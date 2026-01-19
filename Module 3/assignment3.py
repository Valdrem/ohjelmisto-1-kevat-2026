gender = input("Enter biological gender (male/female): ")
hemoglobing = int(input("Enter hemoglobin value (g/l): "))

if gender == "male":
    if hemoglobing >= 134 or hemoglobing >= 167:
        print("Your hemoglobin is normal.")
    elif hemoglobing >= 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")

if gender == "female":
    if hemoglobing >= 117 or hemoglobing >= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobing >= 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")