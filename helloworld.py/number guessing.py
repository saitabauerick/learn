import random

computer=random.randint(1,100)


while True:
    choice=int(input("guess a number between 1 and 100: "))
    if choice<computer:
        print("too low")
    elif choice>computer:
        print("too high")
    elif choice==computer:
        print("congratulations you have guess the number correcty")
        break
    else:
        print("invalid choice")
        break