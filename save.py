import random
print("I am thinking of a number between and 1 and 10")
number = random.randint(1,10)
congratlsfg = True
while congratlsfg:
    guess = input("guess a number ")
    if guess == number:
        print("congrats, u got it ")
        break
    else:
        print("try again to win the game!")
