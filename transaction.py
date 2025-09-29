from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, account_number):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type  # 'deposit' or 'withdrawal'
        self.amount = amount
        self.date = datetime.now()
        self.account_number = account_number

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Type: {self.transaction_type}, Amount: {self.amount}, Date: {self.date}, Account: {self.account_number}"