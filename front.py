from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import json

root = Tk()
root.geometry('1000x500')
root.title("Stonks 9000")

#Funkcje
def addExpense():

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    if fdata is None:
        fdata = []


    dt=data.get_date()
    str1=dt.strftime("%d-%m-%Y")
    try:
        c = int(cena.get())
        d = str1
        o = str(opis.get())

        expenses = {
            'ID': len(fdata) + 1,
            'Price': c,
            'Date': d,
            'Description': o
        }

        fdata.append(expenses)
        with open("expenses.json", "w") as file:
            file.write(json.dumps(fdata))

    except ValueError:
        win = Tk()
        win.geometry('250x50')
        win.title("Huh?")
        huh = Label(win, text="Co ty robisz?!", font=('Calibri', 16) , anchor=CENTER).pack()


def delExpense():

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    for i in fdata:
        selected = tabela.focus()
        temp = tabela.item(selected, 'values')
        ID_szukane = temp[0]
        if str(i['ID']) == ID_szukane:
            fdata.remove(i)


    with open("expenses.json", "w") as file:
        file.write(json.dumps(fdata))





def findExpense():
    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())







with open("expenses.json", "r") as file:
    dane = json.loads(file.read())






cols = ('ID', 'Cena', 'Data', 'Opis')
tabela = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    tabela.heading(col, text=col)
tabela.grid(row=4, column=0, columnspan=21)

for i in dane:
    tabela.insert("", "end", values=(i["ID"], i["Price"], i["Date"], i["Description"]))


#Przyciski
dodaj = Button(root, text="Dodaj",command = addExpense, padx=40,pady=20)
dodaj.grid(row=0,column=0)

usun = Button(root, text="Usuń",command = delExpense, padx=42,pady=20)
usun.grid(row=1,column=0)

edytuj = Button(root, text="Zmień", padx=39,pady=20)
edytuj.grid(row=2,column=0)

znajdz = Button(root, text="Znajdz", command = findExpense, padx=39,pady=20)
znajdz.grid(row=3,column=0)


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

opis = Entry(root, width = 50)
opis.grid(row=1, column= 3, padx=10,pady=10)

date_today = datetime.now()
data = DateEntry(root, selectmode='day', maxdate=date_today)
data.grid(row=2, column= 3)


root.mainloop()