#names = []

#username = input("enter your name or type quit to exit").strip()
#while username.lower() != "quit":
#    if username.title not in names:
#        names.append(username.title()
#    else:
#        print("that name already exists")
#    username = input("enter your name or type quit to exit").strip()

#if len(names) > 0:
#    names.sort()

import random

balls = []
for i in range(6):
    n = random.randint(1, 45)
    while n in balls:
        n = random.randint(1, 45)
    balls.append(n)

balls.sort()
print(balls)