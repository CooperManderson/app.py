run = True
while run is True:
    try:
        weight = float(input("type your weight in kg: "))
        height = float(input("type your height in metres: "))
        run = False
    except ValueError:
        print("only type numbers ")
BMI = (weight) / (height * height)
if BMI >= 18.5 and BMI <= 24.9:
    print(BMI, "your BMI is within the healthy range!")
elif BMI > 24.9:
    print("your BMI is above the healthy range")
elif BMI < 18.5:
    print("your BMI is below the healthy range")
