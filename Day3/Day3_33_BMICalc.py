print("Tip Calculator")

height_inch = input("What is your height in inches? ")
weight_lb = input("What is your weight in lb? ")

height_m = int(height_inch)/39.37
weight_lb = float(weight_lb)/2.205

bmi = weight_lb / (height_m*height_m)

print(f"BMI: {bmi}")

if bmi <= 18.5:
    print("You are under weight")
elif bmi <= 25:
    print("You are in a normal weight zone")
elif bmi <=30:
    print("You are slightly overweight")
elif bmi <=35:
    print("You are obese")
else: 
    print("You're clinically obese")
