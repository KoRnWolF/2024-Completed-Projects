import random
from hangman_words import word_list
from hangman_art import stages, logo

placeholder = str()
correct_letter = []
previous_guesses = []
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

lenght = len(chosen_word)
for lenght in range(lenght):
    placeholder += "_"

print(logo)

print("Hint:")
print(placeholder)
print(stages[6])

exit = False
while exit == False:
    display = str()

    guess = (input("Guess a letter: ").lower())
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter) # appends the letter to correct_letter list to allow for future use of the previous guessed letters

        elif letter in correct_letter: # checks if current letter can be found in correct_letter list, if so it adds the letter to teh display string, as it iterates through the letters in chosen word
            display += letter

        else:
            display += "_"    

    if guess in previous_guesses:
        print(f"You already guessed: {guess}")
    elif guess not in chosen_word:
        print(f"You guessed : {guess}, it is not in the word, you lose a life.")
        lives -= 1
        print(f"****************************{lives} LIVES LEFT****************************")

    previous_guesses.append(guess)
    print(display) 
    print(stages[lives])

    if "_" not in display:
        exit = True

    elif lives <= 0:
        print(f"IT WAS {chosen_word}! YOU LOSE!!!")
        exit = True

   

