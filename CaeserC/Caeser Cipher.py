from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice = "yes"
print(logo)

while choice == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(direction, original_text, shift_amount):

        if direction == "encode":

            encoded_text = str()
            for letter in original_text:
                if letter in alphabet:
                    text_index = alphabet.index(letter)
                    shifted_index = (text_index + shift_amount) % len(alphabet)
                    encoded_text += alphabet[shifted_index]
                else:
                    encoded_text += letter

            print(f"Here is the encode result:",encoded_text) 

        if direction == "decode":

            decoded_text = str()
            for letter in original_text:
                if letter in alphabet:
                    text_index = alphabet.index(letter)
                    shifted_index = (text_index - shift_amount) % len(alphabet)
                    decoded_text += alphabet[shifted_index]
                else:
                    decoded_text += letter

            print("Here is the decoded result:",decoded_text) 


    caesar(direction, original_text = text, shift_amount = shift)

    choice = input("Would you like to go again type yes or no?\n").lower
