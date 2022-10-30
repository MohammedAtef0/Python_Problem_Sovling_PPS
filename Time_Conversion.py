N = int (input("Please enter the number of seconds:"))
Hours = (N // 3600)
Minutes = (N % 3600) // 60
Seconds = N % 60
print (Hours,":",Minutes,":",Seconds)

#Other solution
N = int (input("Please enter the number of seconds:"))
print (N // 3600,":",(N%3600)//60,":",N%60)
