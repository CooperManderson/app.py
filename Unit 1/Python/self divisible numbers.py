number1 = int(input("what number would you like the range to start from? "))
number2 = int(input("what number would you like the range to end at? "))
validnumbers = ""
totalnumbers = 0
for i in range(number1, (number2 + 1)):
    y = ("")
    for x in str(i):
        y = (y) + x
        if int(x) == 0:
            selfdivisible = False
        elif int(y) % int(x) == 0:
            selfdivisible = True
        else:
            selfdivisible = False
    if selfdivisible is True:
        validnumbers = (validnumbers + str(i) + ", ")
        totalnumbers = totalnumbers + 1
print(" the self divisible numbers are: " ,validnumbers)
print("there were" ,totalnumbers, "divisible numbers")


