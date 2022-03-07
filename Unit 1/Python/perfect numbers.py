#ask for a number from the user and find all numbers up to it whos factors count up to its value
loop = True
perfectnumber = 0
while loop is True:
    try:
        endvalue = int(input("what value should i calculate up to? "))
        loop = False
    except ValueError:
        print("please only use numbers")

for i in range(1,endvalue):
    perfectnumber = 0
    for x in range(1,i):
        if i % x == 0:
            perfectnumber = perfectnumber + x
    if perfectnumber == i:
        print(i)
