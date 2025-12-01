import random

print("Welcome to Rock-Paper-Scissors!")
print("Enter your choice: rock, paper, or scissors.")
print("Type 'exit' to quit.\n")

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Your move: ").lower()
    if user_choice == "exit":
        print("Thanks for playing! Goodbye!")
        break
    if user_choice not in choices:
        print("Invalid choice, please enter rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win! 🎉\n")
    else:
        print("You lose! 😞\n")

    print("Let's play again!\n")
    