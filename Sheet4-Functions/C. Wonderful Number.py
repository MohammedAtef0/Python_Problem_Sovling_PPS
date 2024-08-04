def isOdd(n):
    if n % 2 != 0 :
        return True
    else:
        return False
#checking if the number is odd
def BinaryConverting(n):
    binary = []
    while n != 0:
        if n % 2 == 0 :
            n = n / 2
            binary.insert(0,0)
        else:
            n = (n-1) / 2
            binary.insert(0,1)
    rev_binary = binary[::-1]
    if binary == rev_binary:
        return True
    else:
        return False
#checking if the binary representation is palindrome
x = int(input("Enter a number to check if it's wonderful or not:"))
if isOdd(x) == True and BinaryConverting(x) == True:
    print("YES")
else:
    print("NO")
#end of the main method
#====================================================================================================================================================
# Other Solution 
# Checking if it is odd or not 
def isOdd(n):
    # Checking if it is odd or not 
    if n % 2 != 0 :
        return True
    else:
        return False
# Checking for the binary reprentation
def isPalindromeBinaryRep(n):
    s = bin(n)
    s2 = s[2::]
    if s2 == s2[::-1]:
        return True
    else:
        return False
n = int(input())
if isOdd(n) == True and isPalindromeBinaryRep(n) == True:
    print("YES")
else:
    print("NO")
    
