word = ""
underscores = 0
for i in range(5):
    word = word + "#"
    print(word)
    word = ""
    underscores = underscores + 1
    for x in range(underscores):
        word = word + "_"




#teachers method

for i in range(5):
    line = ""
    for i in range(0,i):
        line = line + "_"
    line = line + "#"
    print(line)
