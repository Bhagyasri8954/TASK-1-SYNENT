import math
import datetime

HISTORY_FILE = "history.txt"

def save_to_history(entry):
    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            print("\n=== Calculation History ===")
            print(file.read())
    except FileNotFoundError:
        print("No history found.")

def calculator():
    while True:
        print("\n========== CLI CALCULATOR ==========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (^)")
        print("7. Square Root (√)")
        print("8. View History")
        print("9. Clear History")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '10':
            print("Goodbye!")
            break

        elif choice == '8':
            show_history()
            continue

        elif choice == '9':
            open(HISTORY_FILE, "w").close()
            print("History cleared.")
            continue

        if choice not in [str(i) for i in range(1, 8)]:
            print("Invalid choice!")
            continue

        try:
            if choice == '7':  # Square root
                num = float(input("Enter number: "))
                if num < 0:
                    print("Cannot take square root of negative number!")
                    continue
                result = math.sqrt(num)
                operation = f"√{num} = {result}"

            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = num1 + num2
                    operation = f"{num1} + {num2} = {result}"

                elif choice == '2':
                    result = num1 - num2
                    operation = f"{num1} - {num2} = {result}"

                elif choice == '3':
                    result = num1 * num2
                    operation = f"{num1} * {num2} = {result}"

                elif choice == '4':
                    if num2 == 0:
                        print("Division by zero not allowed!")
                        continue
                    result = num1 / num2
                    operation = f"{num1} / {num2} = {result}"

                elif choice == '5':
                    if num2 == 0:
                        print("Modulus by zero not allowed!")
                        continue
                    result = num1 % num2
                    operation = f"{num1} % {num2} = {result}"

                elif choice == '6':
                    result = num1 ** num2
                    operation = f"{num1} ^ {num2} = {result}"

            print("Result:", result)

            # Save with timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_to_history(f"[{timestamp}] {operation}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Run program
calculator()