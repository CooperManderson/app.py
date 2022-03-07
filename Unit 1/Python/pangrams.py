filename = open('pangrams')
file = filename.readlines()
file.pop(0)
print(file)

for x in file:
    x = x.strip('\n')
    Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in x:
        if i.isalpha():
            if i.upper() in Alphabet:
                Alphabet.remove(i.upper())
    print(x)
    if len(Alphabet) == 0:
        print("pangram")
    else:
        print("not pangram, missing:" , ''.join(Alphabet))