from art import logo
print(logo)

# TODO-1: Ask the user for input
bid_entry = {}

rehash_questions = True
while rehash_questions:

    name = input("What is your name?:")
    price = int(input("What's your bid amount?: $"))
    keep_bidding = input("Is there another bidder? Yes or No?").lower()

# TODO-2: Save data into dictionary {name: price}
    bid_entry[name] = price

# TODO-3: Whether if new bids need to be added
    if keep_bidding == "yes":
        print("\n" * 100)
    elif keep_bidding == "no":
        print("\n" * 100)
        rehash_questions = False
    else:
        rehash_questions = True
        print("Make sure to type either 'Yes' or 'No' please.")
        keep_bidding = input("Is there another bidder? Yes or No?").lower()
        if keep_bidding == "yes":
            print("\n" * 100)
        elif keep_bidding == "no":
            print("\n" * 100)
            rehash_questions = False

# TODO-4: Compare bids in dictionary
winner = max(bid_entry, key=bid_entry.get)
print(f"The highest bidder is {winner} with a bid amount of ${bid_entry[winner]}.")
