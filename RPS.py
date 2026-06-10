import random

valid_coices = ('r','p','s')
print("Welcome to Rock, Paper and Scissors! (Enter 'q' to quit)")

while True:
        comp = random.choice(['r','p','s']).lower()
        player = str(input("Rock, Paper or Scissors? (r/p/s): ")).lower()

        if player == 'q':
            print("Thank you for playing!")
            break
    
        if player not in valid_coices:
            print("Invalid choice. Choose from r/p/s")
            continue

        if comp == 'r' and player == 'r':
            print("Its a Tie!")
        elif comp == 'r' and player == 'p':
            print("You Win!")
        elif comp == 'r' and player == 's':
            print("You Lose!")

        elif comp == 'p' and player == 'p':
            print("Its a Tie!")
        elif comp == 'p' and player == 'r':
            print("You Lose!")
        elif comp == 'p' and player == 's':
            print("You Win!")

        elif comp == 's' and player == 's':
            print("Its a Tie!")
        elif comp == 's' and player == 'r':
            print("You Win!")
        elif comp == 's' and player == 'p':
            print("You Lose!")