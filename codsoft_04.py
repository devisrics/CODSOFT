import random
def instruction():
    print("Welcome to the Rock,Paper,Scissor game!\n")
    print("Instructions:")
    print("1. Type 0 for Rock")
    print("2. Type 1 for paper")
    print("3. Type 2 for Scissor\n")
    print("Rules:")
    print("Rock beats Scissor")
    print("Scissor beats Paper")
    print("Paper beat Rock\n")

def getchoice(choice):
    if choice==0:
        return "Rock"
    elif choice==1:
        return "Paper"
    elif choice==2:
        return "Scissors"
    else:
        print("Invalid choice")

def game():
    instruction()
    
#user choice
    user_choice=int(input("Pick a number for Rock, Paper or Scissor:"))
    print(f"your choice is:{getchoice(user_choice)}")

#generate a random input for computer
    computer_choice=random.randint(0,2)
    print(f"computer chose:{getchoice(computer_choice)}")

    if user_choice>=3 or user_choice<0:
        print("you type an invalid number.you lose")
    elif user_choice==0 and computer_choice==2:
        print("you win!")
    elif computer_choice==0 and user_choice==2:
        print("you lose!")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win!")
    elif computer_choice == user_choice:
        print("It is Draw!")
    

while True:
    game()
    play_again=input("Do You Want to play again? (yes or no):").strip().lower()
    if play_again !='yes':
        print("Thanks For playing")
        break
