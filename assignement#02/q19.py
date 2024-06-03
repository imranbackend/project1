#Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:
#If the customer is a member:
#   If the purchase amount is $50 or more, print "Eligible for 10% discount".
#    Otherwise, print "Eligible for 5% discount".
#If the customer is not a member:
#    If the purchase amount is $100 or more, print "Eligible for 5% discount".
#    Otherwise, print "No discount".
customer= input("Are you member: yes/no?\n")
x=customer.upper()
purchase=input("enter amount\t")
y=int(purchase)
#print(x)
if x=="YES" and y>=50:
    discount_1=y-y*0.1
    print("dear member you are discounted with 10% and amount is "+str(discount_1)+"$")
if x=="YES" and y<50:
    discount_2=y-y*0.05
    print("dear member you are discounted with 5% and amount is "+str(discount_2)+"$")
if x=="NO" and y>=100:
    discount_3=y-y*0.05 
    print("dear non-member you are discounted with 5% and amount is "+str(discount_3)+"$")
if x=="NO" and y<100:
    print("dear non-member you are not earned any discount and the amount is "+str(y)+"$")

    
