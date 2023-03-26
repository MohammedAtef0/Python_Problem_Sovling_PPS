n = eval(input("Etner a number n:"))
a = []; c= 0
for i in range (n):
    x = eval(input("Etner the list elements:"))
    a.append(x)
Search_number = eval(input("Enter a number to search of it's position in the list:"))
for i in range (n):
    if a[i] == Search_number:
        print(i)
        break
    else:
        c = c + 1
if c == n:
    print(-1)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Other solution 1
x = int(input("Enter a N:"))
a= []
for i in range(x):
    Lvalues = int(input("Enter list items:"))
    a.append(Lvalues)
y = int(input("Enter a number to search in the list:"))
if y in a :
    print(a.index(y))
else:
    print(-1)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Other solution 2
x = int(input("Enter a N:"))
a = list(map(int, input("Enter the list values:").split()))
y = int(input("Enter a number to search in the list:"))
if y in a :
    print(a.index(y))
else:
    print(-1)
