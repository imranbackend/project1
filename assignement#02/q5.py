# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
subject_a= input("Enter Grades \n")
grades= int(subject_a)
if grades>=80:
    print("A1 grade")
elif grades>=70 and grades<80:
    print("A grade")
elif grades>=60 and grades<70:
    print("B grade")
elif grades>=50 and grades<60:
    print("c grade")
else:
    print("Fail")