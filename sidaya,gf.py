from tkinter import*
import sqlite3

root=Tk()
root.title('Personal info')
root.geometry("500x500")

conn=sqlite3.connect('Personal_info.db')
c=conn.cursor()

def submit():
    conn=sqlite3.connect('C:/Users/STUDENTS/Desktop')
    c=conn.cursor()
    c.execute ("INSERT INTO Student_info VALUES(:f_name,:l_name,:age,:address,:email)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'age':age.get(),
                  'address':address.get(),
                  'email':email.get(),
                  })
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    email.delete(0,END)

def query():
    conn=sqlite3.connect('C:/Users/STUDENTS/Desktop')
    c=conn.cursor()
    c.execute("SELECT*,oid FROM Student_info")
    records=c.fetchall()

    print_records=""
    for record in records:
        print_records+=(record[0])+""+str(record[1])+""+str(record[2])+""+str(record[3])+""+str(record[4])+"\n"

        query_label=Label(root,text=print_records)
        query_label.grid(row=8,column=0,columnspan=2)

    conn.commit()
    conn.close()

def delete():
   conn=sqlite3.connect('C:/Users/STUDENTS/Desktop')
   c=conn.cursor()
   c.execute("Delete from Student_info WHERE oid="+delete_box.get())


   def edit():
       editor=Tk()
       editor.title('Update Record from database')
       editor.geometry("500x500")

       conn=sqlite3.connect('C:/Users/STUDENT6/Desktop/Personal_info.db')

       c=conn.cursor()

   record_id=delete_box.get()
   c.execute("SELECT * FROM student_info WHERE oid="+record_id)
   records=c.fetchall()


   for record in records:
      f_name_editor.insert(0,record[0])
      l_name_editor.insert(0,record[1])
      age_editor.insert(0,record[2])
      address_editor.insert(0,record[3])
      gmail_editor.insert(0,record[4])  
   
'''

c.execute("""CREATE TABLE "Personal_info" (
	"fname"	TEXT,
	"lname"	TEXT,
	"age"	INTEGER,
	"address"	TEXT,
	"email"	TEXT
)""")
'''

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
age=Entry(root,width=30)
age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)
l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
age_name_label=Label(root,text="Age")
age_name_label.grid(row=2,column=0)
address_name_label=Label(root,text="Address")
address_name_label.grid(row=3,column=0)
email_name_label=Label(root,text="Email")
email_name_label.grid(row=4,column=0)

submit_btn=Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

query_btn=Button(root,text="Show records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

query_btn=Button(root,text="Delete Records",command=delete)
query_btn.grid(row=12,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

delete_box=Entry(root,width=30)
delete_box.grid(row=10, column=1, padx=30)
delete_box_label=Label(root,text="Select ID No.")
delete_box_label.grid(row=10,column=0)


root.mainloop()
        
        

    
                 
