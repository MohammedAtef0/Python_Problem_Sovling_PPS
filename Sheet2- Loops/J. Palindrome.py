s = input("Enter a String:")
String_Count= 0 ; String_Rev = -1 ; c = 0
for i in range (len(s)):
    if s[String_Count] == s[String_Rev] :
        c+= 1
if c == len(s):
    print("Yes")
else:
    print("No")
