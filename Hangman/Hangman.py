import random
placeholder = str()
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

random_number = random.randint(0,2)
chosen_word = word_list[random_number]
print(chosen_word)

word_len = len(chosen_word)
for word_len in chosen_word:
    placeholder += "_"


display = ""
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(placeholder)
print(placeholder.count("_"))
x = 0
while x != 4:
    display = ""
    x += 1
    guess = input("Please guess your letter?\n").lower()

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
    #  is, "Wrong" if it's not.


    for letter in chosen_word:
        if letter == guess:
            display += letter

        else:
            display += "_"

print(display)