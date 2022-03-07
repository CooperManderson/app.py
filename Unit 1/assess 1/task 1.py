values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
romannumerals = ""
number = int(input("please input a number between 0 and 3999: "))
if number < 3999:
    for i in range(0, 13):
        while number >= values[i]:
            romannumerals += (roman[i])
            number = number-values[i]
print(romannumerals)
