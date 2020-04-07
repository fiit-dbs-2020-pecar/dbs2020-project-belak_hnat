import string
from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
import tkinter.messagebox as MessageBox


mydb = mysql.connector.connect(host="localhost", user="root", passwd="dbsheslo",database = "dbs")
my_cursor = mydb.cursor()


def btn_showall():
        tb.delete(*tb.get_children())
        if (dtbs == "zakaznik"):
            my_cursor.execute("SELECT * FROM zakaznik ORDER BY ID_zakaznik")
            # my_cursor.execute("SELECT * FROM zakaznik LIMIT 3")
        elif (dtbs == "donaska"):
            my_cursor.execute("SELECT * FROM donaska ORDER BY ID_donaska")
        elif (dtbs == "objednavka"):
            my_cursor.execute("SELECT * FROM objednavka ORDER BY ID_donaska")
        elif (dtbs == "restauracia"):
            my_cursor.execute("SELECT * FROM restauracia ORDER BY ID_donaska")
        elif (dtbs == "restauracia"):
            my_cursor.execute("SELECT * FROM dodavatel ORDER BY ID_dodavatel")
        rows = my_cursor.fetchall()
        for i in rows:
            tb.insert('', 'end', values=i)


def get():
    top=Toplevel()
    top.attributes('-topmost', 'true') #okno bude vzdy v predu
    top.geometry("400x100")
    top.title ("Search")
    label_name=Label(top,text="Enter items's ID")
    label_name.place(x=20,y=20)
    id=Entry(top)
    id.place(x=150,y=20)
    btn=Button(top,text="Search",height = 1, width = 12,command=lambda: search(id.get(),id,top))
    btn.place(x=20,y=40)





def search(get_id,id,top):
    if (get_id==""):
        MessageBox.showinfo("Insert status","Enter all required fields")
    elif (get_id.isnumeric() == False):
        MessageBox.showinfo("Insert status", "Invalid character")
        id.delete(0,END)
    else:
        tb.delete(*tb.get_children())
        if (dtbs == "zakaznik"):
            my_cursor.execute("select * from zakaznik where ID_zakaznik='"+get_id+"'")
        elif (dtbs == "donaska"):
            my_cursor.execute("select * from donaska where ID_donaska='" + get_id + "'")
        elif (dtbs == "objednavka"):
            my_cursor.execute("select * from donaska where ID_donaska='" + get_id + "'")
        elif (dtbs == "restauracia"):
            my_cursor.execute("select * from restauracia where ID_restauracia='" + get_id + "'")
        elif (dtbs == "dodavatel"):
            my_cursor.execute("select * from restauracia where ID_dodavatel='" + get_id + "'")
        rows = my_cursor.fetchall()
        for i in rows:
            tb.insert('', 'end', values=i)
        top.destroy()

def btn_insert():
    top = Toplevel()
    top.attributes('-topmost', 'true')
    top.title("Add customer")
    # 5 itemov
    if (dtbs == "zakaznik" or dtbs == "restauracia"):
        top.geometry("400x150")
        if dtbs == "zakaznik":
            m,n,o,p="Name:","Surname:","Email:","Premium:"
        elif dtbs == "restauracia":
            m,n,o,p="Manazer","name","Adress","Month/$"
        elif dtbs == "dodavatel":
            m, n, o, p = "Name", "Food", "Price", "ID_restauracia"
        btn = Button(top, text="Add", height=1, width=12,command=lambda: insertFIVE(name, surname, email, premium, name.get(),
                                                                                surname.get(), email.get(),premium.get(), top))
        btn.place(x=20, y=110)

    # 6 itemov
    elif (dtbs == "donaska" or dtbs == "objednavka"):
        top.geometry("400x170")
        if (dtbs == "donaska"):
            m, n, o, p, r = "Adress:", "ID_customer", "Payment", "Price/$","Phone N."
        elif (dtbs == "objednavka"):
            m, n, o, p, r = "Food", "Weight", "Price/$", "ID_Delivery", "ID_Restaurant"
        label_price = Label(top, text=r)
        label_price.place(x=20, y=100)
        price = Entry(top)
        price.place(x=150, y=100)
        btn = Button(top, text="Add", height=1, width=12, command=lambda: insertSIX(name, surname, email, premium,price,name.get(),
                                                                                 surname.get(), email.get(),premium.get(),price.get(),top))
        btn.place(x=20, y=130)

    label_name = Label(top, text=m)
    label_name.place(x=20, y=20)
    label_surname = Label(top, text=n)
    label_surname.place(x=20, y=40)
    lable_email = Label(top, text=o)
    lable_email.place(x=20, y=60)
    label_Premium = Label(top, text=p)
    label_Premium.place(x=20, y=80)

    name = Entry(top)
    name.place(x=150, y=20)
    surname = Entry(top)
    surname.place(x=150, y=40)
    email = Entry(top)
    email.place(x=150, y=60)
    premium = Entry(top)
    premium.place(x=150, y=80)

def clearFieldSIX(e1,e2,e3,e4,e5):
    MessageBox.showinfo("Insert status", "Invalid character")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

def insertSIX(e1,e2,e3,e4,e5,e1txt,e2txt,e3txt,e4txt,e5txt,top):
    if e1txt == "" or e2txt == "" or e3txt == "" or e4txt == "" or e5txt=="":
        MessageBox.showinfo("Insert status", "Enter all required fields")
    elif (e1txt.isnumeric() == True or e2txt.isnumeric() == False or e3txt.isnumeric() == True or e4txt.isnumeric() == False or e5txt.isnumeric() == False) and dtbs == "donaska" :
        clearFieldSIX(e1, e2, e3, e4, e5)
    elif (e1txt.isnumeric() == True or e2txt.isnumeric() == False or e3txt.isnumeric() == False or e4txt.isnumeric() == False or e5txt.isnumeric() == False) and dtbs == "objednavka" :
        clearFieldSIX(e1, e2, e3, e4, e5)
    else:
        if dtbs == "donaska":
            sqlStuff = "INSERT INTO donaska (adresa,id_zakaznik,typ_platby,stav_obj,tel_cislo) VALUES (%s, %s, %s, %s, %s)"
        elif dtbs == "objednavka":
            sqlStuff = "INSERT INTO objednavka (jedlo,vaha,cena,id_donaska,id_restauracia) VALUES (%s, %s, %s, %s, %s)"
        records = (e1txt, e2txt, e3txt, e4txt,e5txt)
        my_cursor.execute(sqlStuff, records)
        mydb.commit()
        top.destroy()

def clearFieldFIVE(e1,e2,e3,e4):
    MessageBox.showinfo("Insert status", "Invalid character")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def insertFIVE(e1,e2,e3,e4,e1txt,e2txt,e3txt,e4txt,top):
    if e1txt =="" or e2txt =="" or e3txt=="" or e4txt=="":
        MessageBox.showinfo("Insert status","Enter all required fields")
    elif (e1txt.isnumeric() == True or e2txt.isnumeric() == True or e3txt.isnumeric() == True or e4txt.isnumeric() == True):
        clearFieldFIVE(e1, e2, e3, e4)
    elif (e1txt.isnumeric() == True or e2txt.isnumeric() == True or e3txt.isnumeric() == True or e4txt.isnumeric() == False):
        clearFieldFIVE(e1, e2, e3, e4)
    elif (e1txt.isnumeric() == True or e2txt.isnumeric() == True or e3txt.isnumeric() == False or e4txt.isnumeric() == False):
        clearFieldFIVE(e1, e2, e3, e4)
    else:
        if dtbs == "zakaznik":
            sqlStuff = "INSERT INTO zakaznik (meno,priezvisko,email,premium) VALUES (%s, %s, %s, %s)"
        elif dtbs == "restauracia":
            sqlStuff = "INSERT INTO restauracia (manazer,nazov,adresa,mesiac_zisk) VALUES (%s, %s, %s, %s)"
        elif dtbs == "dodavatel":
            sqlStuff = "INSERT INTO dodavatel (nazov,typ_jedla,cena,id_restauracia) VALUES (%s, %s, %s, %s)"
        records = (e1txt, e2txt, e3txt, e4txt)
        my_cursor.execute(sqlStuff, records)
        mydb.commit()
        top.destroy()

def btn_delete():
    top=Toplevel()
    top.attributes('-topmost', 'true')
    top.geometry("400x100")
    top.title ("Delete customer")
    label_name=Label(top,text="Enter customer's ID: ")
    label_name.place(x=20,y=20)
    id=Entry(top)
    id.place(x=150,y=20)
    btn = Button(top, text="Delete item", height=1, width=12, command=lambda: delete(id,id.get(), top))
    btn.config(state='normal')
    btn.place(x=20,y=40)

def delete(id,idtxt,top):
    if idtxt=="":
        MessageBox.showinfo("Insert status", "Enter all required fields")
    elif (idtxt.isnumeric() == False):
        MessageBox.showinfo("Insert status", "Invalid character")
        id.delete(0, END)
    else:
        if dtbs == "zakaznik":
            my_cursor.execute("DELETE FROM  zakaznik WHERE ID_zakaznik='"+idtxt+"'")
        elif dtbs == "donaska":
            my_cursor.execute("DELETE FROM  donaska WHERE ID_donaska='" + idtxt + "'")
        elif dtbs == "objednavka":
            my_cursor.execute("DELETE FROM  objednavka WHERE ID_objednavka='" + idtxt + "'")
        elif dtbs == "restauracia":
            my_cursor.execute("DELETE FROM  restauracua WHERE ID_restauracia='" + idtxt + "'")
        elif dtbs == "dodavatel":
            my_cursor.execute("DELETE FROM  dodavatel WHERE ID_dodavatel='" + idtxt + "'")
        mydb.commit()
        top.destroy()

def btn_update_customer():
    top = Toplevel()
    top.attributes('-topmost', 'true')
    top.title("Edit customer")
    # 5 item
    if (dtbs == "zakaznik"):
        top.geometry("400x210")
        if dtbs =="zakaznik":
            m, n, o, p, r, s="Insert ID: ","Edit data of customer ","Name","Surname: ","Email:","Premium:"
        elif dtbs == "restauracia":
            m, n, o, p, r, s = "Insert ID: ", "Edit data of restaurant ", "Manazer", "Name: ", "Adress:", "Income/Month:"
        elif dtbs == "dodavatel":
            m, n, o, p, r, s = "Insert ID: ", "Edit data of restaurant ", "Name", "Food", "Price", "ID_restaurand"
        btn = Button(top, text="Edit", height=1, width=12,command=lambda: update_customerFIVE(id, name, surname, email, premium, id.get(),
                                                                                            name.get(),surname.get(), email.get(), premium.get(), top))
        btn.place(x=20, y=170)
    #6 item
    elif (dtbs == "donaska" or dtbs == "objednavka"):
        top.geometry("400x230")
        if dtbs == "donaska":
            m,n,o,p,r,s,t="Insert ID: ","Edit data of delivery","Adress","ID_Customer","Payment","Order status","Phone N."
        elif dtbs == "objednavka":
            m,n,o,p,r,s,t="Insert ID: ","Edit data of order","Food","Weight","Price","ID_Delivery","ID_Restaurant"
        label_price = Label(top, text=t)
        label_price.place(x=20, y=160)
        price = Entry(top)
        price.place(x=150, y=160)
        btn = Button(top, text="Edit", height=1, width=12,command=lambda: update_customerSIX(id, name, surname, email, premium,price,id.get(),
                                                                                            name.get(),surname.get(), email.get(), premium.get(),price.get(), top))
        btn.place(x=20, y=190)

    label_ID = Label(top, text=m)
    label_ID.place(x=20, y=20)
    label_ID = Label(top, text=n)
    label_ID.place(x=20, y=60)
    label_name = Label(top, text=o)
    label_name.place(x=20, y=80)
    label_Surname = Label(top, text=p)
    label_Surname.place(x=20, y=100)
    label_Email= Label(top, text=r)
    label_Email.place(x=20, y=120)
    label_Premium = Label(top, text=s)
    label_Premium.place(x=20, y=140)

    id = Entry(top)
    id.place(x=150, y=20)
    name = Entry(top)
    name.place(x=150, y=80)
    surname = Entry(top)
    surname.place(x=150, y=100)
    email = Entry(top)
    email.place(x=150, y=120)
    premium= Entry(top)
    premium.place(x=150, y=140)

def deleteSIX(e1,e2,e3,e4,e5,e6):
    MessageBox.showinfo("Insert status", "Invalid character")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

def update_customerSIX(e1,e2,e3,e4,e5,e6,e1txt,e2txt,e3txt,e4txt,e5txt,e6txt,top):
    if e1txt=="" or e2txt =="" or e3txt =="" or e4txt=="" or e5txt==""or e6txt=="":
        MessageBox.showinfo("Insert status","Enter all required fields")
    elif (e1txt.isnumeric() == False or e2txt.isnumeric() == True or e3txt.isnumeric() == False or e4txt.isnumeric() == True or e5txt.isnumeric() == True or e6txt.isnumeric() == False) and dtbs == "donaska":
        deleteSIX(e1,e2,e3,e4,e5,e6)
    elif (e1txt.isnumeric() == False or e2txt.isnumeric() == True or e3txt.isnumeric() == False or e4txt.isnumeric() == False or e5txt.isnumeric() == False or e6txt.isnumeric() == False) and dtbs == "objednavka":
        deleteSIX(e1, e2, e3, e4, e5, e6)
    else:
        if (dtbs == "donaska"):
            my_cursor.execute("UPDATE donaska SET adresa='"+e2txt+"', id_zakaznik='"+e3txt+"', typ_platby='"+e4txt+"',stav_obj='"+e5txt+"', tel_cislo='"+e6txt+"' WHERE ID_donaska='"+e1txt+"'")
        elif (dtbs == "objednavka"):
            my_cursor.execute("UPDATE objednavka SET jedlo='"+e2txt+"', vaha='"+e3txt+"', cena='"+e4txt+"',id_doanska='"+e5txt+"', id_restauracia='"+e6txt+"' WHERE ID_objednavka'"+e1txt+"'")
        mydb.commit()
        top.destroy()


def deleteFIVE(e1,e2,e3,e4,e5):
    MessageBox.showinfo("Insert status", "Invalid character")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

def update_customerFIVE(e1,e2,e3,e4,e5,e1txt,e2txt,e3txt,e4txt,e5txt,top):
    if e1txt=="" or e2txt =="" or e3txt =="" or e4txt=="" or e5txt=="":
        MessageBox.showinfo("Insert status","Enter all required fields")
    elif (e1txt.isnumeric() == False or e2txt.isnumeric() == True or e3txt.isnumeric() == True or e4txt.isnumeric() == True or e5txt.isnumeric() == True) and dtbs == "zakaznik":
        deleteFIVE(e1, e2, e3, e4, e5)
    elif (e1txt.isnumeric() == False or e2txt.isnumeric() ==  True or e3txt.isnumeric() == True or e4txt.isnumeric() == True or e5txt.isnumeric() == False) and dtbs == "restauracia":
        deleteFIVE(e1, e2, e3, e4, e5)
    elif (e1txt.isnumeric() == False or e2txt.isnumeric() ==  True or e3txt.isnumeric() == True or e4txt.isnumeric() == False or e5txt.isnumeric() == False) and dtbs == "dodavatel":
        deleteFIVE(e1, e2, e3, e4, e5)
    else:
        if dtbs == "zakaznik":
            my_cursor.execute("UPDATE zakaznik SET meno='"+e2txt+"', priezvisko='"+e3txt+"', email= '"+e4txt+"',premium='"+e5txt+"' WHERE ID_zakaznik='"+e1txt+"'")
        if dtbs == "restauracia":
            my_cursor.execute("UPDATE restauracia SET manazer='"+e2txt+"', nazov='"+e3txt+"', adresa= '"+e4txt+"',adresa='"+e5txt+"' WHERE ID_restauracia='"+e1txt+"'")
        if dtbs == "dodavatel":
            my_cursor.execute("UPDATE dodavatel SET nazov='"+e2txt+"', typ_jedla='"+e3txt+"', cena= '"+e4txt+"',id_restaurant='"+e5txt+"' WHERE ID_dodavatel='"+e1txt+"'")
        mydb.commit()
        top.destroy()

def adv_settings():
    tb.delete(*tb.get_children())
    my_cursor.execute("select * from dbs.donaska join dbs.zakaznik  where zakaznik.ID_zakaznik=donaska.id_zakaznik")
    rows = my_cursor.fetchall()
    print(rows)


def choose_database(x):
    global dtbs
    if x == 1:
        dtbs = "zakaznik"
        m,n,o,p,r,s = "ID","Name:","Surname:","Email:","Premium:","----"
        my_cursor.execute("SELECT * FROM zakaznik")
    elif x == 2:
        dtbs = "donaska"
        m, n, o, p, r, s = "ID","Adress:", "ID_customer", "Payment", "Order status","Phone N."
        my_cursor.execute("SELECT * FROM donaska")
    elif x == 3:
        dtbs = "objednavka"
        m, n, o, p, r, s = "ID","Food", "Weight", "Price", "ID_Delivery","ID_Restaurant"
        my_cursor.execute("SELECT * FROM objednavka")
    elif x == 4:
        dtbs = "restauracia"
        m, n, o, p, r, s = "ID","Manazer", "Name", "Adress", "Income/M","----"
        my_cursor.execute("SELECT * FROM restauracia")
    elif x == 5:
        dtbs = "dodavatel"
        m, n, o, p, r, s = "ID","Name", "Food", "Price", "ID_Restaurant","----"
        my_cursor.execute("SELECT * FROM dodavatel")
    elif x == 6:
        dtbs = "dodavatel"
        m, n, o, p, r, s = "ID","Name", "Food", "Price", "ID_Restaurant","----"
        my_cursor.execute("SELECT * FROM dodavatel")


    tb.delete(*tb.get_children())
    rows = my_cursor.fetchall()
    for i in rows:
        tb.insert('', 'end', values=i)
    tb.heading(0, text=m)
    tb.heading(1, text=n)
    tb.heading(2, text=o)
    tb.heading(3, text=p)
    tb.heading(4, text=r)
    tb.heading(5, text=s)






# sqlStuff = "INSERT INTO zakaznik (meno,priezvisko,email,premium) VALUES (%s, %s, %s,%s)"
# records = ("Dano", "Drhly", "jano@debeu", "12")
# my_cursor.execute(sqlStuff, records)
# mydb.commit()
#
# sqlStuff = "INSERT INTO donaska (adresa,id_zakaznik,typ_platby,cena,tel_cislo) VALUES (%s, %s, %s, %s,%s)"
# records = ("Dlhy", "45", "Cash", "24","0908552441")
# my_cursor.execute(sqlStuff, records)
# mydb.commit()

root = Tk()
root.title("Customers")
root.geometry("772x520+400+200")
menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Databases",menu=submenu)

submenu.add_command(label="Customers",command=lambda: choose_database(1))
submenu.add_command(label="Deliverys",command=lambda: choose_database(2))
submenu.add_command(label="Orders",command=lambda: choose_database(3))
submenu.add_command(label="Restaurants",command=lambda: choose_database(4))
submenu.add_command(label="Suppliers",command=lambda: choose_database(5))
submenu.add_command(label="Employees",command=lambda: choose_database(6))

my_cursor.execute("select * from zakaznik WHERE ID_zakaznik")
rows = my_cursor.fetchall()
total = my_cursor.rowcount

tb = ttk.Treeview(root, column=(0, 1, 2, 3, 4,5), show="headings", height=5, selectmode='browse')
tb.place(x=30, y=95)
vsb = ttk.Scrollbar(root, orient="vertical", command=tb.yview)
vsb.pack(side='right', fill='y')
tb.configure(yscrollcommand=vsb.set)
tb.column(0, width=70, minwidth=0,anchor="c")
tb.column(1, width=100, minwidth=0,anchor="c")
tb.column(2, width=100, minwidth=0,anchor="c")
tb.column(3, width=100, minwidth=0,anchor="c")
tb.column(4, width=70, minwidth=0,anchor="c")
tb.column(5, width=100, minwidth=0,anchor="c")
choose_database(1)
tb.pack(fill=BOTH, expand=0, side='right')

btn_showall = Button(root, text="Refresh table",height = 1, width = 23,command=btn_showall)
btn_showall.place(x=20,y=20)

btn_get = Button(root, text="Search item",height = 1, width = 23,command=get)
btn_get.place(x=20,y=60)

btn_insert = Button(root, text="Add item",height = 1, width = 23,command=btn_insert)
btn_insert.place(x=20,y=100)

btn_delete = Button(root, text="Delete item",height = 1, width = 23,command=btn_delete)
btn_delete.place(x=20,y=140)

btn_update_customer = Button(root, text="Edit item",height = 1, width = 23,command=btn_update_customer)
btn_update_customer.place(x=20,y=180)

btn_special = Button(root, text="Advanced settings",height = 1, width = 23,command=adv_settings)
btn_special.place(x=20,y=220)

root.mainloop()