#8. Write a program that takes in a list of integers and removes all duplicates, then prints the resulting list. (Hint: Use Sets)(The problem itself)
#Initilazing an empty list l 
l = []
#taking from the user the inputs or -1 to stop 
while True:
    x = int(input('Enter a number (or -1 to stop):'))
    if x == -1 :
        break 
    else:
        l.append(x)
#Declaring a set S and put in it the list after taking the integers from the user 
S = set(l)
#printing the set S and it automaticly will delete the duplicated numbers
print(S)
    
