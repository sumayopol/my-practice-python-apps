weight = 220
height = 1.85

bmi = float(weight / (height ** 2))

bmi = round(bmi,2)
print(f"Your latest BMI: {bmi})

# 🚨 Do not modify the values above
# Write your code below 👇


if bmi < 18.5:
    print(f"Your weight is: {bmi}. You are underweight")
elif 18.5 <= bmi < 25:
    print(f"Your weight is: {bmi}. Your weight is normal")
elif bmi >= 25:
    print(f"Your weight is: {bmi}. You are overweight")