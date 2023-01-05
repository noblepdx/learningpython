# BMI Calculator
# this is just an excercise, not to be taken as fat shaming. knowing bmi can be useful in weight loss.

print("Welcome to the super simple BMI Calculator. To measure your BMI, we are going to need to know a few things.")

height = float(input("Please enter your height in m: "))
weight = float(input("Now, please enter your weight in kg: "))

bmi = round(int(weight) / float(height) ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are semi-obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
