
# Banking Management Toolkit

## Project Description

The Banking Management Toolkit is a Python command-line application that allows users to create a bank account, deposit money, withdraw money, and check their account balance. It uses a menu that repeats until the user chooses to exit.

## Features

- Create a bank account.
- Deposit money into an account.
- Withdraw money when sufficient funds are available.
- Check the current account balance.
- Handle invalid menu choices and invalid numeric input.
- Display friendly messages and formatted balances.

## Technologies Used

- Python 3
- Lists and dictionaries
- Functions
- While loops
- Conditional statements
- F-strings
- Exception handling

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the command:

      bash
   python toolkit.py

5. Follow the numbered menu to use the banking tools.

On Windows, you can also run `py toolkit.py`.

## Screenshots

The `screenshots/` folder contains screenshots showing the menu, invalid menu choice handling, account creation, deposits, withdrawals, balance checking, and exiting the program.

## Reflection

The hardest part of this project was connecting all the banking tools to one menu while keeping the program easy to understand. The bug that took the longest to fix was handling invalid input without allowing the program to crash. I addressed this by using `try` and `except` when converting amounts into numbers. I also used conditionals to prevent deposits or withdrawals with invalid amounts and withdrawals that exceed the available balance. The project helped me understand how loops, lists, functions, and f-strings work together in Python. If I had one more week, I would add account numbers, support multiple accounts, and save account information to a file. I would also improve security and add transaction history.

## Limitations

This is an educational project, not a real banking system. Account information is stored only while the program is running and is not saved securely.
