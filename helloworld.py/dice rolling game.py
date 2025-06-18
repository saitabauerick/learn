import random

play1=random.randint(1,10)
play2=random.randint(1,10)



while True: 
    choice=input("role dice?y/n: " ).lower()
    if choice=="y":
        print(f'({play1}, {play2})')
    elif choice=="n":
        print("thanks for playing!")
        break
    else:
        print("invalid choice")
    
