x = eval(input("Enter a number:"))
print("The list of the 6 consecutive odd numbers is:")
for i in range (x , x + 12 , 2):
    if i % 2 == 0:
        print(i + 1 )
    else:
        print(i)
