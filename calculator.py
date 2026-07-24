while True:
    print("Select operation:")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 for exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Exiting calculator.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter a number from 1 to 5.\n")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
        continue

    if choice == "1":
        print(f"Result: {a + b}\n")
    elif choice == "2":
        print(f"Result: {a - b}\n")
    elif choice == "3":
        print(f"Result: {a * b}\n")
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero.\n")
        else:
            print(f"Result: {a / b}\n")
