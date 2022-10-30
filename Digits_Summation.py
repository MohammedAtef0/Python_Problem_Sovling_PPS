num1 = int (input ("Enter the first number:"))
num2 = int (input("Enter the second number:"))
print ("The sum of the last digits from the first number and the second number = ", (num1%10) + (num2%10))


#another solution
num1 = input("Enter the first number:")
num2 = input ("Enter the second number:")
sum = (int(num1[-1])%10) + (int (num2[-1])%10)
print ("The sum of the last digits from the first number and the second number =" , sum)
