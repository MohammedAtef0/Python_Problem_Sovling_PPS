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
