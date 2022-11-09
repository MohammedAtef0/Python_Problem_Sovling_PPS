n = eval(input("Enter a number n:"))
a = []
for i in range(n):
    x = eval(input("Enter the List elements:"))
    a.append(x)
a.sort()
for i in a:
    print(i , end=" ")
