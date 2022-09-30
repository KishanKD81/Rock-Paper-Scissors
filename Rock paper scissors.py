
import random

def game():

    kepp=random.choice(["r","p","s"])
    user=input("r for ROCK , p for PAPER , s for SCISSORS-->")
    
    if user==kepp:
        print("Same")
        print("Do again")
        return game()

    elif user=="r" and kepp=="p":
        print(f"Computer won as user is {user} and comp is {kepp}")
        
    elif user=="r" and kepp=="s":
        print(f"User won as user is {user} and comp is {kepp}")

    elif user=="p" and kepp=="s":
        print(f"Computer wins as user is {user} and comp is {kepp}")

    elif user=="p" and kepp=="r":
        print(f"User won as user is {user} and comp is {kepp}")


    elif user=="s" and kepp=="r":
        print(f"Computer won as user is {user} and comp is {kepp}")

    elif user=="s" and kepp=="p":
        print(f"User  won as user is {user} and comp is {kepp}")

game()
