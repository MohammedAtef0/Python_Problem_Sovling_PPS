a = []
t = int(input("Enter a number:"))
if t >= 1 :
    c = t
    for i in range (10):
        a.append(t - c )
        c = c - 1
        if c == 0 :
            c =  t
        print("N[" , i , "] = " , a[i] , sep="")
