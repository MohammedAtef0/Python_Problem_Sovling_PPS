a = []
for i in range (15):
    x = int(input("Enter a list element:"))
    a.append(x)
    if a[i] <= 10 :
        print("A[" , i , "] = " , a[i] , sep="")
