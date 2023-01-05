from replit import clear
from art import logo

print(logo)
resume = True
bidders = {}
def high_bid():
    max_bid = 0
    winner = ""
    for key in bidders:
        assign_bid = bidders[key]
        if int(bidders[key]) > int(max_bid):
            max_bid = assign_bid
            winner = key
    print(f"The winner is... {winner}, with a bid of ${max_bid}!")

print("Welcome to the silent Auction!") 

while resume is True:
    name = input("What is your name? ")
    bid = input("How much are you placing your bid for? $")
    bidders[name] = bid
    status = input("Any additional bidders? Type 'yes' or 'no'.\n").lower()
    if status == "yes":
        clear()
        print(logo)
    elif status == "no":
        resume = False
    else:
        print("Invalid Option")
clear()
high_bid()
