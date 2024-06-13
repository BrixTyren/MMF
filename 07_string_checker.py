# check that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_response):

    error = "Please choose {} or {}".format(valid_response[0],
                                            valid_response[1])

    while True:

        response = input(question).lower()

        for item in valid_response:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Ask user if they want to see the instructions
for cash in range(0, 5):
    want_instructions = string_checker("Do you want to read the"
                                       "instructions (y/n): ",
                                       1, yes_no_list)
    print("You chose", want_instructions)

# Ask user to choose a payment method
for case in range(0, 5):
    payment_method = string_checker("Choose a "
                                    "payment method (cash / credit): ",
                                    2, payment_list)
    print("You chose", payment_method)
