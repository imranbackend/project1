# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5
num_1= input("Enter First Value\t")
num_2= input("Enter Second Value\t")
if num_1>num_2:
    print(str(num_1)+" is greater than "+str(num_2))
elif num_1<num_2:
    print(str(num_2)+" is greater than "+str(num_1))
else:
    print("Both are equal")