from art import logo
print(logo)

def compare_bids(bidding_record):
    max_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a total bid of ${max_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        compare_bids(bids)
    elif should_continue == "yes":
        print("\n" * 100)
