def nTimes(n , ch = ''):
    for i in range (n):
        print(ch, " ", end="")
    print()
#end of the nTimes function
t = int(input("Enter the number of test cases:"))
for i in range (t):
    n = int(input("Enter the number to repeat the character:"))
    ch = input("Enter a character:")
    nTimes(n,ch)
# ============================================================================
# Other Solution 
def nTimes(value,times):
    for i in range(times):
        print(value, end= ' ')
    print()
NumberofItems = int(input())
for i in range(NumberofItems):
    t,v = map(str,input().split())
    t = int(t)
    nTimes(v,t)
# ============================================================================
