# Write a program that takes a password as input and checks its strength:
# If the password length is less than 6, print "Weak password".
# If the password length is between 6 and 12, print "Moderate password".
# If the password length is more than 12, print "Strong password".
password= input("input password without space\n")
x=len(password)
if x>=12:
    print("Strong password")
elif 6<x<12:
    print("moderate password")
else:
    print("Weak password")