#age test

#age = int(input("enter your age? "))

#if age >= 18:
    #print("you can buy alcohol")
#else:
    #print("you cant buy alcohol legally")


#vowel test

#vowels = 'aeiouAEIOU'
#word = input('please enter a word: ')
#last_letter = word[-1]
#if last_letter in vowels:
    #print("your word ends in a vowel")
#else:
    #print("your word ends in a consonant")



#grade test
checkerror = False
while checkerror is False:
    try:
        grade = int(input("what was your score? "))
        if grade <= 100:
            checkerror = True
        else:
            print("enter a grade 100 or lower ")


    except ValueError:
        print("please use only numbers ")
#alternate way to check for numbers
#grade = (input("what was your score? ")).strip()
#if mark.isdigit():
    #mark = int(mark)
    #if mark > 100:
        #print("thats not a valid grade")


if grade >= 50:
    if grade >= 70 and grade <= 79:
        print("you got a B!")
    elif grade >= 50 and grade <= 69:
        print("you got a C")
    else:
        print("you got an A!")
elif grade >= 30 and grade <= 49:
    print("you got a D")
else:
    print("you got an E")
