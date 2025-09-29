from transaction import Transaction

class Account:
    def __init__(self, account_number, client):
        self.account_number = account_number
        self.client = client
        self.balance = 0.0
        self.transactions = []
        self.transaction_counter = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_counter += 1
            transaction = Transaction(self.transaction_counter, 'deposit', amount, self.account_number)
            self.transactions.append(transaction)
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_counter += 1
            transaction = Transaction(self.transaction_counter, 'withdrawal', amount, self.account_number)
            self.transactions.append(transaction)
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

    def __str__(self):
        return f"Account Number: {self.account_number}, Client: {self.client.name}, Balance: {self.balance}"