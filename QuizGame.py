questions = ("What is the capital of Australia?",
             "Which planet is known as the Red Planet?",
             "Who wrote the play Romeo and Juliet?",
             "What is the chemical symbol for gold?",
             "Which country is home to the Great Barrier Reef?")

options = (("A. Sydney","B. Melbourne","C. Canberra","D. Perth"),
           ("A. Venus","B. Mars","C. Jupiter","D. Saturn"),
           ("A. Charles Dikens","B. Williams Shekespears","C. Mark Twain","D. Jane Austen"),
           ("A. Go","B. Cu","C. Au","D. Ag"),
           ("A. India","B. Australia","C. Brazil","D. Maxico")
           )

answers = ("C","B","B","C","B")
guesses = []
score = 0
queNum = 0

for question in questions:
    print("---------------------")
    print(question)

    for option in options[queNum]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[queNum]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[queNum]} is the correct answer")
    queNum += 1

print("--------------------------")
print("RESULT:- ")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is: {score}%")