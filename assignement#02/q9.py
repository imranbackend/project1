# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50

num_1= input("enter first value \t")
num_2= input("enter second value \t")
operation= input("enter what operation you need \t")
if operation=="*":
    print(int(num_1)*int(num_2))
elif operation=="+":
    print(int(num_1)+int(num_2))
elif operation=="-":
    print(int(num_1)-int(num_2))
elif operation=="%":
    print(int(num_1)%int(num_2))
else:
    print("invalid sign")