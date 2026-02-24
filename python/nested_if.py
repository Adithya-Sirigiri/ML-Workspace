weight=input("Please enter your weight in kg:")
height=input("Please enter the height in meters:")
BMI=int(weight)//(float(height)*float(height))

if(BMI<18.5):
    print("You are underweight")
elif(BMI<24.9):
    print("You are in normal weight category")
elif(BMI<29.9):
    print("You are overweight")
elif(BMI<34.9):
    print("Obese Class 1")
elif(BMI<39.9):
    print("Obese Class 2")
else:
    print("You will DIE for sure")