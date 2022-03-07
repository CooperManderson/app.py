run = True
while run is True:
    try:
        weight = int(input("type a weight in pounds: "))
    except ValueError:
        print("only type numbers ")
    final_weight = (weight / 2.205)
    print(" your final weight is " ,final_weight, "kg")