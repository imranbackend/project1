# Write a program that accepts 3 input from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

num_1= input("enter first value \t")
num_2= input("enter second value \t")
num_3= input("enter third value \t")
if num_2<num_1>num_3:
    print(str(num_1)+" is great than "+str(num_2)+" and "+str(num_3))
elif num_1<num_2>num_3:
    print(str(num_2)+" is great than "+str(num_1)+" and "+str(num_3))
elif num_1<num_3>num_2:
    print(str(num_3)+" is great than "+str(num_1)+" and "+str(num_2))
else:
    print("all are equal")