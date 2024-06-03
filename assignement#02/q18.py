# Write a program that takes a person's age as input and prints the age group they belong to:
# If the age is less than 13, print "Child".
# If the age is between 13 and 19 (inclusive), print "Teenager".
# If the age is 20 or above and less than 65, print "Adult".
#  If the age is 65 or above, print "Senior".
age= input("write your age \t")
x= int(age)
if x<13:
    print("Child")
elif x>=13 and x<=19:
    print("Teenager")
elif x>=20 and x<65:
    print("Adult")
else:
    print("Senior Citizen")