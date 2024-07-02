import random

target=random.randint(1,100)

while True:
    userChoice = input("Guess the Number or Quit:")
    if(userChoice == "Quit"):                # In case the user wants to quit the game in the middle it takes a string value "Quit"
        break
    
    userChoice = int(userChoice)             # If user dosen't want to quit the game then the user input becomes an Integer value for guessing the number
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")
        
print("-----GAME OVER------") 
