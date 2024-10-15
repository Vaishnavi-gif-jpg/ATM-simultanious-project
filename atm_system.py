import json

# Load data from JSON file
def load_data():
    try:
        with open('atm_data.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save data to JSON file
def save_data(data):
    with open('atm_data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Authenticate user
def authenticate_user(pin):
    data = load_data()
    return pin in data

# Check balance
def check_balance(pin):
    data = load_data()
    return data[pin]['balance']

# Deposit funds
def deposit(pin, amount):
    data = load_data()
    if amount > 0:
        data[pin]['balance'] += amount
        log_transaction(pin, amount, 'deposit')
        save_data(data)
        return data[pin]['balance']
    else:
        raise ValueError("Invalid deposit amount.")

# Withdraw funds
def withdraw(pin, amount):
    data = load_data()
    if amount > 0 and amount <= data[pin]['balance']:
        data[pin]['balance'] -= amount
        log_transaction(pin, amount, 'withdraw')
        save_data(data)
        return data[pin]['balance']
    else:
        raise ValueError("Invalid withdrawal amount or insufficient funds.")

# Log transaction
def log_transaction(pin, amount, transaction_type):
    data = load_data()
    transaction = {
        "type": transaction_type,
        "amount": amount
    }
    data[pin]['transactions'].append(transaction)
    save_data(data)

# User registration
def register_user(pin, name):
    data = load_data()
    if pin in data:
        raise ValueError("This PIN is already registered.")
    data[pin] = {
        "name": name,
        "balance": 0,
        "transactions": []
    }
    save_data(data)

# Show transaction history
def show_transaction_history(pin):
    data = load_data()
    transactions = data[pin]['transactions']
    if transactions:
        print("\nTransaction History:")
        for txn in transactions:
            print(f"{txn['type'].capitalize()}: ${txn['amount']:.2f}")
    else:
        print("No transactions found.")

# ATM operations
def atm_operations(pin):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                balance = check_balance(pin)
                print(f"Your current balance is: ${balance:.2f}")

            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                new_balance = deposit(pin, amount)
                print(f"New balance after deposit: ${new_balance:.2f}")

            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                new_balance = withdraw(pin, amount)
                print(f"New balance after withdrawal: ${new_balance:.2f}")

            elif choice == '4':
                show_transaction_history(pin)

            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")

# Main function
def main():
    print("Welcome to the ATM System")
    print("1. Login")
    print("2. Register")
    choice = input("Choose an option: ")

    if choice == '1':
        pin = input("Please enter your PIN: ")
        if authenticate_user(pin):
            print("Authentication successful!")
            atm_operations(pin)
        else:
            print("Invalid PIN. Please try again.")

    elif choice == '2':
        pin = input("Enter a new PIN: ")
        name = input("Enter your name: ")
        try:
            register_user(pin, name)
            print("Registration successful! You can now log in.")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice. Please try again.")

if '_name_'== "_main_":
    main()