User = input('\nPlease enter your name: ')
weight_KG = float(input('Please enter weight in kilogram: '))
height_Meter = float(input('Please enter height in metre: '))

#BMI Formula
BMI = (weight_KG / (height_Meter ** 2)); #take 2 decimal points

print("\nName: ", User);
print("Weight: ", weight_KG ,"KG")
print("Height: ", height_Meter , "M")

#Body Mass Index Interpretation
if(BMI < 18.5):
    print("BMI: ", BMI ,"\nBelow Normal Weight")
elif (BMI >= 18.5 and BMI < 25):
    print("BMI: ", BMI , "\nNormal Weight")
elif (BMI >= 25 and BMI < 30):
    print("BMI: ", BMI , "Overweight")
elif (BMI >= 30 and BMI < 35):
    print("BMI: ", BMI , "\nClass I Obesity")
elif (BMI >= 35 and BMI < 40):
    print("BMI: ", BMI , "\nClass II Obesity")
elif (BMI >= 40):
    print("BMI: ", BMI , "\nClass III Obesity")
else:
    print("Error Can't Calculate your BMI")

