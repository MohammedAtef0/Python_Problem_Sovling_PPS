n = eval(input("Enter a number:"))
a = []
a.append(n)
print("N[" , 0 , "] = " , a[0] , sep="")
for i in range (1,10):
    x = a[i-1] * 2
    a.append(x)
    print("N[" , i , "] = " , a[i] , sep="")
