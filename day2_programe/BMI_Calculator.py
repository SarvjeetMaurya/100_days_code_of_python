print("This the Body Mass Index(BMI) Calculator....")
Height= float(input("Enter your Height in M \n"))
Weight= float(input("Enter your Weight in KG \n"))
bmi = int(Weight/ (Height*Height))
if bmi<18.8:
    print(f"your BMI  is {bmi},you are underweight.")
elif bmi<25:
    print(f"your BMI is {bmi},you are normal.")
elif bmi<30:
    print(f"your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")