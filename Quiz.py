from quiz_question_list import Questions

# quiz.py
def exit():
    choice=input('Wanna Give more Try (type "yes" to **continue** else type "no" to **exit**): ').lower()
    if choice == "yes":
        print ("Since, You chose to continue playing. So, then let's start the game again!")
        main()
    elif choice == "no":
        print("Thank you for playing! **Goodbye**!")
        quit()
    else:
        print("Thank you for playing! **Goodbye**!")
        
print("\nQuick Quiz Game")
print("Please type all answers in English except choosing number.")
print("Please use correct English grammar and spelling.")


def main():
    qa_data = Questions() # get the question from dictionary
    # Display the instructions and chossing options
    try:
        print ("Choose the number of the question you want to answer (1-200) wisely:")
        value = int(input("Please choose a number from 1 to 200: "))
    except ValueError:
        print("Invalid input. Please enter a number.")      
        return main()

    if value in qa_data:
        q = qa_data[value]["question"]
        a = qa_data[value]["answer"]
        user_ans = input(q + " ").strip().lower()

        if user_ans == a.lower():
            print("Your answer is correct!! :)")
            exit()
        else:
            print("Your answer is incoreect! :( Better luck next time!!")
            print(f"The correct answer was: {a}")
            exit()
    else:
        print("No question found for that number.")
        main()
main()