""" The Challenge: "The Smart ATM"
You are building a security system for an ATM. Write a script that does the following:
1. The Setup: Create a list of blocked_cards containing the numbers 1111, 2222, and 3333.
2. The Loop: Use a while loop to give a user 3 attempts to enter a valid card number.
3. Input & Comparison: Ask the user for their card number (use int(input())).
4. Logical Operators:
    - If the card number is not in the blocked_cards list, and it is a 4-digit number (between 1000 and 9999), print
        "Access Granted" and break the loop.
    - If the card is in the blocked list, print "Card Blocked" and continue to the next attempt.
5. The Else: If the user fails all 3 times, print "Police Notified."
"""

blocked_cards = {"1111", "2222", "3333"} # Using sets since card numbers are unique. Also note I have used strings!
number_of_attempts = 0

while number_of_attempts < 3:
    print(f"Number of attempts: {number_of_attempts}")
    card_number = input("Please enter a valid card number: ")
    if card_number not in blocked_cards and len(card_number) == 4 and card_number.isdigit():
        print("Access Granted")
        break
    else:
        print("Card Blocked")
        number_of_attempts += 1

if number_of_attempts == 3:
    print("Number of attempts exceeded, Police Notified")