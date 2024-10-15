
Simple ATM System in Python

Project Description

This is a simple ATM system implemented in Python, which allows users to perform basic banking operations such as checking account balances, withdrawing money, and depositing funds. The system simulates a typical ATM machine with minimalistic functionality, focusing on user interaction through the command line.

Features

User login with PIN verification.

Check account balance.

Withdraw money (with checks for sufficient balance).

Deposit money.

Exit the system.


Technologies Used

Python: The core programming language for the project.


Prerequisites

Make sure you have the following installed before running the project:

Python 3.x: Install Python


Setup and Installation

1. Clone this repository:

git clone https://github.com/yourusername/atm-system-python.git


2. Navigate to the project directory:

cd atm-system-python


3. Run the main script:

python atm.py



Usage

1. When prompted, enter your user PIN to log in.


2. Follow the on-screen options to check balance, withdraw, or deposit money.


3. Enter exit or choose the exit option to terminate the session.



Example Interaction:

Welcome to the ATM System!
Please enter your PIN: ****
1. Check Balance
2. Withdraw
3. Deposit
4. Exit
Enter your choice: 1
Your current balance is $500.

Enter your choice: 2
Enter the amount to withdraw: $100
Withdrawal successful! Your new balance is $400.

Project Structure

├── atm.py                # Main script for the ATM system
├── README.md             # Project documentation
└── requirements.txt      # List of required dependencies (if any)

Future Improvements

Add user account creation functionality.

Include transaction history.

Implement an interface with a real database for user data storage.


License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributions




