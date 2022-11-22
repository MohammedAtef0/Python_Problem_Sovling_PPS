def Min(n , a=[] ):
    x = a[0]
    for i in range (n) :
        if a[i] < x :
            x = a[i]
    return x
#end of the Min function
def Max(n , a=[]):
    x = a[0]
    for i in range (n):
        if a[i] > x :
            x = a[i]
    return x
#end of the Max function
n = int(input())
a = []
for i in range (n):
    x = int(input())
    a.append(x)
print(Min(n, a ) , " " , Max(n , a ) , sep="")
