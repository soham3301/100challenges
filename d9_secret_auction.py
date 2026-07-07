def user_inputs():
    print("Welcome to the secret auction program.")
    user_name = str(input("What is your name?: "))
    user_bid = int(input("What is your bid?: $"))
    return user_name, user_bid

def bidders_details_storer(names, bids):
    bidders_details = {}
    bidders_details[names] = bids
    return bidders_details

def bidding_calculations(the_details):
    highest_bid = 0
    highest_bidder = ""
    for names, bids in the_details.items():
        if highest_bid < bids:
            highest_bid = bids
            highest_bidder = names
    return highest_bidder, highest_bid

def result_display(highest_bidders_name, highest_bid):
    print(f"The name of the highest bidder is {highest_bidders_name} and the bid is ${highest_bid}")

def program_stopper():
    user_consent = str(input("Are there any ohter bidders? Y / N\n")).lower()
    if user_consent == "y":
        print("\n" * 20)
        return True
    else:
        return False

def main():
    bidders_details_stored = {}
    program_continues = True
    while program_continues:
        user_names, user_bids = user_inputs()
        bidders_details_stored.update(bidders_details_storer(user_names, user_bids))
        program_continues = program_stopper()
    highest_bidder_name, highest_bid = bidding_calculations(bidders_details_stored)
    result_display(highest_bidder_name, highest_bid)

main()

