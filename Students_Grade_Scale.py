Grade = int (input ("Please Enter the student grade:"))
if (Grade >= 0 and Grade < 40):
    print ("The grade is: F")
elif (Grade >= 40 and Grade < 60):
    print ("The Grade is: B")
elif (Grade >= 60 and Grade < 80):
    print ("The Grade is: B+")
elif (Grade >= 80 and Grade <=100):
    print("The Grade is: A")
else:
    print ("Invalid grade.")
    print ("Please re-run the program and enter valid grade from 0 to 100 ")
