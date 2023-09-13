# The (not so) Secret Auction Program

from art import logo

def auction(bidders):

    highestBid = 0
    highestBidder = ""

    for bidder in bidders:
        if(bidders[bidder] > highestBid):
            highestBid = bidders[bidder]
            highestBidder = bidder
    print(f"The winner of the auction is: {highestBidder} with a bid of ${highestBid}")

bidders = {}
biddingFinished = False
while not biddingFinished:
    print("Welcome to the secret auction program. ")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    continuee = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bidders[name] = bid

    if continuee == "no":
        auction(bidders)
        biddingFinished = True
    elif continuee == "yes":
        auction(bidders)
