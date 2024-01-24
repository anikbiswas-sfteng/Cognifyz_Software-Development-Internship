import random

def number_guesser():
    print("Welcome to Cognifyz Number Guesser!")
    print("I have selected a random number between 1 and 10. Can you guess it?")
    
    # Generate a random number between 1 and 10----
    
    secret_number = random.randint(1, 10)
    
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            # Get user input for the guess
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is correct
            if guess == secret_number:
                print("Congratulations! You Guess is Great.")
                break
            else:
                print("Wrong guess. Try again.")
                
            attempts += 1
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # If the player couldn't guess the number in the allowed attempts
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guesser()
#Made by nikDev