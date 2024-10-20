import os
from art import logo
print(logo)

bidders = {}
choice = "yes"

def highest_bidder(bidders):
    highest_bid = 0
#alternate - can get hold of the value(bid amount) from a dict - Bidder = key, bidding_record = dict
#    for bidder in bidding_record:
#       bid_amount = bidding_record[bidder]

    for name, bid in bidders.items():
        if bid > highest_bid:

            highest_bid = bid
            winner = name.capitalize()

    print(f"{winner} has the winning bid with, R{highest_bid}!")

while choice != "no":

    name = input("What is you name?\n").lower()
    bid = int(input("What is you bid?\n"))

    bidders[name] = bid # input name and bid into dict

    choice = input("Is there other bidders? 'yes' or 'no'\n")
    if choice == "no":
        os.system('cls')
        highest_bidder(bidders)
    else:
        os.system('cls')




