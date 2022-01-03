from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#database
conn = sqlite3.connect('stadium.db')

c = conn.cursor()


'''c.execute("""CREATE TABLE customers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        number INTEGER,
        ticket_class INTEGER,
        ticket_price INTEGER,
        match_id INTEGER,
        FOREIGN KEY (match_id) REFERENCES matchs(m_id) ON UPDATE CASCADE ON DELETE CASCADE)
""")

c.execute("""CREATE TABLE matchs(
        m_id INTEGER PRIMARY KEY,
        f_teamname TEXT,
        s_teamname TEXT,
        m_date TEXT)
""")'''

#end of creating the database











#first gui
def page1(root):
    root.geometry('377x260')
    page = Frame(root)
    #log in function
    def logging():
        str1 = e1.get()
        str2 = e2.get()

        if(str1 != "admin" or str2 != "admin"):
            messagebox.showerror("Error", "Wrong Entry")
            e1.delete(0, END)
            e2.delete(0, END)
        else:
            changepage(2)
    #end of log in function

    l1 = Label(page,text= "Welcom to our Tickts Reservation System", justify= LEFT, font= ('Arial',14), padx = 10,pady = 10,  fg = "dark green", bg = "light green").grid(row = 0, columnspan = 6, sticky= "N" )
    l2 = Label(page, text = "Sign in", justify=CENTER, font = 18, padx = 10, pady = 20, fg = "black").grid(row = 1, columnspan = 6, sticky= "N")

    le1 = Label(page , text = "Username",  justify=CENTER, font = 16,padx = 10 ,pady = 10, ).grid(row=  2, column = 0, columnspan= 3, sticky= "W")
    le1 = Label(page , text = "Password",  justify=CENTER, font = 16, padx = 10, pady = 10, ).grid(row=  3, column = 0, columnspan= 3, sticky= "W")


    e1 = Entry(page, width = 40)
    e2 = Entry(page, width = 40, show = "*")
    e1.grid(row = 2, column = 3, columnspan = 3, padx= 10)
    e2.grid(row =3 , column = 3, columnspan = 3, padx= 10)

    b1 = Button(page, text = "Log in",padx = 20 , pady = 5, bg = "#CCCCCC" , font=('Times' , 14), relief=SOLID,cursor='hand2' ,command = logging)
    b2 = Button(page, text = "Quit", padx = 20 , pady = 5 ,  bg = "#CCCCCC" , fg = 'red', font=('Times' , 14), relief=SOLID,cursor='hand2' ,command = root.quit)
    b1.grid(row = 5, column = 1 ,columnspan= 3,  sticky= "S")
    b2.grid(row = 5 , column = 3 ,columnspan= 3,sticky= "S")
    page.pack()
#end of first gui










#second gui
def page2(root):
    page = Frame(root)
    root.geometry('377x260')
    l1 = Label(page,text= "Choose what action you want to do", justify= LEFT, font= 20, padx = 10,pady = 10,  fg = "white", bg = "dark green").grid(row = 0, columnspan = 6, sticky= "N" )
    b1 = Button(page, text = "Reserve a ticket", padx = 20, pady = 10, fg = "blue",command =  lambda : changepage(3))
    b2 = Button(page, text = "Update Matches", padx = 20, pady = 10, fg = "green", command = lambda : changepage(4))
    b3 =  Button(page, text = "Quit", padx = 20, pady = 10, fg = "red", command = quit)
    b1.grid(row = 1, column = 0 ,columnspan= 2,  sticky= "S")
    b2.grid(row = 1, column = 2 ,columnspan= 2,  sticky= "S")
    b3.grid(row = 1, column = 4 ,columnspan= 2,  sticky= "S")
    page.pack()
#end of second gui













#third gui
def page3(root):
    page = Frame(root)
    root.title('New Entry')
    root.geometry('850x450')

    #showing ticket price function
    def show():
        if combo.get() == '1':
            Label(right_frame, text="850.00 LE", bg='#CCCCCC',font=f).grid(row=5, column=2, sticky=W, pady=10)
        elif combo.get() == '2':
            Label(right_frame, text="600.00 LE", bg='#CCCCCC',font=f).grid(row=5, column=2, sticky=W, pady=10)
        elif combo.get() == '3':
            Label(right_frame, text="350.00 LE", bg='#CCCCCC',font=f).grid(row=5, column=2, sticky=W, pady=10)
    #end of showing price function


    f = ('Times', 14)
    var_class = IntVar()


    right_frame = Frame(root, bd=2, bg='#CCCCCC',relief=SOLID, padx=10, pady=10)

    vv = [ 1 , 2 , 3]
    combo = ttk.Combobox(right_frame , values = vv , textvariable = var_class ,width = 28)
    combo.current(0)

    Label(right_frame, text="Enter ID", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Name", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)
    Label(right_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)
    Label(right_frame, text="Contact Number", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)
    Label(right_frame, text="Ticket Class", bg='#CCCCCC',font=f).grid(row=4, column=0, sticky=W, pady=10)
    Label(right_frame, text="Ticket Price", bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)
    Label(right_frame, text="Match ID", bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)

    register_id = Entry(right_frame, font=f)
    register_name = Entry(right_frame, font=f )
    register_email = Entry(right_frame, font=f )
    register_mobile = Entry( right_frame,  font=f ) 
    match_id = Entry( right_frame,  font=f )  

    #inserting data to the database
    def add():
        if combo.get() == '1':
            price = 850
        elif combo.get() == '2':
            price = 600
        elif combo.get() == '3':
            price = 350
        
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()
        c.execute('INSERT INTO customers VALUES (:id , :name, :email, :number, :ticketclass, :ticketprice, :matchid)',
            {
                'id' : register_id.get(),
                'name' :  register_name.get(),
                'email' : register_email.get(),
                'number' : register_mobile.get(),
                'ticketclass' : combo.get(),
                'ticketprice' : price,
                'matchid' : match_id.get()})
        
        register_id.delete(0,END)
        register_name.delete(0,END)
        register_email.delete(0,END)
        register_mobile.delete(0,END)
        combo.delete(0,END)
        match_id.delete(0,END)

        conn.commit()
        conn.close()
    #end of inserting function


    #delete record function
    def delete():
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()

        c.execute('DELETE from customers WHERE id = ' + register_id.get())

        register_id.delete(0,END)
        register_name.delete(0,END)
        register_email.delete(0,END)
        register_mobile.delete(0,END)
        combo.delete(0,END)
        match_id.delete(0,END)

        conn.commit()
        conn.close()
    #end of deleting record function

    #update function
    def update():
        if combo.get() == '1':
            price = 850
        elif combo.get() == '2':
            price = 600
        elif combo.get() == '3':
            price = 350
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()

        c.execute("""UPDATE customers SET
            name = :c_name,
            email = :c_email,
            number = :c_number,
            ticket_class = :t_class,
            ticket_price = :t_price,
            match_id = :mid

            WHERE id = :c_id """,
            {
            'c_name' : register_name.get(),
            'c_email' : register_email.get(),
            'c_number' : register_mobile.get(),
            't_class' : combo.get(),
            't_price' : price,
            'mid' : match_id.get(),

            'c_id' : register_id.get()
            }    
        )
        register_id.delete(0,END)
        register_name.delete(0,END)
        register_email.delete(0,END)
        register_mobile.delete(0,END)
        combo.delete(0,END)
        match_id.delete(0,END)
        conn.commit()
        conn.close()
    #end of update function


    #printing all data in customers table
    def view():
        page = Toplevel(root)
        page.title('Query')
        page.geometry('700x300')
        def readfromdatabase():
           cur.execute("SELECT * from customers")
           return cur.fetchall()

        def showallrecords():
         data = readfromdatabase()
         for index, dat in enumerate(data):
              Label(page, text=dat[0]).grid(row=index+1, column=0)
              Label(page, text=dat[1]).grid(row=index+1, column=2)
              Label(page, text=dat[2]).grid(row=index+1, column=4)
              Label(page, text=dat[3]).grid(row=index+1, column=6)
              Label(page, text=dat[5]).grid(row=index+1, column=8)
              Label(page, text=dat[6]).grid(row=index+1, column=10)


        connection = sqlite3.connect('stadium.db')
        cur = connection.cursor()
        id_Label = Label(page, text="ID ", width=10)
        name_Label = Label(page, text="Name", width=10)
        email_Label = Label(page, text="Email", width=10)
        number_Label = Label(page, text="Number", width=10)
        price_Label = Label(page, text="Price", width=10)
        match_id_Label = Label(page, text="Match ID", width=10)
        id_Label.grid(row=0, column=0)
        name_Label.grid(row=0, column=2)
        email_Label.grid(row=0, column=4)
        number_Label.grid(row=0, column=6)
        price_Label.grid(row=0, column=8)
        match_id_Label.grid(row=0, column=10)
        showallrecords()
    #end of the query



    show_price_btn = Button(right_frame, width=15, text='Show price' , relief=SOLID,cursor='hand2',command=lambda :show())
    add_btn = Button(right_frame, width=15, text='Add', font=f, relief=SOLID,cursor='hand2',command= add)
    delete_btn = Button(right_frame, width=15, text='Delete', font=f, relief=SOLID,cursor='hand2',command= delete)
    quit_btn =  Button(right_frame, width=15, text='EXIT', fg = 'red' , font=f, relief=SOLID,cursor='hand2',command = quit)
    back_btn =  Button(right_frame, width=15, text='Back', font=f, relief=SOLID,cursor='hand2',command = lambda : changepage(2))
    update_btn = Button(right_frame, width=15, text='Update', font=f, relief=SOLID,cursor='hand2',command=update)
    view_btn = Button(right_frame, width=15, text='View', font=f, relief=SOLID,cursor='hand2',command= view)

    register_id.grid(row=0, column=1, pady=10, padx=20)
    register_name.grid(row=1, column=1, pady=10, padx=20)
    register_email.grid(row=2, column=1, pady=10, padx=20) 
    register_mobile.grid(row=3, column=1, pady=10, padx=20)
    match_id.grid(row=6, column=1, pady=10, padx=20)
    combo.grid(row=4, column=1, pady=10, padx=20)
    show_price_btn.grid(row=5, column=1, pady=10, padx=20)
    add_btn.grid(row=7, column = 0, pady=10, padx=20)
    delete_btn.grid(row=7, column=1, pady=10, padx=20)
    update_btn.grid(row=7, column=2, pady=10, padx=20)
    back_btn.grid(row=8, column=2, pady=10, padx=20)
    quit_btn.grid(row=8, column=3, pady=10, padx=20)
    view_btn.grid(row=7, column=3, pady=10, padx=20)
    
    right_frame.pack()
#end of third gui













#fourth gui
def page4 (root):
    page = Frame(root)
    root.title('Update')
    root.geometry('900x300')
    f = ('Times', 14) 


    l1 = Label(root, text="Enter ID Match", bg='#CCCCCC',font=f, cursor='hand2')
    l2 = Label(root, text="Enter Frist club ", bg='#CCCCCC',font=f,cursor='hand2')
    l3 = Label(root, text="Enter Second club ", bg='#CCCCCC',font=f,cursor='hand2')
    l4 = Label(root, text="Enter Match date ", bg='#CCCCCC',font=f,cursor='hand2')
    

    register_id_match = Entry(root, font=f)
    register_name_club1 = Entry(root, font=f)
    register_name_club2 = Entry(root, font=f)
    register_match_date = Entry(root, font=f)


    #inserting data function
    def add():
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()
        c.execute('INSERT INTO matchs VALUES (:m_id , :f_team, :s_team, :m_date)',
            {
                'm_id' :  register_id_match.get(),
                'f_team' : register_name_club1.get(),
                's_team' : register_name_club2.get(),
                'm_date' : register_match_date.get()
            }
        )
        register_id_match.delete(0,END)
        register_name_club1.delete(0,END)
        register_name_club2.delete(0,END)
        register_match_date.delete(0,END)
        conn.commit()
        conn.close()
    #end of inserting function


    #deleting a record function
    def delete():
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()

        c.execute('DELETE from matchs WHERE m_id = ' + register_id_match.get())
        
        register_id_match.delete(0,END)
        register_name_club1.delete(0,END)
        register_name_club2.delete(0,END)
        register_match_date.delete(0,END)

        conn.commit()
        conn.close()
    #end of deleting function
    
    
    #update matches data function
    def update():
        conn = sqlite3.connect('stadium.db')
        c = conn.cursor()

        c.execute("""UPDATE matchs SET
            f_teamname = :fname,
            s_teamname = :sname ,
            m_date = :date

            WHERE m_id = :mid """,
            {
            'fname' : register_name_club1.get(),
            'sname' : register_name_club2.get(),
            'date' : register_match_date.get(),
            'mid' : register_id_match.get()
            })
        
        register_id_match.delete(0,END)
        register_name_club1.delete(0,END)
        register_name_club2.delete(0,END)
        register_match_date.delete(0,END)
        conn.commit()
        conn.close()
    #end of updating function

    #printing data in matchs table
    def view():
        page = Toplevel(root)
        page.title('Query')
        page.geometry('700x300')
        def readfromdatabase():
           cur.execute("SELECT * from matchs")
           return cur.fetchall()

        def showallrecords():
         data = readfromdatabase()
         for index, dat in enumerate(data):
              Label(page, text=dat[0]).grid(row=index+1, column=0)
              Label(page, text=dat[1]).grid(row=index+1, column=2)
              Label(page, text=dat[2]).grid(row=index+1, column=4)
              Label(page, text=dat[3]).grid(row=index+1, column=6)


        connection = sqlite3.connect('stadium.db')
        cur = connection.cursor()
        id_Label = Label(page, text="ID Match", width=10)
        frist_Label = Label(page, text="Frist Club", width=10)
        second_Label = Label(page, text="Second Club", width=10)
        date_Label = Label(page, text="Date", width=10)
        
        
        id_Label.grid(row=0, column=0)
        frist_Label.grid(row=0, column=2)
        second_Label.grid(row=0, column=4)
        date_Label.grid(row=0, column=6)

        showallrecords()
    #end of the function

        
    add_btn = Button(root, width=15, text='Add', font=f, relief=SOLID,cursor='hand2', command= add)
    delete_btn = Button(root, width=15, text='Delete', font=f, relief=SOLID,cursor='hand2',command=delete)
    update_btn = Button(root, width=15, text='Update', font=f, relief=SOLID,cursor='hand2',command=update)
    quit_btn =  Button(root, width=15, text='EXIT', fg = 'red' , font=f, relief=SOLID,cursor='hand2',command = quit)
    back_btn =  Button(root, width=15, text='Back', font=f, relief=SOLID,cursor='hand2',command = lambda : changepage(2))
    view_btn = Button(root, width=15, text='View', font=f, relief=SOLID,cursor='hand2',command= view)

    

    l1.grid(row=0, column=0, sticky=W, pady=10)
    l2.grid(row=1, column=0, sticky=W, pady=10)
    l3.grid(row=1, column=2, sticky=W, pady=10)
    l4.grid(row=2, column=0, sticky=W, pady=10)
    

    register_id_match.grid(row=0, column=1, pady=10, padx=20)
    register_name_club1.grid(row=1, column=1, pady=10, padx=20)
    register_name_club2.grid(row=1, column=3, pady=10, padx=20)
    register_match_date.grid(row=2, column=1, pady=10, padx=20)

    
    add_btn.grid(row=3, column=0, pady=10, padx=20)
    delete_btn.grid(row=3, column=1, pady=10, padx=20)
    update_btn.grid(row=3, column=2, pady=10, padx=20)
    quit_btn.grid(row=4, column=3, pady=10, padx=20)
    back_btn.grid(row=4, column=2, pady=10, padx=20)  
    view_btn.grid(row=3, column=3, pady=10, padx=20)
#end of the fourth gui













#change guis function
def changepage(x):
    global pagenum ,root
    for widget in root.winfo_children():
        widget.destroy()
    if(x == 2):
        page2(root)
    elif (x == 3):
        page3(root)
    elif (x == 4):
        page4(root)
#end of change function
    







root = Tk()
global pagnum
pagnum = 1
page1(root) 

conn.commit()
conn.close()

root.mainloop()
