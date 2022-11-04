Grade = 0
while Grade >= 0 and Grade <= 100 :
    Grade = eval(input("Enter the Students Grades or enter -1 to exit the program:"))
    if (Grade >= 0 and Grade < 40) :
        print("The grade: F")
    elif Grade >= 40 and Grade < 60:
        print('The grade is: B')
    elif Grade >= 60 and Grade < 80:
        print('The grade is: B+')
    elif Grade >= 80 and Grade <= 100:
        print('The grade is: A')
else:
    print("Good Bye ._.")
