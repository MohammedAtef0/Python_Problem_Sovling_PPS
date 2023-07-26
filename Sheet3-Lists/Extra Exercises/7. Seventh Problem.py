#Given a list of tuples, find the average of the second elements of all the tuples.(The problem itself)
#declaring a list of tuples 
l = [(1,2,3,4), (1,2,3), (1,2,3,4,5) ,  (1,4)]
#Initiliazing the Sum and count varialbes 
Sum = 0 ; count = 0 
#Make a nested loop to get the sum of the second elements in all the of the tuples 
for i in range(len(l)):
    for j in range(len(l)):
        if j == 1: 
            Sum += l[i][j] 
            count += 1 
#Printing out the the average 
print ("The average of the second elements of all the tuples is:", Sum / count)
    
