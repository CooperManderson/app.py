number = 0
numbersequence = ""
for i in range(1,6):
    number = i
    numbersequence = ""

    for x in range(i):
        numbersequence = numbersequence + str(i + x)
    print(numbersequence)
