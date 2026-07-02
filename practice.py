import random 

words = ("apple", "banana", "mango", "potato","football")

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
    4: (" O  ",
        "/|\\",
        "    "),
    5: (" O  ",
        "/|\\",
        "/  "),
    6: (" O  ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guess):
    print("--------------------")
    for line in hangman[wrong_guess]:
        print(line)
    print("--------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_ans(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only a letter")
            continue

        guessed_letters.add(guess)

        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else:
            wrong_guess += 1

        if "_" not in hint:
            display_man(wrong_guess)
            display_ans(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guess >= len(hangman) - 1:
            display_man(wrong_guess)
            display_ans(answer)
            print("YOU LOSE!")
            is_running = False
        
if __name__ == "__main__":
    main()