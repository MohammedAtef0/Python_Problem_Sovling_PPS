Age = eval (input("Enter the age:"))
print(Age // 365 , "Year(s)")
print((Age%365) // 30 , "Month(es)")
print((Age%365) % 30 ,"Day(s)" , end="")
