def nTimes(n , ch = ''):
    for i in range (n):
        print(ch, " ", end="")
    print()
#end of the nTimes function
t = int(input("Enter the number of test cases:"))
for i in range (t):
    n = int(input("Enter the number to repeat the character:"))
    ch = input("Enter a character:")
    nTimes(n,ch)
