###--->Creating a BMI Caclulator

weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))

BMI= (weight/(height)**2)

if BMI<18.5:
    print("Under Weight")
elif BMI >=18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Over Weight")
else:
    print("Obesity")