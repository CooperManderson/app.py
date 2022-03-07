run = True
total = 0
while run is True:
    try:
        startnumber = int(input("please enter some numbers to add up: "))
        run = False
    except ValueError:
        print("use only numbers please: ")
number = str(startnumber)
for value in number:
    total = total + int(value)
print(total)

