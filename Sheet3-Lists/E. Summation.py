n = eval(input("Enter a number n:"))
Sum = 0
for i in range (n) :
    x = eval(input("Enter a number x:"))
    Sum+= x
print("The absolutes summation = " , abs(Sum) , sep="")

----------------------------------------------------------------------------------

#other solution
n = eval(input("Enter a number n:"))
a = []
for i in range (n):
    x = eval(input("Enter the array values:"))
    a.append(x)
print("The absolutes summation = " , abs(sum(a)) , sep="")
