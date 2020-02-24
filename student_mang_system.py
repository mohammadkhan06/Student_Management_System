from tkinter import*
from tkinter import messagebox
import pymysql
from prettytable import from_db_cursor

root=Tk()
root.title("Student Management System")
root.config(bg="thistle3")
root.geometry("900x900")
root.resizable(0, 0)
label = Label(root,text="Welcome to Dezignolics",bg="navy",fg="white",font='Arial 20 normal',relief="ridge",height=1)
label.pack()

#frame=Frame(root,bg="wheat")
#frame.place(x=60,y=200,width=700,height=600)

label1= Label(root,text="Enter Your Details Below: ",bg="thistle3",font='Verdana 15 italic',relief="sunken")
label1.place(x=200,y=70)

def delete():
    entry2_1.delete(0,END)
    entry2_2.delete(0,END)
    entry3.delete(0,END)
    dob_entry.delete(0,END)
    opt.set("Select Your gender")
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    box.delete(0.0,END)

def exitt():
    root.destroy()

"""def s_id():
        db=pymysql.connect(host="localhost",user="root",passwd="",db="student_management_system")
        cur=db.cursor()
        sids=cur.execute("SELECT Roll_No FROM student")
        for s in str(sids):
            if s==entry6.get():
                messagebox.showinfo("Data Already Present!")
                
        
        db.commit()
        db.close()"""
    

def submit():
    db=pymysql.connect(host="localhost",user="root",passwd="",db="student_management_system")
    cur=db.cursor()
    try:
        cur.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
         entry2_1.get(),
         entry2_2.get(),
         entry3.get(),
         dob_entry.get(),
         opt.get(),
         entry6.get(),
         entry5.get(),
         entry4.get(),
         box.get(0.0,END),
    
        )
        )
    except:
        messagebox.showinfo("Error","Data Already Present!")
        
    
    
        
    db.commit()
    db.close()
    #messagebox.showinfo("Data Inserted!", "Data Inserted Successfully!")
    entry2_1.delete(0,END)
    entry2_2.delete(0,END)
    entry3.delete(0,END)
    dob_entry.delete(0,END)
    opt.set("Select Your gender")
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    box.delete(0.0,END)
    
"""def fetch():
    root.withdraw()
    global fetcher
    fetcher=Tk()
    fetcher.title("Student Records")
    fetcher.geometry("700x700")
    db=pymysql.connect(host="localhost",user="root",passwd="",db="student_management_system")
    cur=db.cursor()
    cur.execute("SELECT * FROM student")
    rows= cur.fetchall()
    print_records = ''
    for record in rows:
        print_records += str(record[0]) + "\t" + str(record[1]) + "\t" + str(record[2]) + "\t" + str(record[3]) + "\t" + str(record[4]) + "\t" + str(record[5]) + "\t" + str(record[6]) + "\t" +str(record[7]) + "\t"+str(record[8])
    fetch_label= Label(fetcher,text=print_records)
    fetch_label.place(x=10,y=10)
    
    db.commit()
    db.close()"""


def printed():
    win=Tk()
    win.geometry('1100x11000')
    win.configure(bg="white")
    win.title("DISPLAY")
    entry=Text(win)
    entry.place(x=0,y=0,width=1500,height=500)
    curs=pymysql.connect(host="localhost",user="root",password="",db="student_management_system")
    mycursor=curs.cursor()
    mycursor.execute("SELECT * FROM student ")
    x=from_db_cursor(mycursor)
    entry.insert(INSERT,x)
    
    
def delete():
	
	conn = pymysql.connect(host="localhost",user="root",passwd="",db="student_management_system")
	c =conn.cursor()

	c.execute("DELETE from student WHERE Student_Id = " + entry8.get())

	entry8.delete(0, END)

	conn.commit()
 
	conn.close()
    
    

label2_1=Label(root,text="First Name:",bg="thistle3",font='verdana 10 bold')
label2_1.place(x=200,y=120)
entry2_1=Entry(root,width=35)
entry2_1.place(x=290,y=120)

label2_2=Label(root,text="Last Name:",bg="thistle3",font='verdana 10 bold')
label2_2.place(x=200,y=170)
entry2_2=Entry(root,width=35)
entry2_2.place(x=290,y=170)

label3=Label(root,text="Student-Id:",bg="thistle3",font='verdana  10 bold')
label3.place(x=200,y=220)
entry3=Entry(root,width=35)
entry3.place(x=290,y=220)

dob=Label(root,text="D-O-B:",bg="thistle3",font='verdana 10 bold')
dob.place(x=200,y=270)
dob_entry=Entry(root,width=35)
dob_entry.place(x=290,y=270)

Gender = Label(root,text="Gender:",bg="thistle3",font='verdana 10 bold')
Gender.place(x=200,y=320)
opt=StringVar(root)
opt.set("Select Your gender")
choices= {'Male','Female','Other'}
res = OptionMenu(root,opt,*choices,)
res.place(x=290,y=320)


label6=Label(root,text="Roll_No:",bg="thistle3",font='verdana 10 bold')
label6.place(x=200,y=370)
entry6=Entry(root,width=35)
entry6.place(x=290,y=370)

label5=Label(root,text="Email:",bg="thistle3",font='verdana 10 bold')
label5.place(x=200,y=420)
entry5=Entry(root,width=35)
entry5.place(x=290,y=420)

label4=Label(root,text="Phone-No:",bg="thistle3",font='verdana 10 bold')
label4.place(x=200,y=470)
entry4=Entry(root,width=35)
entry4.place(x=290,y=470)

label7=Label(root,text="Address:",bg="thistle3",font='verdana 10 bold')
label7.place(x=200,y=520)
box=Text(root,width=55,height=4)
box.place(x=200,y=540)


button1=Button(root,text="Clear Entries",height=1,width=12,fg="white",font='verdana 10 bold',relief="groove",bg="navy",command=delete)
button1.place(x=210,y=620)

button2=Button(root,text="Exit",height=1,width=12,fg="white",font='verdana 10 bold',relief="groove",bg="navy",command=exitt)
button2.place(x=510,y=620)

button3=Button(root,text="Submit",height=1,width=12,fg="white",font='verdana 10 bold',relief="groove",bg="navy",command=submit)
button3.place(x=360,y=620)

label8=Label(root,text="Enter Id:",bg="thistle3",font='verdana 10 bold')
label8.place(x=200,y=720)
entry8=Entry(root,width=35)
entry8.place(x=290,y=720)

button2=Button(root,text="Delete Record",height=1,width=12,fg="white",font='verdana 10 bold',relief="groove",bg="navy",command=delete)
button2.place(x=520,y=720)


button4=Button(root,text="Show All Records",height=1,width=25,fg="white",font='verdana 10 bold',relief="ridge",bg="navy",command=printed)
button4.place(x=300,y=670)

root.mainloop()
