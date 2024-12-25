def ShiftZero(n,a):
    for i in a:
        if i == 0:
            a.remove(i)
            a.append(0)
    return a
n = int(input())
a = list(map(int,input().split()))
print(*ShiftZero(n,a))
