#create the same ATM machine program that we do in last class.
#features:
#allow only affiliated_card if age < 60
#allow govt employee regardless of age and affiliated_card
#charge 10 Rs more if grade is less than 18
# (hint: filename: if_statement/if_with_nested_if.py)

age= input("Enter your age in number\t")
nominal_charge= input("enter charges\t")
extra_charge= int(nominal_charge)+int(10)
grade= input("Enter your grade\t")
if int(age)<=60 and int(grade)<18:
    print("Your age is "+str(age))
    print("You are eligible for affiliated card and your charges are "+str(nominal_charge)+"Rs")
elif int(age)<=60 and int(grade)>=18:
        print("Your age is "+str(age))
        print("You are eligible for affiliated card your charges are "+str(extra_charge)+"Rs")
elif int(age)>60:
      print(" You are not eligible for affiliated card")