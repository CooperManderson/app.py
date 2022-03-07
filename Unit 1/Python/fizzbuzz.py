#for every number between 1 and 100 inclusive. either print the number or if its  multiple of three, print the word fizz, if its a multiple of 5 print buzz, if its a multiple of 3 and 5, print fizzbuzz
fizzbuzz = ""
for i in range(1, 101):
    if i % 3 == 0:
        fizzbuzz = fizzbuzz + "fizz"

    elif i % 5 == 0:
        fizzbuzz = fizzbuzz + "buzz"

    elif fizzbuzz == "":
        print(i)
    print(fizzbuzz)
    fizzbuzz = ""




#for i in range(1,101):
#    print(i)

