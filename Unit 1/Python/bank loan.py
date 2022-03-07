income = 0
workyears = 0
loop = True
loan = False
while loop is True:
    try:
        income = int(input("how much money do you make a year? "))

    except ValueError:
        print("only use numbers please ")

    try:
        workyears = int(input("how many years have you worked at your job? "))
        loop = False
    except ValueError:
        print("only use numbers please ")



if workyears >= 2 and income >= 40000:
    loan = True
if workyears >= 5:
    loan = True

if loan is True:
    print("you are eligible for a loan")
else:
    print("you are ineligible for a loan")