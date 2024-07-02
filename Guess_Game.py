import random
import string

def number_guessing_game():
    target = random.randint(1, 100)
    
    while True:
        userChoice = input("Guess the Number or type 'Quit' to exit: ")
        if userChoice.lower() == "quit":  # Case insensitive quit
            break

        try:
            userChoice = int(userChoice)  # If user doesn't want to quit, convert input to an integer for guessing the number
        except ValueError:
            print("Please enter a valid number.")
            continue

        if userChoice == target:
            print("Success: Correct Guess!!")
            break
        elif userChoice < target:
            print("Your number was too small. Take a bigger guess..")
        else:
            print("Your number was too big. Take a smaller guess..")
    
    print("-----GAME OVER------")

def letter_guessing_game():
    target = random.choice(string.ascii_uppercase)
    
    while True:
        userChoice = input("Guess the Letter (A-Z) or type 'Quit' to exit: ").upper()  # Ensure input is uppercase
        if userChoice == "QUIT":  # Case insensitive quit
            break

        if len(userChoice) != 1 or userChoice not in string.ascii_uppercase:
            print("Please enter a valid letter (A-Z).")
            continue

        if userChoice == target:
            print("Success: Correct Guess!!")
            break
        elif userChoice < target:
            print("Your letter is too early in the alphabet. Try a later letter.")
        else:
            print("Your letter is too late in the alphabet. Try an earlier letter.")
    
    print("-----GAME OVER------")

def main():
    print("Choose the game mode:")
    print("1. Number Guessing Game")
    print("2. Letter Guessing Game")
    game_choice = input("Enter 1 or 2: ")

    match game_choice:
        case "1":
            number_guessing_game()
        case "2":
            letter_guessing_game()
        case _:
            print("Invalid choice. Exiting the game.")

if __name__ == "__main__":
    main()
