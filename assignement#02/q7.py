
#(To determine if a year is a leap year, we apply a simple rule: 
#if the year is divisible by 4, it's a leap year,
#except for end-of-century years, which must also be divisible by 400. 
#For instance, the year 2000 was a leap year, while 1900 was not. 
#2024, 2028, 2032 and 2036 are all leap years.)

year= input("put the year \n")
x=int(year)
if (x%4==0 and x%100 !=0) or (x%400==0):
    print("it is leap year")
else:
    print("it is not a leap year") 