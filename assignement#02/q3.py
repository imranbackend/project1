# Write a program to check the number is positive or negative. User input.
num= input("enter number \n")
x=int(num)
if x<0:
    print("negative")
elif x==0:
    print("value is zero")
else:
    print("positive")