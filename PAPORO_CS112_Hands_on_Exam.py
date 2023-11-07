# Define a function to convert a decimal number to binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)


# Define a function to convert a decimal number to octal
def decimal_to_octal(decimal_num):
    return oct(decimal_num)


# Define a function to convert a decimal number to hexadecimal
def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)


# Start an infinite loop to keep the program running
while True:
    try:
        # Ask the user to select a conversion option
        user_choice = int(input(
            "Enter 1 to convert to binary, 2 to convert to octal, 3 to convert to hexadecimal, or any other key to exit: "))

        # Check if the user's choice is 1, 2, or 3
        if user_choice in (1, 2, 3):
            # Prompt the user to enter a decimal number
            decimal_num = int(input("Enter a decimal number: "))

            # Perform the selected conversion based on the user's choice
            if user_choice == 1:
                print(f"Binary: {decimal_to_binary(decimal_num)}")
            elif user_choice == 2:
                print(f"Octal: {decimal_to_octal(decimal_num)}")
            elif user_choice == 3:
                print(f"Hexadecimal: {decimal_to_hexadecimal(decimal_num)}")
        else:
            # If the user enters an invalid option, display an error message
            print("Invalid input. Please try again.")
    except ValueError:
        # Handle exceptions if the user enters non-integer input
        print("Invalid input. Please try again.")1