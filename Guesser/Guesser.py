from random import randint
from art import logo
exit_guess = 0
exit_flag = True

def set_diff(difficulty):
    """Set difficulty - pass into function from input tries"""
    if difficulty == "easy":
        difficulty = 10
    if difficulty == "hard":
        difficulty = 5
    if difficulty == "exit":
        difficulty = 15

    return difficulty

def check_guess(guess_attempt,target_number):
    """Check guess(guess attempt) against random number"""
    if guess_attempt > target_number:
        print("To high")
        print("Guess again")
    
    if guess_attempt < target_number:
        print("To low")
        print("Guess again")

    if guess_attempt == target_number:
        print(f"You won, the answer was {target_number}.")

def play_game(exit_guess):

    print(logo)
    target_number = randint(1, 100)
    print("I am thinking of a number between 1 and 100.")

    tries = int((set_diff(input("Choose a difficulty. Type 'easy' or 'hard' or 'exit'.\n").lower())))
    
    if tries == 15:
        exit()

    print(f"You have {tries} attempts remaining to guess the number.")

    while exit_guess != target_number:
        try:
            guess = int(input("Make a guess: "))
            check_guess(guess, target_number)
            exit_guess = guess
        except ValueError:
            print("Invalid number entered")
            guess = int(input("Make a guess: "))
            check_guess(guess, target_number)
            exit_guess = guess

        if exit_guess != target_number:
            tries = tries - 1
            if tries == 0:
                print("You lose, Out of guess attempts!!!!")
                play_game(exit_guess)
            print(f"You have {tries} attempts remaining to guess the number.")

while exit_flag:
    play_game(exit_guess)