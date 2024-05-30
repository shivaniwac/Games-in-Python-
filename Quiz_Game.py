def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key, value in question.items():
        print("")
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(value, guess)
        question_num += 1 

    display_score(correct_guesses, guesses)

def check_answer(answers, guess):
    if answers == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("")
    print("Results")
    print("")
    print("Correct Guesses: ", correct_guesses)
    print("Answer: ", end="")
    for i in question:
        print(question.get(i), end="")
    print()  
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="") 
    print()
    score = int((correct_guesses/len(question))*100)
    print("Your score is : "+str(score)+"%")

def play_again():
    response = input("Do you want to play again? (yes or no ): ").upper()

    if response == "YES":
        return True
    else:
        return False

question={
    "What is the capital of India?": "A", 
    "Who is the prime minister of India?": "B",
    "How many states INDIA has?": "C",
    "Which party, you are in favour?": "D"
}
answers=[["A. Delhi","B. Punjab","C. Maharashtra","D. Uttar Pradesh"],
         ["A. RajNath","B. Narendra Modi", "C. Amit shah","D. Rahul gandhi"],
         ["A. 26","B. 25","C. 28","D. 29"],
         ["A. BJP","B. AAP","C. Congress","D. NOTA"]]

new_game()
while play_again():
    new_game()
print("bye")