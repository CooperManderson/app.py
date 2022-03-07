run = True
filename = "task2"
contents = open(filename)
for y in contents:
    word1, word2 = y.split(" ")
    list1 = []
    list2 = []

    variable1 = 0
    for i in word1:
        variable1 = variable1 + 1
        run = True
        for x in range(variable1, len(word1)):
            if run is True:
                if word1[x] == i:
                    list1.append("+{}".format(x-variable1+1))
                    run = False
        if run == True:
            list1.append(0)
    variable1 = 0
    for i in word2:
        variable1 = variable1 + 1
        run = True

        for x in range(variable1, len(word2)):
            if run is True:
                if word2[x] == i:
                    list2.append("+{}".format(x-variable1+1))
                    run = False
        if run == True:
            list2.append(0)
    list2.pop()
    if len(list1) == len(list2):
        if list1 == list2:
            finallist1 = str(list1)
            finallist1 = finallist1.replace("'", "")
            finallist1 = finallist1.replace(",", "")
            finallist1 = finallist1.replace("[", "")
            finallist1 = finallist1.replace("]", "")
            print(word1, word2, "are isomorphs with repetition pattern", finallist1)
        else:
            print(word1, word2, "are not isomorphs")
    else:
        print(word1, "and", word2, "are not the same length")



