# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input
colour_sign= input("enter the colour\t")
x= colour_sign .upper()
#print(x)
if x== "RED":
    print("Car has to stop")
elif x== "GREEN":
    print("Car is allowed to go")
elif x== "ORANGE":
    print("Car has to wait")
else:
    print("invalid input")