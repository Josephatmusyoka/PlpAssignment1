# Advanced Calculator Program

def calculator():
    while True:
        print("\nSimple Python Calculator")
        print("Available operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (**)")
        print("7. Exit")

        # Get user choice
        choice = input("Choose an operation (1-7): ")

        if choice == "7":
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop

        # Get user input for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue  # Restart the loop

        # Perform the chosen operation
        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        elif choice == "5":
            if num2 == 0:
                print("Error: Modulus by zero is not allowed.")
            else:
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
        elif choice == "6":
            result = num1 ** num2
            print(f"{num1} ** {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
calculator()
