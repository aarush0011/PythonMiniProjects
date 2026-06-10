import random
  
def dice():
    while True: 
        
        user_input = input("Roll the dice? (y/n): ")
        how_many = int(input("How many dice you want roll(1-3): "))

        if(user_input.lower() == "y" and how_many == 1):
            die1 = random.randint(1,6)
            print(f'({die1})')
        elif(user_input.lower() == "y" and how_many == 2):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f'({die1},{die2})')
        elif(user_input.lower() == "y" and how_many == 3):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            die3 = random.randint(1,6)
            print(f'({die1},{die2},{die3})')
        elif(user_input.lower() == "n"):
            print("Not rolling")
            break
        else:
            print("Invalid Choice, type 'y' or 'n'")
            print("Thnak you!")

dice()
