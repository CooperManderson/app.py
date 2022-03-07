#ask the user for the number of rolls, 2 dice -> 10

#number of rolls >7
#craps= 7
#number of rolls <7

import random

rolls = int(input("how many times should the dice roll? "))
under = 0
craps = 0
over = 0



for x in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    dicetotal = dice1 + dice2
    if dicetotal > 7:
        over = over + 1
    elif dicetotal < 7:
        under = under + 1
    elif dicetotal == 7:
        craps = craps + 1

print("you got " ,under, " below 7, " ,over, " above 7 and " ,craps, " craps")
