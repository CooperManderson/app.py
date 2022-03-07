#run = True
#run2 = True
#final_temperature = 0
#while run is True:
#    while run2 is True:
#        try:
#            unit = str(input("would you like to convert to Celcius(C) or Fahrenheit(F), C or F? "))
#            if unit is C or unit is F:
#                run2 = False
#            else:
#                print("please type only CAPITAL c or f")
#        except ValueError:
#            print("please only type letters C or F")
#
#    if unit is F:
#        temperature = int(input("type a temperature in celcius: "))
#    elif unit is C:
#        temperature = int(input("type a temperature in fahrenheit: "))
#
#    if unit == C:
#        final_temperature = (temperature - 32) * 5/9
#
#    else:
#        final_temperature = (temperature * 9/5) + 32
#
#
#





run = True
while run is True:
    try:
        temperature = int(input("type a temperature in fahrenheit: "))
    except ValueError:
        print("only type numbers ")
    final_temperature = (temperature - 32) * 5/9
    print(" your final temperature is " ,final_temperature, "degrees celcius")
