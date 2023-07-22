#1. Find the second largest element in a list of integers(The problem)
#declaring an empty list 
l =[]

#taking the list values from the user 
while True:
    x = int(input("Enter a list value (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        l.append(x)
        
#sorting the list to find the second largest value in the list
l.sort()

#cheking if the list is empty or not!
if len(l) == 0:
    print("Please, enter values into the list, your list is empty!")
else:
    #printing the second largest element in the list 
    print(l[-2])
    

