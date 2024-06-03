# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

num= input("Enter a value \t")
x= int(num)
if x%2==0 and x%3!=0:
    print("It only divisible by 2")
elif x%2!=0 and x%3==0:
    print("It only divisible by 3")
else:
    print("It is divisible by both 2 and 3")