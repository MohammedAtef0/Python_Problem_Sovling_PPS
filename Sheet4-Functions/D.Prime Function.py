from math import sqrt
def isPrime(n):
    if n<= 1:
        return False
    for i in range (2,int(sqrt(n)+1)):
        if n % i == 0 :
            return False
    return True
#end of the isPrime Function
x = int(input())
for i in range (x):
    NumberToCheck = int(input())
    if isPrime(NumberToCheck) :
        print("YES" )
    else:
        print("NO" )
