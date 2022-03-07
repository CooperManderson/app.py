fails = 0
username = "cooper"
password = "cooper"

while fails < 3:
    inputusername = input("input your username: ")
    inputpassword = input("input your password: ")
    if inputpassword != password or inputusername  != username:
        fails = fails + 1
        if fails >= 3:
            print("your account is now locked out for 60 minutes")
        else:
            print("either your username or password is incorrect")
    else:
        print("welcome back")
