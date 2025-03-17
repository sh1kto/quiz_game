# Function to load questions from file
def load_questions(filename):
    questions = []
    options = []
    answers = []
    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")  # Split the line by ";"
            if len(parts) == 6:  # Ensure it has the correct format
                questions.append(parts[0])  # Question
                options.append(tuple(parts[1:5]))  # Options (as a tuple)
                answers.append(parts[5])  # Correct answer

    return questions, options, answers


# Load questions from file
questions, options, answers = load_questions("questions/demo.qnf")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    # Input validation
    while True:
        guess = input("Enter (A, B, C, D): ").upper()
        if guess in ["A", "B", "C", "D"]:
            break
        print("Invalid choice! Please enter A, B, C, or D.")
    
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1

# Display results
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", " ".join(answers))
print("guesses: ", " ".join(guesses))

score_percentage = round((score / len(questions)) * 100, 2)
print(f"Your score is: {score_percentage}%")
