import random



while True:

    my_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose {my_choice}, computer chose {computer_choice}.\n")

    if my_choice == computer_choice:
        print(f"Both players selected {my_choice}. It's a tie!")
    elif my_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif my_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif my_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Wrong Choice ")
        break

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == "n":
        print("\n E X I T ")
        break