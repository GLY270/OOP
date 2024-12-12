from tkinter import *
import sqlite3

root = Tk()
root.title('Loan_payment')
root.geometry("900x900")
root.config(bg='#d3d3d3')  

conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')

c = conn.cursor()

def submit():
    conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')
    c = conn.cursor()
    c.execute("INSERT INTO Loan_payment VALUES(:fname, :lname, :address, :number, :paydate, :amount)",
              {
                  'fname': fname.get(),
                  'lname': lname.get(),
                  'address': address.get(),
                  'number': number.get(),
                  'paydate': paydate.get(),
                  'amount': amount.get(),
              })
    
    fname.delete(0, END)
    lname.delete(0, END)
    address.delete(0, END)
    number.delete(0, END)
    paydate.delete(0, END)
    amount.delete(0, END)
    
    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Loan_payment")
    records = c.fetchall()
    
    print_records = ''
    for record in records:
        print_records += (f"First Name: {record[0]}  /  Last Name: {record[1]}  /  Address: {record[2]}  / "
                          f"Phone Number: {record[3]}  / Pay Date: {record[4]}  / Amount: {record[5]}\n")
    
    query_label.config(text=print_records)
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')
    c = conn.cursor()
    c.execute("DELETE FROM Loan_payment WHERE oid=" + delete_box.get())
    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute(""" UPDATE Loan_payment SET
    fname=:first,
    lname=:last,
    address=:address,
    number=:number,
    paydate=:paydate,
    amount=:amount
    WHERE oid=:oid""",
    {
        'first': fname_editor.get(),
        'last': lname_editor.get(),
        'address': address_editor.get(),
        'number': number_editor.get(),
        'paydate': paydate_editor.get(),
        'amount': amount_editor.get(),
        'oid': record_id
    })
    conn.commit()
    conn.close()

def edit():
    editor = Tk()
    editor.title('Update Record from Database')
    editor.geometry("700x700")
    
    
    editor.config(bg='#d3d3d3')  
    
    conn = sqlite3.connect('D:/SIDAYA/Loan_payment.db')
    c = conn.cursor()
    
    record_id = delete_box.get()
    c.execute("SELECT * FROM Loan_payment WHERE oid=" + record_id)
    records = c.fetchall()
    
    global fname_editor, lname_editor, address_editor, number_editor, paydate_editor, amount_editor
    fname_editor = Entry(editor, width=30)
    fname_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    
    
    fname_editor.config(bg='white')  
    
    lname_editor = Entry(editor, width=30)
    lname_editor.grid(row=1, column=1, padx=20)
    
    lname_editor.config(bg='white')  
    
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
   
   
    address_editor.config(bg='white')  
    
    number_editor = Entry(editor, width=30)
    number_editor.grid(row=3, column=1, padx=20)
   
   
    number_editor.config(bg='white')  
    
    paydate_editor = Entry(editor, width=30)
    paydate_editor.grid(row=4, column=1, padx=20)

   
    amount_editor = Entry(editor, width=30)
    amount_editor.grid(row=5, column=1, padx=20)

   
    amount_editor.config(bg='white')  

    fname_label = Label(editor, text="First Name", bg='pink')
    fname_label.grid(row=0, column=0)
   
    lname_label = Label(editor, text="Last Name", bg='pink')
    lname_label.grid(row=1, column=0)
   
    address_label = Label(editor, text="Address", bg='pink')
    address_label.grid(row=2, column=0)
   
    number_label = Label(editor, text="Number", bg='pink')
    number_label.grid(row=3, column=0)
   
    paydate_label = Label(editor, text="Paydate", bg='pink')
    paydate_label.grid(row=4, column=0)

    amount_label = Label(editor, text="Amount", bg='pink')
    amount_label.grid(row=5, column=0)

    for record in records:
       fname_editor.insert(0, record[0])
       lname_editor.insert(0, record[1])
       address_editor.insert(0, record[2])
       number_editor.insert(0, record[3])
       paydate_editor.insert(0, record[4])
       amount_editor.insert(0, record[5])
   
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=(10),ipadx=(140))


fname = Entry(root,width=30,bg='#d3d3d3')
fname.grid(row=0,column=1,padx=(20))

lname = Entry(root,width=30,bg='#d3d3d3')
lname.grid(row=1,column=1,padx=(20))

address = Entry(root,width=30,bg='#d3d3d3')
address.grid(row=2,column=1,padx=(20))

number = Entry(root,width=30,bg='#d3d3d3')
number.grid(row=3,column=1,padx=(20))

paydate = Entry(root,width=30,bg='#d3d3d3')
paydate.grid(row=4,column=1,padx=(20))

amount = Entry(root,width=30,bg='#d3d3d3')
amount.grid(row=5,column=1,padx=(20))

delete_box = Entry(root,width=(30))
delete_box.grid(row=(10),column=(1),padx=(30))


fname_label = Label(root,text="First Name",bg='white')
fname_label.grid(row=(0),column=(0))

lname_label = Label(root,text="Last Name",bg='white')
lname_label.grid(row=(1),column=(0))

address_label = Label(root,text="Address",bg='white')
address_label.grid(row=(2),column=(0))

number_label = Label(root,text="Number",bg='white')
number_label.grid(row=(3),column=(0))

paydate_label = Label(root,text="Paydate",bg='white')
paydate_label.grid(row=(4),column=(0))

amount_label = Label(root,text="Amount",bg='white')
amount_label.grid(row=(5),column=(0))

submit_btn = Button(root,text="Add Record to Database",command=submit,bg='Pink')  
submit_btn.grid(row=(6),columnspan=(2),pady=(10),padx=(10),ipadx=(100))

edit_btn = Button(root,text="Edit Record",command=edit,bg='Pink')  
edit_btn.grid(row=(8),columnspan=(2),pady=(10),padx=(10),ipadx=(136))

query_btn = Button(root,text="Show Records",command=query,bg='Pink')  
query_btn.grid(row=(7),columnspan=(2),pady=(10),padx=(10),ipadx=(137))

delete_btn = Button(root,text="Delete Records",command=delete,bg='Pink')  
delete_btn.grid(row=(12),columnspan=(2),pady=(10),padx=(10),ipadx=(136))

delete_box_label = Label(root,text="Select ID No.",bg='Light gray')
delete_box_label.grid(row=(10),column=(0))

query_label = Label(root,text="",justify=CENTER,bg='#d3d3d3')  
query_label.grid(row=(13),columnspan=(2))

root.mainloop()
