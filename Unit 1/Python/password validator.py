error = ""
run = True
errorcount = 0
numbers = False
while run is True:
    password = input("enter your password: ")
    lowercase = str.islower(password)
    symbols = str.isalnum(password)

    for character in password:
        if character.isdigit():
            numbers = True



    if len(password) > 20 or len(password) < 6:
        error = (error + "Between 6 and 20 characters,")
        errorcount = errorcount + 1

    if lowercase is True:
        errorcount = errorcount + 1
        error = (error + " At least one capital letter,")
    if symbols is True:
        errorcount = errorcount + 1
        error = (error + " At least one special character,")
    if numbers is False:
        errorcount = errorcount + 1
        error = (error + " At least one number")
    if errorcount > 1:
        print ("password must contain:" ,error,)
        error = ""
        errorcount = 0
    else:
        run = False
        print (password, "is a valid password")



