import random

comp = random.randint(1,100)
while True:

    try:
        player = int(input("Guess a number between 1-100: "))

        if player > comp:
            print("Too high")
        elif player < comp:
            print("Too low")
        elif player == comp:
            print("Congratulations! You guessed it")
            break
    except ValueError:
        print("Enter numbers only")

