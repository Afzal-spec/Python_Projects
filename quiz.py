def new_game():
    
    guesses = []
    correct_guess = 0
    question_num = 1
    for key in questions:
        print("_ _ _ _ _  _ _ _ _ _ _  _ _ _")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A,B,C or D: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key),guess)
        question_num+=1


    display_score(correct_guess,guesses)
    


def check_answer(answer, guess):
    if(answer == guess):
        print("Correct")
        return 1
    else :
        print("Wrong")
        return 0
    

def display_score(correct_guesses, guesses):
    print("_ _ _ _ __  _ _ _ _ ")
    print("Results")
    print("_ _ _ _ _ _ _  _ _  _ _ ")

    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is :"+ str(score)+"%")


    
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else :
        return False


questions = {
    "who created python?: ":"A",
    "what year was python created?: ": "B",
    "pythin is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"

}

options = [["A.Guido Van Rossom","B.Elon mask","C.Mark zukerberg","D.james doom"],
           ["A.1989","B.1991","C.2016","D.2000"],
           ["A.Lonely Island","B.smoosh","C.Monty python","D.SNL"],
           ["A.True", "B.False", "C.maybe", "D.dont know"]]

new_game()

while play_again():
    new_game()

print("BYEEE !")
