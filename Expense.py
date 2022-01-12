import datetime
import sqlite3
import csv
import json


expenses = {
    "ID": None,
    "Price": None,
    "Date": None,
    "Description": None
}

with open("expenses.json", "r") as file:
    dane = json.loads(file.read())


def list_all_expenses():
    allExpenses = dane


def addExpense():
    for field in expenses:
        expenses[field] = input("Podaj wartosc dla {0} ".format(field))
    expenses.append(expenses)


def removeExpense():
    for i in range(len(dane)):
        if dane[i][expenses["ID"]] == id:
            dane.pop(i)



with open("expenses.json", "w") as file:
    file.write(json.dumps(expenses))




