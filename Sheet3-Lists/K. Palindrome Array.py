n = int(input("Enter a numbre n:"))
a = []
for i in range(n):
    x = eval(input('Enter a list elements:'))
    a.append(x)
if a == a[::-1] :
    print("YES")
else:
    print("NO")
