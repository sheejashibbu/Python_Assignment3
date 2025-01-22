weight= float(input("Enter the weight in kg:"))
Height=float(input("Enter the height in M:"))
BMI=weight/(Height*Height)
print("BMI",BMI)
if BMI<18.5:
    print("Underweight")
elif BMI > 18.5 and BMI <= 24.9:
    print("normal")
elif BMI > 24.9 and BMI <= 30:
    print("Over weight")
else:
    print("obesity")