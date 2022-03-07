#import pygame

variable1 = 0
run = True
Variable2 = 0
list1 = []
list2 = []
Check = True
filename = "task2"
contents = open(filename)
for y in contents:
    word1, word2 = y.split(" ")
    word1.strip()
    word2.strip()
    Check = True
    Variable2 = 0
    for i in word1:
        variable1 = variable1 + 1
        run = True

        for x in range(variable1, len(word1)):
            #print(word1[x])
            if run is True:
                if word1[x] == i:
                    list1.append("+{}".format(x-variable1+1))
                    #print("yes")
                    run = False
        if run == True:
            list1.append("+{}".format(0))
    variable1 = 0
    Variable2 = 0
    Check = True
    for i in word2:
        variable1 = variable1 + 1
        run = True

        for x in range(variable1, len(word2)):
            #print(word2[x])
            if run is True:
                if word2[x] == i:
                    list2.append("+{}".format(x-variable1+1))
                    #print("yes")
                    run = False
        if run == True:
            list2.append("+{}".format(0))
    variable1 = 0
    list2.pop()
    if len(list1) == len(list2):
        #print(list1, list2)
        #for o in range(0, len(list1)-1):
            #if Check == True:
        if list1 == list2:
                    #Variable2 += 1
            print("isomorphs", list1, list2)

        else:
            print("not isomorphs")
                    #Check = False
                #if Variable2 == len(list1):
                    #print("isomorphs", list1, list2)
    else:
        print(word1, "and", word2, "not the same length")

    list1 = []
    list2 = []


