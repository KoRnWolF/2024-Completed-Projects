import random
exit_guess = 0

target_number = random.randrange(1, 100)

def set_diff(difficulty):
    if difficulty == "easy":
        difficulty = 10
    if difficulty == "hard":
        difficulty = 5

    return difficulty

def check_guess(guess_attempt):
    if guess_attempt > target_number:
        print("To high")
        print("Guess again")
    
    if guess_attempt < target_number:
        print("To low")
        print("Guess again")

    if guess_attempt == target_number:
        print(f"You won, the answer was {target_number}")

print("I am thinking of a number between 1 and 100.")
tries = int((set_diff(input("Choose a difficulty. Type 'easy' or 'hard'\n").lower())))
print(f"You have {tries} attempts remaining to guess the number.")


while exit_guess != target_number:

    # guess = int(check_guess(input("Make a guess:"),tries))
    guess = int(input("Make a guess: "))
    check_guess(guess)
    exit_guess = guess
    if exit_guess != target_number:
        tries = tries - 1
        print(f"You have {tries} attempts remaining to guess the number.")
