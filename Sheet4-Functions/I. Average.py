def avg(n , a=[]):
    Sum = 0
    for i in a:
        Sum += i
    return Sum / n
#end of the avg function
n = int (input())
a = []
for i in range (n):
    x = eval(input())
    a.append(x)
print(format(avg(n,a), '.7f'))
# =============================================================================================================================
# Avg Func.
def Avg(n,a):
    Sum = 0 
    for i in a:
        Sum += i
    return Sum / n 
# Input
n = int(input())
a = list(map(float,input().split()))
# Print with the 7th decimal point
print(format(Avg(n,a), '.7f'))
