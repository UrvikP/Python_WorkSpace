import os
from art import logo

print(logo)
auction_bidders = {}
status = True
while status:
    name = input("What is the bidder's name: ")
    bid = input("What is the bid ammount: ")

    auction_bidders[name] = bid

    others = input("Are there any other bidders? Yes or No: ")

    if others == "No":
        status = False
    os.system("clear")

highest_bidder = ""
largest_bid_ammount = 0
for bidder in auction_bidders:
    if auction_bidders[bidder] > largest_bid_ammount:
        highest_bidder = bidder
        largest_bid_ammount = auction_bidders[bidder]

print(f"The winner is {highest_bidder}. Congradulations!")
