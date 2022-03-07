run = True
while run is True:
    try:
        weight = int(input("type a weight in kg: "))
    except ValueError:
        print("only type numbers ")
    final_weight = (weight / 100 ) * 16.5
    print(" your final weight on the moon is" ,final_weight, "kg")