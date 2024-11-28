import time

# ATM Simulation Program
print("Please insert your card")
time.sleep(3)

password = 1922  # PIN for authentication
balance = 5700  # Initial balance

# Ask for PIN
pin = int(input("Enter your ATM PIN: "))

if pin == password:
    while True:
        print("""
        1. Check Balance
        2. Withdraw Money
        3. Deposit Money
        4. Exit
        """)

        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid option.")
            continue

        if option == 1:
            print(f"Your current balance is ₹{balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter the amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient balance! Please try again.")
            elif withdraw_amount <= 0:
                print("Invalid amount! Please enter a positive value.")
            else:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount} has been debited from your account.")
                print(f"Your current balance is ₹{balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter the amount to deposit: "))
            if deposit_amount <= 0:
                print("Invalid amount! Please enter a positive value.")
            else:
                balance += deposit_amount
                print(f"₹{deposit_amount} has been credited to your account.")
                print(f"Your updated balance is ₹{balance}")

        elif option == 4:
            print("Thank you for using our ATM! Have a nice day.")
            break

        else:
            print("Invalid option! Please select a valid choice.")
else:
    print("Incorrect PIN. Please try again.")

