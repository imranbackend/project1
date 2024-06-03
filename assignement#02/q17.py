# Write a program that takes the total amount of a purchase as input and applies a discount:
# If the amount is less than $100, no discount.
# If the amount is between $100 and $500, apply a 10% discount.
# If the amount is more than $500, apply a 20% discount.
# Print the final amount after the discount.
purchase_amount= input("enter purchase amount\t")
x= int(purchase_amount)
y= int(x)/100
#print(str(x))
if x<100:
    print(str(x)+"$ no discount")
elif (100<=x<=500):
    z=y*10
    b=x-z
    print(str(b)+"$ after discount 10%")
else:
    a=y*20
    c=x-a
    print(str(c)+"$ after discount 20%")