def cast(number):
    finalnumber = 0
    for i in number:
        finalnumber = finalnumber + i
        if finalnumber >= 9:
            finalnumber = finalnumber - 9
    return finalnumber






filename = casting9s.txt
contents = open(filename)