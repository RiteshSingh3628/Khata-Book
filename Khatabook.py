import sqlite3, time
from tkinter import *


# connection to sql
def connection():
    try:
        conn = sqlite3.connect("book.db")
    except:
        print("+++++++CANNOT CONNECT TO DATABASE++++++++")
    return conn


def submit_data():
    n = name.get()
    l = lastname.get()
    p = phone.get()
    a = address.get()
    am = amount.get()
    conn = connection()
    cur = conn.cursor()
    note = "no"
    n_strip = n.strip()
    l_strip = l.strip()
    if n == "":
        Label(f1, text="<PLEASE ENTER NAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=150)
    elif l == "":
        Label(f1, text="<PLEASE ENTER LASTNAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=220)
    elif p == "" or len(p) < 10 or len(p) > 10:
        Label(f1, text="<PLEASE ENTER PHONE.NO>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=290)
    elif a == "":
        Label(f1, text="<PLEASE ENTER ADDRESS>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=370)
    elif am == "":
        Label(f1, text="<PLEASE ENTER AMOUNT>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=440)
    elif cur.execute("SELECT * FROM khatabook1 WHERE COSTUMER_NAME = ? AND COSTUMER_LASTNAME =?",
                     (n_strip.upper(), l_strip.upper())).fetchone():
        note = "yes"
        Label(f1, text="NAME ALREADY EXISTS", font="Arial 16 bold", fg="green").place(x=200, y=600)
        name.set("")
        lastname.set("")
        phone.set("")
        address.set("")
        amount.set("")

    else:
        if note == "no":
            conn = connection()
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS khatabook1( COSTUMER_NAME TEXT ,COSTUMER_LASTNAME TEXT ,PHONE INTEGER,ADDRESS TEXT,AMOUNT INTEGER )")
            cur.execute("insert into khatabook1 values(?,?,?,?,?)",
                        (n_strip.upper(), l_strip.upper(), int(p), a.upper(), int(am)))
            conn.commit()
            conn.close()
            Label(f1, text="COSTUMER ID CREATED SUCCESSFULLY", font="Arial 16 bold", fg="green").place(x=200, y=600)
            name.set("")
            lastname.set("")
            phone.set("")
            address.set("")
            amount.set("")


# creating costumer id
def costumer_id():
    global name, lastname, phone, address, email, f1, amount

    name = StringVar()
    lastname = StringVar()
    phone = StringVar()
    address = StringVar()
    amount = StringVar()

    f1 = Frame(bg="pink").place(x=0, y=0, width=780, height=780)
    l = Label(f1, text="ADD NEW COSTUMER IN  KHATA", fg="white", bg="cyan", font="Arial 24 italic").place(x=80, y=50)
    l1 = Label(f1, text="NAME", font="Arial 20 bold", bg="pink").place(x=50, y=150)
    l2 = Label(f1, text="LAST NAME", font="Arial 20 bold", bg="pink").place(x=50, y=220)
    l3 = Label(f1, text="PHONE.NO", font="Arial 20 bold", bg="pink").place(x=50, y=290)
    l4 = Label(f1, text="ADDRESS", font="Arial 20 bold", bg="pink").place(x=50, y=370)
    l5 = Label(f1, text="AMOUNT", font="Arial 20 bold", bg="pink").place(x=50, y=440)

    e1 = Entry(font="Arial 20 ", textvariable=name).place(x=250, y=150)
    e2 = Entry(font="Arial 20 ", textvariable=lastname).place(x=250, y=220)
    e3 = Entry(font="Arial 20 ", textvariable=phone).place(x=250, y=290)
    e4 = Entry(font="Arial 20 ", textvariable=address).place(x=250, y=370)
    e5 = Entry(font="Arial 20", textvariable=amount).place(x=250, y=440)

    b1 = Button(f1, text="<=", command=home, width=5).place(x=0, y=0)
    b2 = Button(f1, text="Submit", command=submit_data, font="Arial 16 bold").place(x=350, y=510)


# submiting amount

def Amount_sql():
    a = n_one.get()
    b = l_one.get()
    c = a_one.get()

    n_strip = a.strip()
    l_strip = b.strip()

    conn = connection()
    cur = conn.cursor()
    note = "no"

    if a == "":
        Label(f2, text="<PLEASE ENTER NAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=150)
    elif b == "":
        Label(f2, text="<PLEASE ENTER LASTNAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=220)


    elif cur.execute(
            "SELECT 1,5 FROM khatabook1 WHERE COSTUMER_NAME = '" + n_strip.upper() + "' AND COSTUMER_LASTNAME ='" + l_strip.upper() + "'").fetchone():
        note = "yes"
        cur.execute("UPDATE khatabook1 SET AMOUNT=AMOUNT+? WHERE COSTUMER_NAME=?", (c, a.upper()))
        conn.commit()
        conn.close()
        Label(f2, text="AMOUNT ADDED SUCCESSFULLY", font="Arial 16 bold", fg="green").place(x=200, y=370)
        n_one.set("")
        l_one.set("")
    else:
        if note == "no":
            Label(f2, text=" NO SUCH NAME FOUND", font="Arial 16 bold", fg="green").place(x=200, y=370)
            n_one.set("")
            l_one.set("")


# adding amount in costumer kahat
def add_amount():
    global f2, n_one, l_one, a_one

    n_one = StringVar()
    l_one = StringVar()
    a_one = IntVar()

    f2 = Frame(bg="pink").place(x=0, y=0, width=780, height=780)
    l = Label(f2, text="ADD AMOUNT IN COSTUMER KHATA", fg="white", bg="cyan", font="Arial 24 italic").place(x=80, y=50)
    l1 = Label(f2, text="NAME", font="Arial 20 bold", bg="pink").place(x=50, y=150)
    l2 = Label(f2, text="LAST NAME", font="Arial 20 bold", bg="pink").place(x=50, y=220)
    l3 = Label(f2, text="AMOUNT", font="Arial 20 bold", bg="pink").place(x=50, y=290)

    e1 = Entry(font="Arial 20 ", textvariable=n_one).place(x=250, y=150)
    e2 = Entry(font="Arial 20 ", textvariable=l_one).place(x=250, y=220)
    e3 = Entry(font="Arial 20 ", textvariable=a_one).place(x=250, y=290)

    b1 = Button(f2, text="<=", command=home, width=5).place(x=0, y=0)
    b2 = Button(f2, text="Submit", command=Amount_sql, font="Arial 16 bold").place(x=350, y=410)


# Costumer details
def detail_value():
    a = n_three.get()
    b = l_three.get()
    conn = connection()
    cur = conn.cursor()

    n_strip = a.strip()
    l_strip = b.strip()
    note = "no"

    if a == "":
        Label(f3, text="<PLEASE ENTER NAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=150)
    elif b == "":
        Label(f3, text="<PLEASE ENTER LASTNAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=220)

    elif cur.execute(
            "SELECT 1,5 FROM khatabook1 WHERE COSTUMER_NAME = '" + n_strip.upper() + "' AND COSTUMER_LASTNAME ='" + l_strip.upper() + "'").fetchone():
        note = "yes"
        r = cur.execute(
            "SELECT * FROM khatabook1 WHERE COSTUMER_NAME='" + n_strip.upper() + "' AND COSTUMER_LASTNAME ='" + l_strip.upper() + "' ")
        for i in r:
            t1.insert(END, "\nNAME =   " + i[0] + i[1] + "\nPHONE.NO =   " + str(i[2]) + "\nADDRESS =   " + i[
                3] + "\nAMOUNT=    " + str(i[4]) + "\n")
    else:
        if note == "no":
            Label(f3, text="<NO SUCH NAME FOUND>", font="Arial 10 ", fg="red", bg="pink").place(x=550, y=150)
            n_three.set("")
            l_three.set("")


def detail():
    global n_three, l_three, f3, t1

    n_three = StringVar()
    l_three = StringVar()

    f3 = Frame(bg="pink").place(x=0, y=0, width=780, height=780)
    l = Label(f3, text="COSTUMER DETAILS", fg="white", bg="cyan", font="Arial 24 italic").place(x=80, y=50)
    l1 = Label(f3, text="NAME", font="Arial 20 bold", bg="pink").place(x=50, y=150)
    l2 = Label(f3, text="LAST NAME", font="Arial 20 bold", bg="pink").place(x=50, y=220)

    e1 = Entry(font="Arial 20 ", textvariable=n_three).place(x=250, y=150)
    e2 = Entry(font="Arial 20 ", textvariable=l_three).place(x=250, y=220)

    b1 = Button(f3, text="<=", command=home, width=5).place(x=0, y=0)

    s = Scrollbar(f3)
    s.place(x=680, y=300, height=420)

    t1 = Text(width=40, yscrollcommand=s.set, height=13, font="Arial 20 bold ", fg="yellow", bg="black")
    t1.place(x=70, y=300)
    s.config(command=t1.yview)

    b2 = Button(f3, text="Submit", command=detail_value, font="Arial 16 bold").place(x=600, y=180)


def sub_sql():
    a = n_two.get()
    b = l_two.get()
    c = a_two.get()

    n_strip = a.strip()
    l_strip = b.strip()

    conn = connection()
    cur = conn.cursor()
    note = "no"

    if a == "":
        Label(f4, text="<PLEASE ENTER NAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=150)
    elif b == "":
        Label(f4, text="<PLEASE ENTER LASTNAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=220)
    elif cur.execute(
            "SELECT 1,5 FROM khatabook1 WHERE COSTUMER_NAME = '" + n_strip.upper() + "' AND COSTUMER_LASTNAME ='" + l_strip.upper() + "'").fetchone():
        note = "yes"
        cur.execute("UPDATE khatabook1 SET AMOUNT=AMOUNT-? WHERE COSTUMER_NAME=?", (c, n_strip.upper()))
        conn.commit()
        conn.close()
        Label(f4, text="AMOUNT DEDUCTED SUCCESSFULLY", font="Arial 16 bold", fg="green").place(x=200, y=370)
    else:
        if note == "no":
            Label(f2, text="NO SUCH NAME FOUND", font="Arial 16 bold", fg="green").place(x=200, y=370)
            n_two.set("")
            l_two.set("")


# dey amount pay
def due_amount():
    global f4, n_two, l_two, a_two

    n_two = StringVar()
    l_two = StringVar()
    a_two = IntVar()

    f4 = Frame(bg="pink").place(x=0, y=0, width=780, height=780)
    l = Label(f4, text="SUBTRACT AMOUNT IN COSTUMER KHATA", fg="white", bg="cyan", font="Arial 24 italic").place(x=80,
                                                                                                                 y=50)
    l1 = Label(f4, text="NAME", font="Arial 20 bold", bg="pink").place(x=50, y=150)
    l2 = Label(f4, text="LAST NAME", font="Arial 20 bold", bg="pink").place(x=50, y=220)
    l3 = Label(f4, text="AMOUNT", font="Arial 20 bold", bg="pink").place(x=50, y=290)

    e1 = Entry(font="Arial 20 ", textvariable=n_two).place(x=250, y=150)
    e2 = Entry(font="Arial 20 ", textvariable=l_two).place(x=250, y=220)
    e3 = Entry(font="Arial 20 ", textvariable=a_two).place(x=250, y=290)

    b1 = Button(f4, text="<=", command=home, width=5).place(x=0, y=0)
    b2 = Button(f4, text="Submit", command=sub_sql, font="Arial 16 bold ").place(x=350, y=410)


# costumer list

def name_list():
    f5 = Frame(bg="pink").place(x=0, y=0, width=780, height=780)

    s = Scrollbar(f5)
    s.place(x=735, y=100, height=600)

    l = Label(f5, text="COSTUMERS LIST ", fg="white", bg="cyan", font="Arial 24 italic").place(x=80, y=50)
    t = Text(f5, yscrollcommand=s.set, width=55, height=25, font="Arial 16 bold ", fg="white", bg="black")
    t.place(x=70, y=100)
    s.config(command=t.yview)

    conn = connection()
    cur = conn.cursor()
    r = cur.execute("SELECT* FROM khatabook1 ORDER BY COSTUMER_NAME")
    for i in r:
        t.insert(END, i[0] + " " + i[1] + "      " + str(i[2]) + "   " + i[3] + "   " + str(i[4]) + "\n")
    conn.close()
    b1 = Button(f5, text="<=", command=home, width=5).place(x=0, y=0)


# def delete_id_call():
#     conn = connection()
#     cur = conn.cursor()
#     note = "no"
#     a = n_four.get()
#     b = l_four.get()

#     if a == "":
#         Label(f6, text="<PLEASE ENTER NAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=150)
#     elif b == "":
#         Label(f6, text="<PLEASE ENTER LASTNAME>", font="Arial 10 ", fg="red", bg="pink").place(x=580, y=220)
#     elif cur.execute(
#             "SELECT 1,5 FROM khatabook1 WHERE COSTUMER_NAME = '" + a.upper() + "' AND COSTUMER_LASTNAME ='" + b.upper() + "'").fetchone():
#         note = "yes"
#         value = (f"\'{a}\'")
#         print(value)
#         r = cur.execute("DELETE FROM khatabook1 WHERE COSTUMER_NAME='" + value + "' ")
#         conn.commit()
#         conn.close()
#         Label(f6, text="ID DELETED SUCCESSFULLY", font="Arial 16 bold", fg="green").place(x=200, y=370)

#     else:
#         if note == "no":
#             Label(f6, text="NO SUCH NAME FOUND", font="Arial 16 bold", fg="green").place(x=200, y=370)
#             n_four.set("")
#             l_four.set("")


# main program

def home():
    f = Frame(bg="white").place(x=0, y=0, width=800, height=800)
    l1 = Label(f, text="WELCOME TO \n APNA KHATA BOOK", font="Arial 30 bold", fg="red", bg="yellow").place(x=200, y=50)
    b1 = Button(text="ADD COSTUMER", font="Arial 20 bold", bg="pink", width=30, command=costumer_id).place(x=150, y=300)
    b2 = Button(text="ADD  AMOUNT IN COSTUMER KHATA", font="Arial 20 bold", width=30, bg="pink",
                command=add_amount).place(x=150, y=370)
    b3 = Button(text="VIEW COSTUMER  DETAILS", font="Arial 20 bold", bg="pink", width=30, command=detail).place(x=150,
                                                                                                                y=440)
    b4 = Button(text=" COSTUMER PAYED DUE AMOUNT", font="Arial 20 bold", bg="pink", width=30, command=due_amount).place(
        x=150, y=510)
    b5 = Button(text="VIEW ALL COSTUMER'S LIST", font="Arial 20 bold", bg="pink", width=30, command=name_list).place(
        x=150, y=580)
    

# intro
root = Tk()
root.geometry("800x800")
root.resizable(0, 0)
root.title("khatabook v2.0")
root.configure(background="white")
photo = PhotoImage(file="khatalogo.png")
l2 = Label(image=photo).place(x=150, y=50)
root.update()
time.sleep(2)

home()

root.mainloop()
