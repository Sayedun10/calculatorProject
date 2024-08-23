# Define functions for basic arithmetic operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # Ensure we do not divide by zero
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Display the menu of operations
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


# Get user input for the operation and numbers
def get_user_input():
    while True:
        # Display the menu
        display_menu()

        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            # Get the numbers from the user
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            # Return the choice and the numbers
            return choice, num1, num2
        else:
            print("Invalid input. Please select a valid operation.")


# Perform the calculation based on user's choice
def calculate(choice, num1, num2):
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")


# Main loop for the calculator
def main():
    while True:
        # Get user input
        choice, num1, num2 = get_user_input()

        # Perform the calculation
        calculate(choice, num1, num2)

        # Ask if the user wants to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break


# Run the calculator
main()
