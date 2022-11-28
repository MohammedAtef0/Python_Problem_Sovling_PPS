#At the first please create a file named Input and put it in the same directory in your project
try:
    Input = open('Input.txt', 'r')
    # opne the file
    x = int(Input.readline())
    # process on the file
    Input.close()
    # closing the file
    c = 0
    Output = open('Output.txt', 'w')
    # opening the file
    for i in range(1, x + 1):
        if i % 2 == 0:
            print(i)
            c += 1
            Output.write(str(i) + '\n')
    print("The count of the even number is:", c)
    Output.write('The count of the even number is: ' + str(c) + '\n')
    print("The data have been written in the output file ")
    Output.close()
    # closing the file
except:
    print("An error have been occurred!")
