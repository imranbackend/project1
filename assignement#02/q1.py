# Write a program to check whether a person is eligible to vote or not?

age= input("enter your age \n")
x=int(age)
#x=19 (we can also start code from here to check condition is true or not)
if x<18:
    print("you are not eligible for vote")
else:
    print("you are eligible for vote")