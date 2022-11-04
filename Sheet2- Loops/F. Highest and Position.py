n = eval(input("Enter the number of values:"))
c = 0 ; hig = 0;
if (n != 0 ):
    for i in range (1, n+1):
        x = eval(input("Enter the values:"))
        if x >= hig:
            hig = x
            c = i
print("The highest value is:",hig)
print("The postion of the hights value is:", c)
