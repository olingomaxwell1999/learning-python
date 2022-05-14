import random

#Generate Random Number

random_number = random.randint(1, 10)

while True:
    try:
        user_guess = int(input("Please guess a number between 1 and 10\n"))
        if (user_guess == random_number):
            break
    except:
        print("Please provide an integer, don't ruin my program!")

print("Game Over!!! Congratulations, You win!!! The number was : ", random_number)