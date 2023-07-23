#5. Given a list of strings, find the longest string in the list.(The Problem)

#initializing an empty list of strings and a counter = 0 
ListOfStrings = []; 

#taking the values from the user or -1 to stop 
while True:
    x = input("Enter a word(or -1 to stop):")
    if x == "-1" :
        break 
    else:
        ListOfStrings.append(x)
   
#checking if the list is an empty list or not and print the longest string the list   
if len(ListOfStrings) == 0 :
    print("The list is empty!!")
else:
    print("The longest string in the list is:",max(ListOfStrings) , sep='')
