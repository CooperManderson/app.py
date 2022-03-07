totalhappynumbers = 0
totalunhappynumbers = ""
longeststeps = 0
smallest3digit = 1000
circleofdespair = [2, 4, 16, 37, 58, 89, 145, 42, 20]
circleofdespairloops = 0
largestunhappydigit = 0
for i in range(0, 999):
    total = i
    loops = 0
    number = 0

    while total != 1 and loops < 500 and total not in circleofdespair:
        loops = loops + 1

        for x in str(total):
            number = number + (int(x) * int(x))
        total = number
        number = 0
    if total != 1:
        totalunhappynumbers = totalunhappynumbers + "," + str(i)
    if total == 1:
        print("happy number" ,i)
        totalhappynumbers = totalhappynumbers + 1
        if len(str(i)) == 3:
            if loops > longeststeps:
                longeststeps = loops
            if i < smallest3digit:
                smallest3digit = i
    if totalhappynumbers == 10:
        tenthhappynumber = i
    if total in circleofdespair:
        if len(str(i)) == 3:
            if total > circleofdespairloops:
                circleofdespairloops = loops
            if i > largestunhappydigit:
                largestunhappydigit = i


print("these are the circle of despair numbers" ,totalunhappynumbers)
print("the tenth happy number was" ,tenthhappynumber)
print("the longest steps for a 3 digit number was" ,longeststeps)
print("the smallest three digit happy number was" ,smallest3digit)
print("the maximum loops to enter the circle of despair was" ,circleofdespairloops, "for" ,i)
print("the largest 3 digit unhappy number was" ,largestunhappydigit)