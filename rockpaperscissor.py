import random
print("Select 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissor'.")
user_choice = int(input("Enter yor choice: "))
if (user_choice > 2 or user_choice < 0):
    print("You entered Invalid number.")
else: 
    computer_choice = random.randint(0,2)
    print("Computer chose: ",computer_choice)

    if user_choice == computer_choice:
        print("It's a draw.")

    elif user_choice == 0:
        if computer_choice == 2:
            print("Rock smashes Scissor. You WIN!")
        else:
            print("Paper covers Rock. You LOSE!")

    elif user_choice == 1:
        if computer_choice == 0:
            print("Paper covers Rock. You WIN!")
        else:
            print("Scissor cuts Paper. You LOSE!")
    elif user_choice == 2:
        if computer_choice == 1:
            print("Scissor cuts Paper. You WIN!")
        else:
            print("Rock smashes Scissor. You LOSE!")
