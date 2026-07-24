while True:
    print("\n===== Calculator =====")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")

    try:
        choice = int(input("Enter choice (1-4): "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")

    again = input("\nDo you want to perform another calculation? (y/n): ").lower()
    if again != 'y':
        print("Thank you for using the calculator!")
        break

    