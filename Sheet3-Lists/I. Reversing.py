#Solution0
n = eval(input("Enter a number n:"))
a=[]
for i in range(n):
    x = eval(input("Enter the List elements:"))
    a.append(x)
a.reverse()
for i in a:
    print(i , end=" ")
    
----------------------------------------------------------------------------------------------------

#Other solution1
n = eval(input("Enter a number n:"))
a=[]
for i in range(n):
    x = eval(input("Enter the List elements:"))
    a.append(x)
print(a[::-1] ,end=" ")

--------------------------------------------------------------------------------------------------
#Other solution2
n = eval(input("Enter a number n:"))
a=[]
for i in range(n):
    x = eval(input("Enter the List elements:"))
    a.append(x)
for i in range(n , 0 , -1):
    print(i , end=" ")


