def NewArray( a=[] , b=[]):
    for i in b:
        print(i , end=" ")
    for i in a:
        print(i , end=" ")
#end of the NewArray function
n = int(input("Enter the number of test cases:"))
a = []; b= []
for i in range (n):
    x = input("Enter the Elements of the first List:")
    a.append(x)
#filling a List
for i in range (n):
    y = input("Enter the Elements of the second List:")
    b.append(y)
#filling b List
NewArray(a, b)
