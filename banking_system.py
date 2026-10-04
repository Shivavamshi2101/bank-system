import random
from datetime import datetime

# Store all bank accounts
accounts = {}


# -----------------------------------------
# CREATE ACCOUNT
# -----------------------------------------
def create_account():
    print("\n================================")
    print("         CREATE ACCOUNT")
    print("================================")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    # PIN validation
    while True:
        pin = input("Create a 4-digit PIN: ")

        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print("PIN must contain exactly 4 digits.")

    # Generate unique account number
    while True:
        account_number = str(random.randint(100000, 999999))

        if account_number not in accounts:
            break

    # Store account details
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Please remember your Account Number and PIN.")


# -----------------------------------------
# CHECK BALANCE
# -----------------------------------------
def check_balance(account):
    print("\n================================")
    print("          ACCOUNT BALANCE")
    print("================================")

    print("Account Holder:", account["name"])
    print("Current Balance: ₹", account["balance"])


# -----------------------------------------
# DEPOSIT MONEY
# -----------------------------------------
def deposit_money(account):
    print("\n================================")
    print("          DEPOSIT MONEY")
    print("================================")

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        account["balance"] += amount

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = (
            f"{current_time} - Deposited ₹{amount:.2f}"
        )

        account["transactions"].append(transaction)

        print("\nDeposit successful!")
        print("Deposited: ₹", amount)
        print("Current Balance: ₹", account["balance"])

    except ValueError:
        print("Please enter a valid amount.")


# -----------------------------------------
# WITHDRAW MONEY
# -----------------------------------------
def withdraw_money(account):
    print("\n================================")
    print("         WITHDRAW MONEY")
    print("================================")

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > account["balance"]:
            print("\nInsufficient balance!")
            print("Available Balance: ₹", account["balance"])
            return

        account["balance"] -= amount

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        transaction = (
            f"{current_time} - Withdrawn ₹{amount:.2f}"
        )

        account["transactions"].append(transaction)

        print("\nWithdrawal successful!")
        print("Withdrawn: ₹", amount)
        print("Current Balance: ₹", account["balance"])

    except ValueError:
        print("Please enter a valid amount.")


# -----------------------------------------
# TRANSFER MONEY
# -----------------------------------------
def transfer_money(account_number):
    print("\n================================")
    print("         TRANSFER MONEY")
    print("================================")

    receiver_account = input("Enter receiver account number: ")

    # Check receiver account
    if receiver_account not in accounts:
        print("\nReceiver account not found!")
        return

    # Prevent transfer to same account
    if receiver_account == account_number:
        print("\nYou cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter transfer amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        sender = accounts[account_number]
        receiver = accounts[receiver_account]

        # Check sender balance
        if amount > sender["balance"]:
            print("\nInsufficient balance!")
            print("Available Balance: ₹", sender["balance"])
            return

        # Transfer money
        sender["balance"] -= amount
        receiver["balance"] += amount

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Sender transaction
        sender_transaction = (
            f"{current_time} - Transferred ₹{amount:.2f} "
            f"to Account {receiver_account}"
        )

        # Receiver transaction
        receiver_transaction = (
            f"{current_time} - Received ₹{amount:.2f} "
            f"from Account {account_number}"
        )

        sender["transactions"].append(sender_transaction)
        receiver["transactions"].append(receiver_transaction)

        print("\nTransfer successful!")
        print("Transferred: ₹", amount)
        print("To Account:", receiver_account)
        print("Current Balance: ₹", sender["balance"])

    except ValueError:
        print("Please enter a valid amount.")


# -----------------------------------------
# TRANSACTION HISTORY
# -----------------------------------------
def transaction_history(account):
    print("\n================================")
    print("       TRANSACTION HISTORY")
    print("================================")

    transactions = account["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")
        return

    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction}")


# -----------------------------------------
# CHANGE PIN
# -----------------------------------------
def change_pin(account):
    print("\n================================")
    print("           CHANGE PIN")
    print("================================")

    old_pin = input("Enter your current PIN: ")

    if old_pin != account["pin"]:
        print("\nIncorrect current PIN!")
        return

    while True:
        new_pin = input("Enter your new 4-digit PIN: ")

        if new_pin.isdigit() and len(new_pin) == 4:
            break

        print("PIN must contain exactly 4 digits.")

    confirm_pin = input("Confirm your new PIN: ")

    if new_pin != confirm_pin:
        print("\nPINs do not match!")
        return

    account["pin"] = new_pin

    print("\nPIN changed successfully!")


# -----------------------------------------
# ACCOUNT MENU
# -----------------------------------------
def account_menu(account_number):
    account = accounts[account_number]

    while True:
        print("\n================================")
        print("          ACCOUNT MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account)

        elif choice == "2":
            deposit_money(account)

        elif choice == "3":
            withdraw_money(account)

        elif choice == "4":
            transfer_money(account_number)

        elif choice == "5":
            transaction_history(account)

        elif choice == "6":
            change_pin(account)

        elif choice == "7":
            print("\nLogged out successfully!")
            break

        else:
            print("\nInvalid choice! Please select 1-7.")


# -----------------------------------------
# LOGIN
# -----------------------------------------
def login():
    print("\n================================")
    print("             LOGIN")
    print("================================")

    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if account_number not in accounts:
        print("\nAccount not found!")
        return

    account = accounts[account_number]

    if account["pin"] != pin:
        print("\nIncorrect PIN!")
        return

    print("\nLogin successful!")
    print("Welcome,", account["name"])

    account_menu(account_number)


# -----------------------------------------
# MAIN MENU
# -----------------------------------------
def main():
    while True:
        print("\n================================")
        print("        BANKING SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank you for using Banking System!")
            print("Have a great day!")
            break

        else:
            print("\nInvalid choice! Please select 1-3.")


# -----------------------------------------
# START PROGRAM
# -----------------------------------------
if __name__ == "__main__":
    main()