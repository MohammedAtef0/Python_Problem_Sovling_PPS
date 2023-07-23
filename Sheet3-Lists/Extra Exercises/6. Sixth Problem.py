from math import *
#6. Write a program that takes in a list of numbers and finds the largest prime number in the list.(The problem)

#initializing an empty list 
ListOfNumbers = [] ; ListOfPrimeNumbers =[]; IsPrime= False

#taking from the user the ListOfNumber values 
while True:
    x = int(input("Enter the list values (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        ListOfNumbers.append(x)

#checking for all prime numbers in the ListOfNumbers and append all prime numbers in a new list named ListOfPrimeNumbers
for i in ListOfNumbers:
    if i <= 1:
        continue
    for j in range(2 , int(sqrt(i) )+1):
        if i % j == 0 :
            break  
    else:
        ListOfPrimeNumbers.append(i)

#sorting the ListOfPrimeNumbers to get the last value in the list because it's the largest ListOfPrimeNumbers
ListOfPrimeNumbers.sort()

#checking if the list is empty or not!
if len(ListOfNumbers) == 0 or len(ListOfPrimeNumbers) == 0:
    print("The list is empty please try again!")
else:
    print("The largest prime number in list is:" , ListOfPrimeNumbers[-1])

        
