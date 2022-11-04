n = eval (input("Enter a number:"))
c = 0
for i in range (1 , n+1):
    if i % 2 == 0:
        print(i)
        c += 1 #This is the same when we say c = c + 1
if  c == 0 :
    print(-1 , end="")
else:
    print("The count of the even numbers is:", c , end="")
