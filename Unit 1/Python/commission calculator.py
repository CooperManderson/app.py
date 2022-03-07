run = True
while run is True:
    try:
        sales = int(input("How much money in sales did you make? "))
        run = False
    except ValueError:
        print("use only numbers please and no decimals: ")

if sales >= 20000:
    commission = 0.1
else:
    commission = 0.05

money = (sales * commission)
print("You made $" ,money, ",well done!")
