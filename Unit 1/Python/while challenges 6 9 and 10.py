#run = True
#end = "quit"
#while run is True:
#    name = str(input("whats your name? type QUIT to exit "))
#    if str.isupper(name) and name == "QUIT":
#        run = False
#    print(name)



#number = int(input("what number should i calculate the factorial of? "))
#factorial = 1
#for i in range(1,number):
#    factorial = factorial * i
#print(factorial)



#run = True
#N = int(input("please enter a number "))
#while run is True:
#    if N % 2 == 0:
#        N = N/2
#    elif N == 1:
#        run = False
#    else:
#        N = N * 3 + 1
#    print(N)



population = 26000000
years = 0

while population < 50000000:
    
    population = population * 1.03
    years = years + 1
print (years)
