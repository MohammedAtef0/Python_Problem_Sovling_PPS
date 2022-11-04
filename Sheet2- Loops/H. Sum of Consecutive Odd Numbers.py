n = eval (input("Enter the number of values:"))
for i in range (n):
    x = eval(input("Enter the value X:"))
    y = eval(input("Enter the value Y:"))
    Sum = 0
    if x < y :
        for j in range (x+1 , y  , 1):
            if j % 2 != 0 :
                Sum += j
    elif x > y :
        for c in range (x - 1 , y, -1):
            if c % 2 != 0 :
                Sum +=  c
    else:
        Sum = 0
    print("The sum of odd numbers = ", Sum)


