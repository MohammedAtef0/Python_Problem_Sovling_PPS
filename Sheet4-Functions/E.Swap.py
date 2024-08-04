def Swap(x , y ):
    print(y , x , end=' ')
#end of the Swap function
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
Swap(a , b )
# ===============================================================
# Other Solution
def swap(x,y):
    return y,x 
a,b = map(int,input().split())
print(*swap(a,b))
===============================================================
