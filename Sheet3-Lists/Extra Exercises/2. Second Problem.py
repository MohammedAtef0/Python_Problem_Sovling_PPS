#first solution
#2. Find the nth largest element in a list of integers (the problem)
l = []; MaxValueInTheList = 0
while True:
    x = int(input("Enter the list values (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        l.append(x)
for i in range(len(l)):
    if  l[i] >= MaxValueInTheList:
        MaxValueInTheList = l[i]
if len(l) == 0:
    print("The list is empty please add values to the list!")
else:
    print("The largest element in the list is:",MaxValueInTheList)
------------------------------------------------------------------------------------------------
#second solution
#2. Find the nth largest element in a list of integers (the problem)
l = []
while True:
    x = int(input("Enter the list values (or -1 to stop):"))
    if x == -1 :
        break 
    else:
        l.append(x)
l.sort()
if len(l) == 0:
    print("The list is empty please add values to the list!")
else:
    print("The largest element in the list is:",l[-1])
