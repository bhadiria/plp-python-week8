
# Banking Management Toolkit
# This program allows users to manage a simple bank account.

accounts = []


# Tool 1: Create an account and store it in the accounts list.
def create_account():
    if accounts:
        print("You already have an account. Please use the other tools.")
        return

    name = input("Enter your full name: ").strip()

    if not name:
        print("Your name cannot be empty. Please try again.")
        return

    account = {
        "name": name,
        "balance": 0.0
    }

    accounts.append(account)
    print(f"Congratulations, {name}! Your account has been created.")


# Tool 2: Deposit money into the existing account.
def deposit_money():
    if not accounts:
        print("Please create an account first.")
        return

    try:
        amount = float(input("Enter the amount to deposit: "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            accounts[0]["balance"] += amount
            print(
                f"Deposit successful! Your new balance is "
                f"KSh {accounts[0]['balance']:.2f}."
            )
    except ValueError:
        print("Invalid amount. Please enter a number.")


# Tool 3: Withdraw money without allowing an overdraft.
def withdraw_money():
    if not accounts:
        print("Please create an account first.")
        return

    try:
        amount = float(input("Enter the amount to withdraw: "))
        balance = accounts[0]["balance"]

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > balance:
            print(f"Insufficient funds. Your balance is KSh {balance:.2f}.")
        else:
            accounts[0]["balance"] -= amount
            print(
                f"Withdrawal successful! Your new balance is "
                f"KSh {accounts[0]['balance']:.2f}."
            )
    except ValueError:
        print("Invalid amount. Please enter a number.")


# Tool 4: Display the account holder's current balance.
def check_balance():
    if not accounts:
        print("Please create an account first.")
        return

    name = accounts[0]["name"]
    balance = accounts[0]["balance"]

    print(f"Account holder: {name}")
    print(f"Current balance: KSh {balance:.2f}")


# Main menu: repeat until the user chooses Exit.
def main():
    print("Welcome to the Banking Management Toolkit!")

    while True:
        print("\nPlease choose an option:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using our banking toolkit. Goodbye!")
            break
        else:
            print(
                f"Sorry, '{choice}' is not a valid choice. "
                "Please select a number from 1 to 5."
            )


# Start the program.
if __name__ == "__main__":
    main()
