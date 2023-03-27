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
----------------------------------------------------------------------------------
#other solution2
n = int(input("Enter N:"))
a,b,c = list(map(int,input("Enter list item's:").split()))
print(abs(sum(a)))
----------------------------------------------------------------------------------
#other solution3
#Taking from the user N
n = int(input("Enter N:"))
#initilaze empty list
a=[];Sum=0
#taking from the user list items
for i in range(n):
    x = int(input("Enter list item's:"))
    a.append(x)
    Sum += x
if Sum > 0 :
    print(Sum)
else:
    print(Sum * -1)
