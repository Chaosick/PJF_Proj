import json

expenses = {
    "ID": None,
    "Price": None,
    "Date": None,
    "Description": None
}

with open("expenses.json", "r") as file:
    dane = json.loads(file.read())

print(expenses)