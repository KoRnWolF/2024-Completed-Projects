import random

choice = ""

while choice != 3:

    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors, 3 to EXIT\n"))

    if choice >= 3:
        print("Invalid number you lose")
        break

    if choice == 3:
        break

    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''
    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    rpc = [rock, paper, scissors]
    outcome = ["win", "lose", "draw"]
    x = int()
    aichoice = random.randint(0, 2)


    if choice == 0 and aichoice == 2:
        x = 0
    elif choice == 1 and aichoice == 0:
        x = 0
    elif choice == 2 and aichoice == 0:
        x = 1
    elif aichoice > choice:
        x = 1
    elif choice > aichoice:
        x = 0
    else:
        x = 2

    

    # if choice == 0 and aichoice == 1:
    #     x = 1
    # if choice == 0 and aichoice == 2:
    #     x = 0
    # if choice == 0 and aichoice == 0:
    #     x = 2
    # if choice == 1 and aichoice == 2:
    #     x = 1
    # if choice == 1 and aichoice == 0:
    #     x = 0
    # if choice == 1 and aichoice == 1:
    #     x = 2
    # if choice == 2 and aichoice == 0:
    #     x = 1
    # if choice == 2 and aichoice == 1:
    #     x = 0
    # if choice == 2 and aichoice == 2:
    #     x = 2

    print("Your choice:")
    print(rpc[choice])
    print("Computer chose:")
    print(rpc[aichoice])
    print(f"You",outcome[x])
    print("\n")
