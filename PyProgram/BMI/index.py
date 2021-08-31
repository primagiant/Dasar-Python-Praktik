# BMI CALCULATOR
weight = int(input("Masukkan Berat Anda (kg) : "))
height = float(input("Masukkan Tinggi Anda (cm) : "))

# Height dari centimeter ke meter
height = height / 100

BMI = (weight / (height**2))

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 35:
    print("Overweight")
else:
    print("Obesity")

print("Your BMI is :", BMI)
