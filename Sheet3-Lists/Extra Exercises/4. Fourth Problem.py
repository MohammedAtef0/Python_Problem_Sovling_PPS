#4. Given a list of strings, count the number of strings that are longer than 5 characters(the problem)

#initializing an empty list of strings and a counter = 0 
ListOfStrings = []; Counter = 0

#taking the values from the user or -1 to stop 
while True:
    x = input("Enter a word(or -1 to stop):")
    if x == "-1" :
        break 
    else:
        ListOfStrings.append(x)
        
#Checking for the characters of each value in the list 
for i in range(len(ListOfStrings)):
    if len(ListOfStrings[i]) > 5:
        Counter += 1 
   
#checking if the list is an empty list or not      
if len(ListOfStrings) == 0 :
    print("The list is empty!!")
else:
    print("There are ", Counter , " Strings that are longer than 5 characters" , sep='')
