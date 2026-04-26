transactions = [
    {"date": "2024-02-01", "amount": 40, "location": "StoreA"},
    {"date": "2024-02-03", "amount": 45, "location": "StoreA"},
    {"date": "2024-02-05", "amount": 42, "location": "StoreB"}
]

customer_profile = {
    "typical_location": "StoreA",
    "average_amount": 43
}

new_transaction = {"date": "2024-02-10", "amount": 80, "location": "StoreB"}

is_suspicious = False

if new_transaction["location"] != customer_profile["typical_location"]:
    is_suspicious = True

if new_transaction["amount"] > customer_profile["average_amount"] + 20:
    is_suspicious = True


print(is_suspicious, transactions[0]["location"], customer_profile["typical_location"])
