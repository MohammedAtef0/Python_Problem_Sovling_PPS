n = int(input("Enter a number n:"))
for i in range (n):
    x = eval(input("Enter a number x:"))
    if x <= 10 :
        print("A[" , i , "] = " , x , sep="")
        
-----------------------------------------------------------------------------------

#Other solution
n = int(input("Enter a number n:"))
a = []
for i in range (n):
    x = eval(input("Enter a number x:"))
    a.append(x)
    if a[i] <= 10 :
        print("A[" , i , "] = " , a[i] , sep="")
        
