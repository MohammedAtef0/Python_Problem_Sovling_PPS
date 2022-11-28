try:
    NewFile = open('Input.txt', 'r')
    # opening the file
    x = int(NewFile.readline())
    even = 0;
    odd = 0;
    pos = 0;
    neg = 0
    for i in NewFile:
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
        if int(i) >= 1:
            pos += 1
        elif int(i) < 0:
            neg += 1
    # the porcess on the file
    NewFile.close()
    # closing file
    print("Even: ", even, "\nodd: ", odd, "\nPositive: ", pos, "\nNegative: ", neg, sep="")
    # printing the output on the console
    WriteIntoFile = open('Output.txt', 'w')
    # open the file
    WriteIntoFile.write(
        "Even: " + str(even) + "\nodd: " + str(odd) + "\nPositive: " + str(pos) + "\nNegative: " + str(neg))
    # process on file
    WriteIntoFile.close()
    # closing file
except:
    print("Error!")
    print("Try again")
