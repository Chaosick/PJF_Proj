from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import json

root = Tk()
root.geometry('800x550')
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
        c = float(cena.get())
        d = str1
        o = str(opis.get())
        i = len(fdata)+1

        expenses = {
            'ID': i,
            'Price': c,
            'Date': d,
            'Description': o
        }

        fdata.append(expenses)
        tabela.insert(parent='', index='end', values=(i,c,d,o))

        cena.delete(0, END)
        opis.delete(0, END)

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
            tabela.delete(selected)

    with open("expenses.json", "w") as file:
        file.write(json.dumps(fdata))


def findExpense():
    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    dt=data.get_date()
    str1=dt.strftime("%d-%m-%Y")


    win1 = Tk()
    win1.geometry('800x200')
    win1.title("Zakupione w danym dniu")

    cols = ('ID', 'Cena', 'Data', 'Opis')
    find_tabela = ttk.Treeview(win1, columns=cols, show='headings')
    for col in cols:
        find_tabela.heading(col, text=col)
    find_tabela.grid(row=0, column=0)

    for i in fdata:
        if str(i['Date']) == str1:
            find_tabela.insert(parent='', index='end', values=(i["ID"], i["Price"], i["Date"], i["Description"]))


def editExpense():

    try:
        cena.delete(0, END)
        opis.delete(0, END)

        selected = tabela.focus()
        info = tabela.item(selected, 'values')

        cena.insert(0,info[1])
        opis.insert(0,info[3])

        zatwierdz["state"] = NORMAL

    except IndexError:
        win = Tk()
        win.geometry('250x50')
        win.title("Huh?")
        huh = Label(win, text="Co ty robisz?!", font=('Calibri', 16) , anchor=CENTER).pack()


def zapisz():
    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())

    dt = data.get_date()
    str1 = dt.strftime("%d-%m-%Y")

    selected = tabela.focus()
    values = tabela.item(selected, 'values')
    ID_szukane = values[0]

    for i in fdata:
       if str(i['ID']) == ID_szukane:
           i['Price'] = cena.get()
           i['Description'] = opis.get()
           i['Date'] = str1

    cena.delete(0, END)
    opis.delete(0, END)
    zatwierdz["state"] = DISABLED

    with open("expenses.json", "w") as file:
       file.write(json.dumps(fdata))


def graphCreate():

    with open("expenses.json", "r") as file:
        fdata = json.loads(file.read())
    
    sum=0
    iter = 0
    wartosc = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    while iter <= 12:
        for i in fdata:
            if str(i['Date'][3:5]) == str(iter).zfill(2):
                wartosc[iter] += i['Price']
        iter+=1

    dni=np.arange(0,13)
    plt.title("Wykres wydatków")
    plt.xlabel("Miesiące")
    plt.ylabel("Kwota")
    plt.plot(dni,wartosc,marker = "o",color="green")
    plt.show()
#=================================================================================================================

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

znajdz = Button(root, text="Znajdz", command = findExpense, padx=38,pady=20)
znajdz.grid(row=2,column=0)

edytuj = Button(root, text="Zmień", command = editExpense, padx=39,pady=20)
edytuj.grid(row=3,column=0)

zatwierdz = Button(root, text="Zatwierdz",state = DISABLED, command = zapisz, padx=40, pady=20)
zatwierdz.grid(row=3, column=1)

wykres = Button(root, text="Wykres", command = graphCreate, padx = 100, pady = 20)
wykres.grid(row=5, column = 0, columnspan = 20)


#Text
c = Label(root,text = "Wartość")
c.grid(row=0, column= 1)

o = Label(root,text = "Opis")
o.grid(row=1, column= 1)

d = Label(root,text = "Data")
d.grid(row=2, column= 1)


#Pola do wpisywania
cena = Entry(root, width = 50)
cena.grid(row=0, column= 2, padx=10,pady=10)

opis = Entry(root, width = 50)
opis.grid(row=1, column= 2, padx=10,pady=10)

date_today = datetime.now()
data = DateEntry(root, selectmode='day', maxdate=date_today)
data.grid(row=2, column= 2)


root.mainloop()