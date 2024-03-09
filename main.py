from calculator import Calculator

def main():
    calculator = Calculator()

    while True:
        try:
            print("Choose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Clear history")
            print("6. Exit")

            choice = int(input("Enter choice: "))

            if choice == 6:
                print("Exiting...")
                break

            if choice not in range(1, 7):
                print("Invalid choice. Please choose a number between 1 and 6.")
                continue

            a = Decimal(input("Enter first number: "))
            b = Decimal(input("Enter second number: "))

            if choice == 1:
                result = calculator.add(a, b)
            elif choice == 2:
                result = calculator.subtract(a, b)
            elif choice == 3:
                result = calculator.multiply(a, b)
            elif choice == 4:
                result = calculator.divide(a, b)
            
            print("Result:", result)

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
