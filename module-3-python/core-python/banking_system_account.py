print("Welcome to the Banking System")
# Hardcoded for simplicity
CORRECT_PIN = 0000
balance = 50000
account_holder = "Het Kakadiya"
account_number = "1234567890"

pin = int(input("Enter your PIN (4 digits): "))
if pin == CORRECT_PIN:
    print(f"Login successful!")
    print(f"Welcome to your account")
    print(f"{account_holder}")
    print(f"Account number: {account_number}")
    print(f"Balance: Rs {balance:,}")

    while True:
        print("\n1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Your balance is Rs {balance:,}")
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance")
            elif amount <= 0:
                print("Amount must be positive")
            else:
                balance -= amount
                print(f"Your new balance is Rs {balance:,}")
        elif choice == 3:
            amount = int(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive")
            else:
                balance += amount
                print(f"Your new balance is Rs {balance:,}")
        elif choice == 4:
            print("Thank you for using our banking system")
            break
        else:
            print("Invalid choice")
else:
    print("Login failed")

