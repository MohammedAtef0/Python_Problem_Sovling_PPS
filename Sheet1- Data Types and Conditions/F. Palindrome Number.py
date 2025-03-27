# The Most Correct Code for the Palindrome Problem
InputString = input("Enter your string to check if it is a palindrome string or not:")
if InputString == InputString[::-1]:
    print("YES")
else:
    print("NO")
-------------------------------------------------------------------------------------------------------------
#1st solution
x = eval (input("Enter a number to check if it Palindrome Number or not:"))
if x % 11 == 0:
    print("YES")
else:
    print("NO")
-------------------------------------------------------------------------------------------------------------
#2nd solution
x =input("Enter a number to check if it Palindrome Number or not:")
if x[0] == x[-1]:
    print("YES")
else:
    print("NO")
-------------------------------------------------------------------------------------------------------------    
#3rd solution
x =eval(input("Enter a number to check if it Palindrome Number or not:"))
if (x // 10) == (x % 10) :
    print("YES")
else:
    print("NO")
