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

def okienko():
    window = Toplevel()
    window.geometry("200x80")

    tekst_id = Label(window, text="Podaj ID: ").grid(row = 0, column = 0)
    pole_id = Entry(window, width=10).grid(row=0, column=1, padx=20, pady=10)

    zatwierdz = Button(window, text="Zatwierdz")
    zatwierdz.grid(row=1, column=0, padx=10,pady=10)

    koniec = Button(window, text="Zamknij", command = window.destroy)
    koniec.grid(row=1, column=1, padx=10, pady=10)