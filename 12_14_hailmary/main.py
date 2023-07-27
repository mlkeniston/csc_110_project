# Dictionaries for the functions to pull products and prices from #

no_prime_member_price = {
    "Kindle Paperwhite": 129.99,
    "Echo Dot": 39.99,
    "Fire TV Stick": 39.99,
    "Alexa Smart Plug": 24.99,
    "Fire Tablet": 49.99,
    "Echo Show 8": 129.99,
    "Ring Doorbell": 99.99,
    "Echo Flex": 24.99,
    "Echo Auto": 49.99,
    "Fire TV Stick Lite": 29.99,
    "Fire TV Cube": 119.99,
    "Apple Airpods": 159.99,
    "Instant Pot": 99.99,
    "Apple Watch": 199.99,
    "Fitbit Charge 4": 149.99,
    "Bose Headphones": 199.99,
    "Keurig Coffee Maker": 99.99,
    "Shark Vacuum": 199.99,
    "Samsung TV": 399.99,
    "Fujifilm Camera": 499.99,
    "KitchenAid Mixer": 199.99,
}
prime_member_price = {
    "Kindle Paperwhite": 119.99,
    "Echo Dot": 34.99,
    "Fire TV Stick": 34.99,
    "Alexa Smart Plug": 19.99,
    "Fire Tablet": 39.99,
    "Echo Show 8": 119.99,
    "Ring Doorbell": 89.99,
    "Echo Flex": 19.99,
    "Echo Auto": 39.99,
    "Fire TV Stick Lite": 24.99,
    "Fire TV Cube": 99.99,
    "Apple Airpods": 139.99,
    "Instant Pot": 79.99,
    "Apple Watch": 179.99,
    "Fitbit Charge 4": 129.99,
    "Bose Headphones": 179.99,
    "Keurig Coffee Maker": 79.99,
    "Shark Vacuum": 179.99,
    "Samsung TV": 279.99,
    "Fujifilm Camera": 469.99,
    "KitchenAid Mixer": 179.99,
}

# Displays the options of products that you can type #
user_list = {}
print("Your Amazon product options are:")
print(", ".join(no_prime_member_price.keys()))
print("Enter an item to add to your list. Type 'done' when finished.")
while True:
    user_selection = input()
    # Moves on to next function if you type done #
    if user_selection.lower() == "done":
        break
    # Asks for quantity #
    if user_selection in no_prime_member_price and user_selection in prime_member_price:
        print("\nHow many would you like to add to your list?")
        user_quantity = input()
        if user_quantity.isnumeric() and (int(user_quantity) > 0):
            user_list[user_selection] = int(user_quantity)
        else:
            print("Number not recognized. Try again.")
    else:
        print("Invalid product. Try again.")
#Shows list of items and asks if you are a prime member to pull from either of the two different dictionaries#

print("\nHere is your list:")
print(user_list)
print("Are you a Prime member? Type 'yes' or 'no'.")
#Subtotal is a constant at zero, which gets different prices added to it to calculate the total#
user_input = input()
if user_input.lower() == "yes" or user_input.lower() == "no":
    is_prime_member = user_input.lower() == "yes"
    subtotal = 0
#If you type no to being a prime member, it will calculate how much you could have saved and convert it to a string#
    for item, quantity in user_list.items():
        if is_prime_member:
            subtotal += prime_member_price[item] * quantity
        else:
            savings = 0
            savings += (no_prime_member_price[item] - prime_member_price[item]) * quantity
            savings = round(savings, 2)
            print("You would have saved $" + str(savings) + " on shipping if you were a Prime member.")
            subtotal += no_prime_member_price[item] * quantity
#Total is calculated by multiplying the subtotal by 8%, and adding it back to the subtotal#
    tax = subtotal * 0.08
    total = subtotal + tax
    total = round(total, 2)
    print("Subtotal: $" + str(subtotal))
    print("Total (including tax): $" + str(total))
else:
    print("Invalid input. Please try again.")