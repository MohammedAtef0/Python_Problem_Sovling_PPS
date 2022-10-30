a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a <= b and a <= c :
    min = a
elif b <= a and b <= c :
    min = b
elif c <= a and c <= b :
    min = c
#checking for the minumum value
if a >= b and a >= c:
    max = a
elif b >= a and b >= c :
    max = b
elif c >= a and c >= b:
    max = c
#checking for the maximux value
print(min,max)
#print ("The minimum number is:", min , " and the maximum is:", max)
#other method for printing the result
