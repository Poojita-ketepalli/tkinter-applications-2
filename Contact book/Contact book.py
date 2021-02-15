from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pymysql
from tkinter import ttk

root=Tk()

root.title("Contact book")
root.geometry("580x230+500+200")
root.config(bg="white")
root.maxsize(width=580,height=230)
root.minsize(width=580,height=230)

frame1 = Frame(root,width=350,height=230)
frame1.place(x=0,y=0)
frame2 = Frame(root,width=230,height=230)
frame2.place(x=352,y=0)

name_lbl = Label(frame1,text="Name")
name_lbl.place(x=50,y=20)
name=StringVar()
name_entry = Entry(frame1,textvariable=name,width=15)
name_entry.place(x=130,y=20)

ph_no_lbl = Label(frame1,text="PH NO.")
ph_no_lbl.place(x=50,y=80)
ph_no=StringVar()
ph_no_entry = Entry(frame1,textvariable=ph_no,width=15)
ph_no_entry.place(x=130,y=80)

scrolly = Scrollbar(frame2, orient=VERTICAL)
scrolly.pack(side=RIGHT, fill=Y)
details_tree = ttk.Treeview(frame2, columns=('cname', 'phno'), yscrollcommand=scrolly.set)
details_tree.heading('cname', text="Contact Name")
details_tree.heading('phno', text="Number")
details_tree['show'] = 'headings'
details_tree.column('cname', width=100)
details_tree.column('phno', width=100)

scrolly.config(command=details_tree.yview)
details_tree.pack(fill=BOTH, expand=1)

def add():
    if name.get()=="":
        messagebox.showerror("Error","Name is required")
    elif ph_no.get()=="":
        messagebox.showerror("Error","Phone number is required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='Poojita12345@', db='contact_book')
        cur = con.cursor()
        cur.execute("select * from details where cname=%s",name.get())
        row = cur.fetchone()
        if (row != None):
            messagebox.showerror("Error", "Name already exists in record")
        else:
            sql = "insert into details (cname,phno) values (%s,%s)"
            val=(name.get(),ph_no.get())
            cur.execute(sql,val)
            con.commit()
            messagebox.showinfo("Success","Phonenumber added to the records")
            name.set("")
            ph_no.set("")
            show()

def update():
    if name.get()=="":
        messagebox.showerror("Error","Name is required")
    if ph_no.get()=="":
        messagebox.showerror("Error","Ph No. is required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='Poojita12345@', db='contact_book')
        cur = con.cursor()
        cur.execute("select * from details where cname=%s",name.get())
        row = cur.fetchone()
        if (row != None):
            sql = "update details set phno=%s where cname=%s"
            val = (ph_no.get(),name.get())
            cur.execute(sql, val)
            con.commit()
            messagebox.showinfo("Success", "Phonenumber updated in the records")
            name.set("")
            ph_no.set("")
            show()
        else:
            messagebox.showerror("Error", "Name doesn't exists in record")

def delete():
    if name.get()=="":
        messagebox.showerror("Error","Name is required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='Poojita12345@', db='contact_book')
        cur = con.cursor()
        cur.execute("select * from details where cname=%s",name.get())
        row = cur.fetchone()
        if (row != None):
            sql = "delete from details where cname=%s"
            val = (name.get())
            cur.execute(sql, val)
            con.commit()
            messagebox.showinfo("Success", "Phonenumber deleted to the records")
            name.set("")
            ph_no.set("")
            show()

        else:
            messagebox.showerror("Error", "Name doesn't exists in record")

def show():
    for i in details_tree.get_children():
        details_tree.delete(i)
    try:
        con = pymysql.connect(host='localhost', user='root', password='Poojita12345@', db='contact_book')
        cur = con.cursor()
        cur.execute("select * from details")
        row = cur.fetchall()
        for i in row:
            details_tree.insert('', END, values=i)
        con.close()
    except EXCEPTION as ex:
        messagebox.showerror("Error", f'Error due to {str(ex)}')

def search():
    if name.get() == "":
        messagebox.showerror("Error", "Name is required")
    else:
        con = pymysql.connect(host='localhost', user='root', password='Poojita12345@', db='contact_book')
        cur = con.cursor()
        cur.execute("select * from details where cname=%s", name.get())
        row = cur.fetchone()
        if (row != None):
            name.set(row[0])
            ph_no.set(row[1])
        else:
            messagebox.showerror("Error", "Name doesn't exists in record")

btn_add = Button(frame1,text="Add",command=add)
btn_add.place(x=10,y=170)

update_btn = Button(frame1,text="Update",command=update)
update_btn.place(x=90,y=170)

del_btn = Button(frame1,text="Delete",command=delete)
del_btn.place(x=170,y=170)

search_btn = Button(frame1,text="Search",command=search)
search_btn.place(x=250,y=170)

show()
root.mainloop()

