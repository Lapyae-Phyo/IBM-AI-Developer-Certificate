# Import libraries
from flask import Flask, render_template, request, url_for, redirect

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': float(100)},
    {'id': 2, 'date': '2023-06-02', 'amount': float(-200)},
    {'id': 3, 'date': '2023-06-03', 'amount': float(300)}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Display add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":

        # Create a new transaction obiect using form field values
        date = request.form.get("date")
        amount = float(request.form.get("amount"))

        transaction = {
            "id": len(transactions)+1,
            "date": date,
            "amount": amount
        }

        # Append the new transaction to the list
        transactions.append(transaction)

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))

    # Render the form template to display the add translation form
    return render_template("form.html")

# Update operation: Display edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        # Extract the update values from the form fields
        date = request.form.get("date")
        amount = float(request.form.get("amount"))

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = date
                transaction["amount"] = amount
                break

        # Redirect to the transactions list page
        return redirect(url_for("get_transactions"))

    # Find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return render_template("edit.html", transaction=transaction)


# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            break

    # Redirect to the transaction list page
    return redirect(url_for("get_transactions"))

# Search operation
@app.route("/search", methods=["GET","POST"])
def search_transaction():
    if request.method == "POST":
        min_amount = float(request.form.get("min_amount"))
        max_amount = float(request.form.get("max_amount"))

        filter_transactions = [transaction for transaction in transactions if min_amount <= transaction["amount"] <= max_amount]
        return render_template("transactions.html", transactions=filter_transactions)

    return render_template("search.html")

#Total balance
@app.route("/balance")
def total_balance():
    total = 0
    for transaction in transactions:
        total += transaction["amount"]

    return render_template("transactions.html", transactions=transactions, total_balance=f"Total balance: {total}")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
