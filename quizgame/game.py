import random as r

count = 0
player = int(input("Let's play a game. If you want to play, enter 1. Otherwise, enter 0: "))

if player == 1:
    computer = r.randint(1, 10)

    while True:
        option = int(input("I have a number, you have to guess it: "))

        if computer == option:
            print("Congratulations! You win.")
            count += 1
            break
        else:
            print("Try again.")
            count += 1

print("Game over. You took", count, "tries.")


