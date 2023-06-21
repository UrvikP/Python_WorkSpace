import os
from art import logo

print(logo)
auction_bidders = {}
status = True
while status:
    name = input("What is the bidder's name: ")
    bid = int(input("What is the bid ammount: "))

    auction_bidders[name] = bid

    others = input("Are there any other bidders? Yes or No: ")

    if others == "No":
        status = False
    os.system("clear")

highest_bidder = ""
largest_bid_ammount = 0
for bidder in auction_bidders:
    bid_amount = auction_bidders[bidder]
    if bid_amount > largest_bid_ammount:
        highest_bidder = bidder
        largest_bid_ammount = bid_amount

print(f"The winner is {highest_bidder}. Congradulations!")
