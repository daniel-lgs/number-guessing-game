from art import logo
from replit import clear
import random

end_game = False

print(logo)
print("Welcome to the number guessing game!\n")
print("Your objective is to guess the number chosen by the computer between 1 and 100.\n")
input("Press enter to start...")
clear()

while not end_game:
    print(logo)
    random_number = random.randint(1, 100)
    game_mode = ""
    
    while game_mode != 'easy' and game_mode != 'hard':
        game_mode = input("Type 'easy' to easy mode or 'hard' to hard mode: ").lower()
        if game_mode == "easy":
            attempts = 10
            print("You have 10 attempts...\n")
        elif game_mode == "hard":
            attempts = 5
            print("You have 5 attempts...\n")
            
    user_number = 0
    
    while attempts > 0:
        user_number = int(input("Guess a number: "))
        if user_number == random_number:
            print("Congratulations! You're right 🎉")
            break
        elif user_number != random_number and attempts == 1:
            print("You lose 😢. But try again!")
        elif user_number < random_number:
            print("Too low.")
        elif user_number > random_number:
            print("Too high.")
        attempts -= 1
        
    end_game = True
