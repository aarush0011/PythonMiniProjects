import random 
from words import *

hangman = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "/  "),
    6: (" O ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("-------------------------")
    for line in hangman[wrong_guesses]:
        print(line)
    print("-------------------------")
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    print("Welcome to The Hangman")
    print("If you see a full stickman figure that means you LOSE!")
    print("HINT: guess only animals or fruits")
    answer = random.choice(words)
    hint = ["_"]*len(answer) 
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Type only a letter")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' is already guessed")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU GUESSED IT!\nYOU WIN!")
            is_running = False            
        elif wrong_guesses >= len(hangman) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()