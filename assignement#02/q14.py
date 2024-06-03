# Write a program that takes two numbers as input and prints:
# "First number is greater" if the first number is greater than the second number.
# "Second number is greater" if the second number is greater than the first number.
# "Both numbers are equal" if the two numbers are equal.
num_1= input("enter first number\t")
num_2= input("enter second number\t")
if num_1>num_2:
    print("first value is greater than second: "+str(num_1)+">"+str(num_2))
elif num_1<num_2:
    print("second value is greater than first: "+str(num_2)+">"+str(num_1))
else:
    print("Both values are equal: "+str(num_1)+" = "+str(num_2))
