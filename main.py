questions = ("Who is Saitama?: ",
             "Who is Ken Kaneki?: ",
             "Who can beat Saitama?: ",
             "Which one is the best class?: ")

options = (("A. Doctor", "B. Caped Baldy", "C. Politician", "D. Mafia"),
            ("A. Whale", "B. Vampire", "C. Ghoul", "D. Ostrich"),
            ("A. Blast", "B. God", "C. Garou", "D. NO ONE!"),
            ("A. Necromancer", "B. Knight", "C. Theif", "D. Samurai"))

answers = ("B", "C", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your score is: {score}%")