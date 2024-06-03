# Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:
# If the years of service are less than 5, no bonus.
# If the years of service are between 5 and 10, bonus is 10% of the salary.
# If the years of service are more than 10, bonus is 20% of the salary.
# Print the bonus amount.
salary= input("enter amount of salary\t")
service_tenure= input("input service years\t")
x= int(salary)/100
y= int(service_tenure)
#print(str(x))
if y<5:
    print("no bonus your salary is "+str(salary))
elif (5<=y<10):
    z=10*x
    w=int(z)+int(salary)
    print(str(w)+" bonus is 10% of salary")
else:
    a=20*x
    e=int(a)+int(salary)
    print(str(e)+" bonus is 20% of salary")