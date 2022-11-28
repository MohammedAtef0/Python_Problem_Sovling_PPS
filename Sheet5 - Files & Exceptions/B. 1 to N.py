#At the first please create a file named Input and put it in the same directory in your project
try:
    Input = open('Input.txt', 'r')
    # opne the file
    x = int(Input.readline())
    # process on the file
    Input.close()
    # closing the file
    Output = open('Output.txt', 'w')
    # opening the file
    for i in range(x):
        print(i)
        Output.write(str(i) + '\n')
    Output.close()
    # closing the file
    print("The data has been written in the Output File", end='')
except:
    print("Error have been occured!")
