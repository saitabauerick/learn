import random

computer=random.randint(1,100)
guees=input("choose a number between 1 and 100: ")

while True:
    if guees==computer:
        print("congeratulations you gueesd the number correct")
    elif guees!=computer:
        print("the number is incorrect")
    else:
        print("invalid choice")
    

    