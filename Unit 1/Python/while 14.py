import random
turns = 0
pot = int(input("how much money would you like to bet? "))
highest = 0

while pot > 0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicetotal = dice1 + dice2
    if dicetotal == 7:
        pot = pot + 4
    else:
        pot = pot - 1
    if pot > highest:
        highest = pot
    turns = turns + 1
print("it took" ,turns, "turns to lose all the money")
print("and the highest amount in the pot was" ,highest,"$")
