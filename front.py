from tkinter import *
import json

root = Tk()
root.geometry('1000x500')
root.title("Expenses Traker 9000")

with open("expenses.json", "r") as file:
    dane = json.loads(file.read())

#Funkcje
def addExpense():

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    if fdata is None:
        fdata = []

    expenses = {
        'ID': len(fdata),
        'Price': cena.get(),
        'Date': data.get(),
        'Description': opis.get()
    }

    fdata.append(expenses)
    with open("expenses.json", "w") as file:
        file.write(json.dumps(fdata))


def delExpense(id):

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    for i in fdata:
        if i['ID'] == id:
            fdata.remove(i)

    with open("expenses.json", "w") as file:
        file.write(json.dumps(fdata))

def editExpense(id):

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    for i in fdata:
        if i['ID'] == id:
        expenses = {
            'ID': id,
            'Price': cena.get(),
            'Date': data.get(),
            'Description': opis.get()
        }

    with open("expenses.json", "w") as file:
        file.write(json.dumps(fdata))

#Przyciski
dodaj = Button(root, text="Dodaj",command = addExpense, padx=40,pady=20)
dodaj.grid(row=0,column=0)

usun = Button(root, text="Usuń",command = lambda: delExpense(1), padx=42,pady=20)
usun.grid(row=1,column=0)

edytuj = Button(root, text="Zmień", padx=39,pady=20)
edytuj.grid(row=2,column=0)


#Text
c = Label(root,text = "Wartość")
c.grid(row=0, column= 2)

o = Label(root,text = "Opis")
o.grid(row=1, column= 2)

d = Label(root,text = "Data")
d.grid(row=2, column= 2)


#Pola do wpisywania
cena = Entry(root, width = 50)
cena.grid(row=0, column= 3, padx=10,pady=10)

data = Entry(root, width= 50)
data.grid(row=1, column= 3, padx=10,pady=10)

opis = Entry(root, width = 50)
opis.grid(row=2, column= 3, padx=10,pady=10)



root.mainloop()