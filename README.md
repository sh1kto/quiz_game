# 🧠 Quiz Game  

A simple command-line quiz game in Python that loads multiple-choice questions from a file and evaluates the user's answers.  

![Static Badge](https://img.shields.io/badge/Prerequisites-Python-brightgreen)  

## 📌 Features  

✅ Loads questions dynamically from a `.qnf` file.  
✅ Supports multiple-choice questions (A, B, C, D).  
✅ Validates user input to prevent incorrect responses.  
✅ Provides real-time feedback and a final score.  

## 🛠 Installation  

### Prerequisites  

- Python must be installed on your system. You can download it from [python.org](https://www.python.org/).  

### Steps  
1. **Clone the repository:**  
   ```sh
   git clone https://github.com/sh1kto/quiz-game.git
   cd quiz-game
   ```  

2. **Run the script:**  
   ```sh
   python main.py
   ```  

## 📂 Question File Format  

The quiz loads questions from a `.qnf` file located in the `questions` folder in the following format:  

```
Question1;OptionA;OptionB;OptionC;OptionD;CorrectAnswer
Question2;OptionA;OptionB;OptionC;OptionD;CorrectAnswer
```

Example:  

```
What is the capital of France?;A) Berlin;B) Madrid;C) Paris;D) Rome;C
Which planet is known as the Red Planet?;A) Earth;B) Venus;C) Mars;D;Jupiter;C
```

## 🏆 Scoring  

- Correct answers increase the score.  
- Final results display the user's accuracy as a percentage.  

## 📸 Screenshots  
![Quiz Game](https://raw.githubusercontent.com/sh1kto/quiz_game/refs/heads/main/qz_sc1.png)

## 📜 License  

This project is open-source. Feel free to modify and improve it!
