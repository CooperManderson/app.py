msg = input("what is your coded message? ")
A = ord(msg[0]) - 64
columns = A % 3 + 3
msglength = len(msg)
y = -1
message = ""
if msglength % columns != 0:
    rows = int(msglength/columns + 1)
else:
    rows = int(msglength/columns)
#for i in range(0, columns):
 #   for x in range(0, msglength):
  #      if msg[i * columns + 1].isalpha():
   #         message = message + msg[i * columns + 1]
    #    else:
     #       message = message + " "
      #  print(message)











for a in range(0, rows):
    x = -1
    y = y + 1
    message = ""
    for i in msg:
        x = x + 1
        if (x+y) % columns == 0:
            if i.isalpha():
                message = message + i
            else:
                message = message + " "
    print(message)