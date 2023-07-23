#3. Given a list of integers, find the first number that is divisible by 3

#Declaring an empty list and a initializing a divisibleByThree variable
l = []; divisibleByThree = 0;

#Taking from the user the list values and if -1 stop accepting values 
while True:
    x = int(input("Enter the list values (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        l.append(x)

#chekcing for all the list values which is the first value is divisible by 3
for i in l:
    if i % 3 == 0:
        divisibleByThree = i
        break 

#Checking if the list is empty or not to display a warning message to the user
if len(l) == 0:
    print("The list is empty please add values to the list!")
else:
    print("The first divisible by 3 number in the list is:",divisibleByThree)
