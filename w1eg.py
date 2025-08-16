import random

def run_quiz():
    """
    Runs the main quiz game loop.
    """
    # List of questions. Each question is a dictionary.
    # The 'options' key is a list of multiple-choice answers.
    # The 'correct_answer' key stores the index of the correct option.
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "correct_answer": 2  # Index of 'C. Paris'
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["A. list", "B. tuple", "C. float", "D. array"],
            "correct_answer": 3  # Index of 'D. array'
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. fun", "B. define", "C. def", "D. function"],
            "correct_answer": 2  # Index of 'C. def'
        },
        {
            "question": "What does the 'pass' statement do in Python?",
            "options": ["A. Skips the function call", "B. Ends the program", "C. Is a placeholder for future code", "D. Returns a value"],
            "correct_answer": 2  # Index of 'C. Is a placeholder for future code'
        },
        {
            "question": "What is the output of 'print(2 ** 3)'?",
            "options": ["A. 6", "B. 8", "C. 9", "D. Error"],
            "correct_answer": 1  # Index of 'B. 8'
        }
    ]

    score = 0
    # Randomize the order of questions for a fresh game each time.
    random.shuffle(questions)

    # Loop through each question in the list.
    for i, q in enumerate(questions):
        print(f"\n--- Question {i + 1} of {len(questions)} ---")
        print(q["question"])
        
        # Display all answer options.
        for option in q["options"]:
            print(option)
        
        # Loop until the user provides a valid integer input.
        while True:
            try:
                user_answer = int(input("Enter the number of your choice (1, 2, 3, or 4): "))
                # Adjust for 0-based indexing.
                user_answer -= 1
                
                if 0 <= user_answer < len(q["options"]):
                    # Check if the user's answer is correct.
                    if user_answer == q["correct_answer"]:
                        print("Correct! 🎉")
                        score += 1
                    else:
                        print(f"Incorrect. 😔 The correct answer was { q['options'][q['correct_answer']] }.")
                    break  # Exit the inner loop once a valid answer is given.
                else:
                    print("Invalid choice. Please enter a number from 1 to 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # After the quiz, display the final score.
    print("\n--- Quiz Complete! ---")
    print(f"You scored {score} out of {len(questions)}! 🏆")

def main():
    """
    Main function to start the game and handle 'play again' logic.
    """
    while True:
        run_quiz()
        
        # Ask the user if they want to play again.
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Entry point of the script.
if __name__ == "__main__":
    main()






