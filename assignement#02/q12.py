# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15
num_1= input("enter first value \t")
num_2= input("enter second value \t")
num_3= input("enter third value \t")
if num_2>num_1>num_3:
    print(str(num_1)+" as this number is larger than "+str(num_3)+" and smaller than "+str(num_2))
elif num_2<num_1<num_3:
    print(str(num_1)+" as this number is larger than "+str(num_2)+" and smaller than "+str(num_3))
elif num_1>num_2>num_3:
    print(str(num_2)+" as this number is larger than "+str(num_3)+" and smaller than "+str(num_1))
elif num_1<num_2<num_3:
    print(str(num_2)+" as this number is larger than "+str(num_1)+" and smaller than "+str(num_3))
elif num_1>num_3>num_2:
   print(str(num_3)+" as this number is larger than "+str(num_2)+" and smaller than "+str(num_1))
elif num_1<num_3<num_2:
     print(str(num_3)+" as this number is larger than "+str(num_1)+" and smaller than "+str(num_2))
elif num_1>num_2 and num_2==num_3:
     print(str(num_1)+" as this number is larger than equal number of "+str(num_2)+" and "+str(num_3))
elif num_2>num_1 and num_1==num_3:
     print(str(num_2)+" as this number is larger than equal number of "+str(num_1)+" and "+str(num_3))
elif num_3>num_2 and num_2==num_1:
     print(str(num_3)+" as this number is larger than equal number of "+str(num_2)+" and "+str(num_1))
else:
    print("all are equal")