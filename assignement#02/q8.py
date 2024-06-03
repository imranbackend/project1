# Write a program to ask user its name and check whether name consists of 5 or more letters
name = input("Enter your name:") 
letters= name.replace(" ","")
num_of_words= len(letters)
print("Your name consists of "+str(num_of_words))
if num_of_words>5:
    print("Your name have greater than five letters")
elif num_of_words==5:
    print("Your name have five letters")
else:
    print("Your name have less than five letters")