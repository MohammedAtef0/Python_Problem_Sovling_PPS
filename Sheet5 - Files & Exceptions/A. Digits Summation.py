#At the first please create a file named Input and put it in the same directory in your project
try :
    Input = open('InputFile.txt' , 'r')
    # opne the file
    x = int(Input.readline())
    y = int(Input.readline())
    # process on the file
    Input.close()
    # closing the file
    print(x % 10 + y % 10)
    Output = open('OutputFile.txt' , 'w')
    #opening the file
    Output.write(str(x%10 + y % 10) + '\n')
    #writing the output in a new file
    Output.close()
    #closing the file
    print("The data has been written in the OutputFile", end='')
except:
    print('An error occured!' , end="")
