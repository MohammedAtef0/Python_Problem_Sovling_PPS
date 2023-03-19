n = eval(input("Enter the number of values:"))
c = 0 ; hig = 0;
if (n != 0 ):
    for i in range (1, n+1):
        x = eval(input("Enter the values:"))
        if x >= hig:
            hig = x
            c = i
print("The highest value is:",hig)
print("The postion of the hights value is:", c)
--------------------------------------------------------------------------------------------------------------------------------------------------
#Other harder solution 
n = int(input("Enter how many times you want to loop"))
count = 1 ; pos = 0
num = eval(input("Enter values:"))
if n == 1 :
    pos = 1
else:
    for i in range(n - 1):
        nums = eval(input("Enter values:"))
        count += 1
        if nums >= num:
            num = nums
            pos = count
print(num , pos)
