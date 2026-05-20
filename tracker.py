to_do_list = []

def input_amount(prompt, *args, **kwargs):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def add_expense(amount=None, description=None, *args, **kwargs):
    """Add an expense with optional args/kwargs or prompt for input."""
    if amount is None:
        amount = input_amount("Enter expense amount: ")
    if description is None:
        description = input("Enter description (what is it for?): ").strip() or "No description"
    status = kwargs.get('status', 'pending')
    to_do_list.append({
        'type': 'expense',
        'amount': float(amount),
        'description': description,
        'status': status
    })
    print("New expense added successfully.")

def add_income(amount=None, description=None, *args, **kwargs):
    """Add an income with optional args/kwargs or prompt for input."""
    if amount is None:
        amount = input_amount("Enter income amount: ")
    if description is None:
        description = input("Enter description: ").strip() or "No description"
    status = kwargs.get('status', 'pending')
    to_do_list.append({
        'type': 'income',
        'amount': float(amount),
        'description': description,
        'status': status
    })
    print("New income added successfully.")

def view_transaction(*args, **kwargs):
    """View transactions with optional kwargs support."""
    print("Your Transaction List:")
    if not to_do_list:
        print("No transactions in the list.")
    else:
        for index, t in enumerate(to_do_list, start=1):
            print(f"{index}: [{t['type']}] {t['description']} - ${t['amount']:.2f} - {t['status']}")
    print("\n")

def view_summary(transactions=None, *args, **kwargs):
    """View a summary of transactions with optional transactions list."""
    transactions = transactions if transactions is not None else to_do_list
    if not transactions:
        print("No transactions to summarize.")
        return
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    balance = total_income - total_expenses

    print("Transaction Summary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

def remove_transaction(transaction_number=None, *args, **kwargs):
    """Remove a transaction by number or prompt the user."""
    if not to_do_list:
        print("List IS Empty.")
        return
    if transaction_number is None:
        try:
            transaction_number = int(input("Enter the transaction number that you want to remove: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        transaction_number = int(transaction_number) - 1

    if 0 <= transaction_number < len(to_do_list):
        removed = to_do_list.pop(transaction_number)
        print(f"Transaction removed successfully: {removed['description']}.")
    else:
        print("Invalid transaction number.")


def mark_done(transaction_number=None, *args, **kwargs):
    """Mark a transaction as done by number or prompt the user."""
    if not to_do_list:
        print("No transactions in the list.")
        return
    if transaction_number is None:
        try:
            transaction_number = int(input("Enter the number of the transaction to mark as done: ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        transaction_number = int(transaction_number) - 1

    if 0 <= transaction_number < len(to_do_list):
        to_do_list[transaction_number]['status'] = kwargs.get('status', 'done')
        print(f"Transaction '{to_do_list[transaction_number]['description']}' marked as done.")
    else:
        print("Invalid transaction number.")


def menu():
    while True:
        print("=== Responsive Budget Tracker ===")
        print("1. Add expense")
        print("2. Add income")
        print("3. View transactions")
        print("4. View summary")
        print("5. Remove a transaction")
        print("6. Mark transaction as done")
        print("7. Exit")

        choice = input("Please enter a choice(1-7): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            add_income()
        elif choice == '3':
            view_transaction()
        elif choice == '4':
            view_summary()
        elif choice == '5':
            remove_transaction()
        elif choice == '6':
            mark_done()
        elif choice == '7':
            print("Exiting the Application... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
