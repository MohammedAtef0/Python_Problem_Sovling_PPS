a=[]
for i in range (10):
    x = int(input("Enter the elements of the list:"))
    if x <= 0 :
        a.append(1)
    else:
        a.append(x)
    print(end="")
    print("x[", i , "] = " , a[i] , sep="")
