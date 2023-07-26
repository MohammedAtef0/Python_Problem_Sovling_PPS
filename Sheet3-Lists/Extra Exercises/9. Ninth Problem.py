#Write a program that takes in two lists of integers and returns a set containing only the elements that appear in both lists. (Hint: Use Sets)(The problem)
#Iniliazing two empty lists 
l1 = []
l2 = []
#taking the numbers from the user in the first list 
while True:
    x = int(input("Enter a number in the first list (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        l1.append(x)

#taking the number from the user in the second list 
while True:
    y = int(input("Enter a number in the second list (or -1 to stop):"))
    if y == -1:
        break 
    else:
        l2.append(y)
#displaying out each list with it's elements
print("Elements in the first list are:" , l1)
print("Elements in the second list are:" , l2)
#making the sets from l1 and l2 
s1 = set(l1)
s2 = set(l2)
#printing out the intersection between the first list and the second list
print("The elements that appear in both lists are:" , s1.intersection(s2))
