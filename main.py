from client import Client
from account import Account

def main():
    # Create clients
    client1 = Client(1, "Juan Perez", "juan@example.com")
    client2 = Client(2, "Maria Lopez", "maria@example.com")

    print("Clients created:")
    print(client1)
    print(client2)
    print()

    # Create accounts
    account1 = Account(1001, client1)
    account2 = Account(1002, client2)

    print("Accounts created:")
    print(account1)
    print(account2)
    print()

    # Perform transactions
    print("Performing transactions:")
    account1.deposit(500)
    print(f"Deposit 500 to account {account1.account_number}. Balance: {account1.get_balance()}")

    account1.withdraw(200)
    print(f"Withdraw 200 from account {account1.account_number}. Balance: {account1.get_balance()}")

    account2.deposit(1000)
    print(f"Deposit 1000 to account {account2.account_number}. Balance: {account2.get_balance()}")

    account2.withdraw(150)
    print(f"Withdraw 150 from account {account2.account_number}. Balance: {account2.get_balance()}")
    print()

    # Show transaction history
    print("Transaction history for account 1001:")
    for transaction in account1.get_transaction_history():
        print(transaction)

    print("\nTransaction history for account 1002:")
    for transaction in account2.get_transaction_history():
        print(transaction)

if __name__ == "__main__":
    main()