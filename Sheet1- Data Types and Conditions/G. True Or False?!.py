A = int (input("Enter the number A:"))
B = int (input("Enter the number B:"))
C = int (input("Enter the number C:"))
D = int (input("Enter the number D:"))
if (B > C ) and (D > A) and ((C + D ) > (A + B )) and (C >= 0) and (D >= 0) and (A % 2 ==0):
    print("Accepted")
else:
    print("Error!")
