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
