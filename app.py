from flask import Flask, render_template, request, redirect, url_for
from client import Client
from account import Account

app = Flask(__name__)

clients = []
accounts = []
client_counter = 0
account_counter = 1000

@app.route('/')
def index():
    return render_template('index.html', clients=clients, accounts=accounts)

@app.route('/create_client', methods=['GET', 'POST'])
def create_client():
    if request.method == 'POST':
        global client_counter
        client_counter += 1
        name = request.form['name']
        email = request.form['email']
        client = Client(client_counter, name, email)
        clients.append(client)
        return redirect(url_for('index'))
    return render_template('create_client.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        global account_counter
        account_counter += 1
        client_id = int(request.form['client_id'])
        client = next((c for c in clients if c.client_id == client_id), None)
        if client:
            account = Account(account_counter, client)
            accounts.append(account)
        return redirect(url_for('index'))
    return render_template('create_account.html', clients=clients)

@app.route('/deposit/<int:account_number>', methods=['GET', 'POST'])
def deposit(account_number):
    account = next((a for a in accounts if a.account_number == account_number), None)
    if not account:
        return "Account not found", 404
    if request.method == 'POST':
        amount = float(request.form['amount'])
        account.deposit(amount)
        return redirect(url_for('index'))
    return render_template('transaction.html', account=account, action='deposit')

@app.route('/withdraw/<int:account_number>', methods=['GET', 'POST'])
def withdraw(account_number):
    account = next((a for a in accounts if a.account_number == account_number), None)
    if not account:
        return "Account not found", 404
    if request.method == 'POST':
        amount = float(request.form['amount'])
        account.withdraw(amount)
        return redirect(url_for('index'))
    return render_template('transaction.html', account=account, action='withdraw')

@app.route('/transactions/<int:account_number>')
def transactions(account_number):
    account = next((a for a in accounts if a.account_number == account_number), None)
    if not account:
        return "Account not found", 404
    return render_template('transactions.html', account=account)

if __name__ == '__main__':
    app.run(debug=True)