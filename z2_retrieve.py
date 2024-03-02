import sqlite3

def display_questions():
    connection = sqlite3.connect('FridayProj5.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT id, question, answer
        FROM QuestAns
        
    ''')

    questions = cursor.fetchall()

    print("\n--- Quiz Bowl ---")

    score = 0

    for category, question, correct_answer in questions:
        user_answer = input(f"\nCategory: {category}\nQuestion: {question}\nYour Answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            
    print(f"\nYour Score: {score}/{len(questions)}")

    connection.close()
# Display existing quiz questions
display_questions()

