import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pull_player_card(cards_player):

    rand = random.randint(0, 12)
    cards_player.append(cards[rand])

def pull_pc_card(cards_pc):
        
    rand = random.randint(0, 12)
    cards_pc.append(cards[rand])

def player_score(cards_player):

    if 11 in cards_player and 10 in cards_player and len(cards_player) == 2:
        return 0

    return sum(cards_player)

def pc_score(cards_pc):
    if 11 in cards_pc and 10 in cards_pc and len(cards_pc) == 2:
        return 0

    return sum(cards_pc)

def play_game():

    cards_player = []
    cards_pc = []
    player_status = ""
    pc_status = ""
    draw = bool
    pull_cards = "y"

    os.system('cls')

    print(logo)

    if pull_cards == "y":
        for x in range(0,2):
            pull_player_card(cards_player)

        pull_pc_card(cards_pc)
        print(f"Current cards Player:{cards_player}, current score:{player_score(cards_player)}")
        print(f"Computers first card : {cards_pc}")

    if pull_cards =="n":
        exit()
            
    pull_cards = input("Another card 'y' or 'n' to pass?")
    while pull_cards == "y" and player_score(cards_player) < 21 and player_score(cards_player) != 0:

        pull_player_card(cards_player)
        print(f"Current cards Player:{cards_player}, current score:{player_score(cards_player)}")
        print(f"Computers first card : {cards_pc}")

        if player_score(cards_player) > 21:
            try:
                eleven = cards_player.index(11)
                cards_player[eleven] = 1
                os.system('cls')
                print(f"Current cards Player:{cards_player}, current score:{player_score(cards_player)}")
                print(f"Computers first card : {cards_pc}")
            except:
                print("")

        if player_score(cards_player) <= 21:
            pull_cards = input("Another card?")
        

    if player_score(cards_player) > 21:
            print("Player bust")
            player_status = "bust"

    if pull_cards == "n" and player_status != "bust":
        while pc_score(cards_pc) < 17:

            if pc_score(cards_pc) < 21:
                pull_pc_card(cards_pc)
            
            if pc_score(cards_pc) > 21: #Shitty code, look into
                try:
                    eleven = cards_pc.index(11)
                    cards_pc[eleven] = 1
                except:
                    print("")

            if pc_score(cards_pc) > 21:
                print("PC bust")
                pc_status = "bust"

            if pc_score(cards_pc) == player_score(cards_player):
                draw = True

        if player_score(cards_player) > pc_score(cards_pc) or pc_status == "bust" and player_status != "bust":
            os.system('cls')
            print("Player Wins")
        if player_score(cards_player) < pc_score(cards_pc) and pc_status != "bust":
            os.system('cls')
            print("PC Wins")
        if draw == True:
            os.system('cls')
            print("Game is a draw")

    if player_score(cards_player) == 0:
        print("Black Jack")

        
    print(f"Players final hand:{cards_player}, final score:{player_score(cards_player)}")
    print(f"Computers final hand : {cards_pc}, final score:{pc_score(cards_pc)}")

while input("Do you want to play a game? y/n \n") == "y":
    play_game()

