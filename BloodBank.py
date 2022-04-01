import mysql.connector
from tkinter import *

db=mysql.connector.connect(host="localhost",database="bbms",user="root",password="password")
if db.is_connected():
 print("connected")
else:
 print("error")
cursor=db.cursor()
root = Tk()
root.title("BLOOD BANK")
root.geometry("1080x650")
root.configure(background='white')
l3=Label(root,text="BLOOD BANK SYSTEM",bg='white',font = "Helvetica 15 bold").place(x=450,y=40,w=300,h=40,)
l1=Label(root,text="Click to enter the details of the donor",bg='white',font="Helvetica 12").place(x=80,y=100,w=300,h=40)
b1=Button(root,text="Donor Details",command=lambda : donordetails()).place(x=80,y=150)
l2=Label(root,text="Click to enter the details of the blood",bg='white',font="Helvetica 12").place(x=80,y=200,w=300,h=40)
b2=Button(root,text="Blood Details",command=lambda : blooddetails()).place(x=80,y=250)
l3=Label(root,text="Click to make a request for blood",bg='white',font="Helvetica 12").place(x=80,y=300,w=300,h=40)
b3=Button(root,text="Blood Request",command=lambda : requestblood()).place(x=80,y=350)
b2=Button(root,text="Exit",command=lambda : stop(root)).place(x=80,y=400)
v = StringVar()

def insertDonor(don_id,name,age,gender,address,contactno):
 insert = "INSERT INTO donor VALUES(%s,'%s',%s,'%s','%s',%s);"%(don_id,name,age,gender,address,contactno)
 try:
  cursor.execute(insert)
  db.commit()
 except:
  db.rollback()

def insertBlood(don_id,bloodgroup,platelet,rbc):
 insert= "INSERT INTO blood VALUES(%s,'%s',%s,%s,CURDATE());"%(don_id,bloodgroup,platelet,rbc)

 try:
  cursor.execute(insert)
  db.commit()
 except:
  db.rollback()

def retrieve(bg):
 request="select * from donor inner join blood using(don_id) where bloodgroup='%s';"%(bg)

 try:
  cursor.execute(request)
  rows=cursor.fetchall()
  db.commit()
  print(len(rows))
  return rows
 except:
  db.rollback()

def donordetails():
 root=Toplevel()
 root.title("BLOOD BANK")
 root.geometry("1024x600")
 root.configure(background ='#FF8F8F')
 l1=Label(root,text="Name:",bg='white',font="Helvetica 12").place(x=40,y=40)
 l2=Label(root,text="Age:",bg='white',font="Helvetica 12").place(x=40,y=80)
 l3=Label(root,text="Gender:",bg='white',font="Helvetica 12").place(x=40,y=120)
 l4=Label(root,text="Address:",bg='white',font="Helvetica 12").place(x=40,y=220)
 l5=Label(root,text="Contact:",bg='white',font="Helvetica 12").place(x=40,y=260)

 e1=Entry(root)
 e1.place(x=120,y=40)
 e2=Entry(root)
 e2.place(x=120,y=80)
 e3=Entry(root)
 e3.place(x=120,y=120)
 e4=Entry(root)
 e4.place(x=120,y=220)
 e5=Entry(root)
 e5.place(x=120,y=260)

 slno="SELECT COUNT(*) FROM donor;"
 cursor.execute(slno)
 x=cursor.fetchall()
 no=x[0][0]
 no=no+1

 b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=300)

 b1=Button(root,text="Submit",command=lambda :
 insertDonor(no,e1.get(),e2.get(),e3.get(),e4.get(),e5.get())).place(x=40,y=300)

 root.mainloop()

def blooddetails():
 root=Tk()
 root.title("BLOOD BANK")
 root.geometry("1024x600")
 root.configure(background ='#FF8F8F')
 l1=Label(root,text="Blood Group:",font="Helvetica 12").place(x=40,y=40,w=250,h=20)
 l2=Label(root,text="PLatetelet count (in 100 thousands):",font="Helvetica12").place(x=40,y=80,w=250,h=20)
 l3=Label(root,text="RBC count (in millions):",font="Helvetica 12").place(x=40,y=120,w=250,h=20)
 e1=Entry(root)
 e1.place(x=350,y=40)

 e2=Entry(root)
 e2.place(x=350,y=80)
 e3=Entry(root)
 e3.place(x=350,y=120)

 slno="SELECT COUNT(*) FROM blood;"
 cursor.execute(slno)
 x=cursor.fetchall()
 no=x[0][0]
 no=no+1

 b2=Button(root,text="Back",command=lambda : stop(root)).place(x=200,y=160)
 b1=Button(root,text="Submit",command=lambda :
 insertBlood(no,e1.get(),e2.get(),e3.get())).place(x=40,y=160)

 root.mainloop()

def grid1(bg):
 root=Tk()
 root.title("LIST OF MATCHING DONORS")
 root.geometry("860x500")
 root.configure(background='#0C43F0')
 rows=retrieve(bg)
 x=0
 for row in rows:
  l1=Label(root,text=row[0],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l2=Label(root,text=row[1],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l3=Label(root,text=row[2],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l4=Label(root,text=row[3],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l5=Label(root,text=row[4],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)

  l6=Label(root,text=row[5],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l7=Label(root,text=row[6],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=6,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l8=Label(root,text=row[7],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=7,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l9=Label(root,text=row[8],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=8,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
  l10=Label(root,text=row[9],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=9,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)

  x=x+1
 root.mainloop()

def requestblood():
 root=Tk()
 root.title("BLOOD BANK")
 root.geometry("1024x600")
 root.configure(background='#FF8F8F')
 l=Label(root,text="Enter the blood group").place(x=50,y=50,w=400,h=40)
 e=Entry(root)
 e.place(x=500,y=50)
 b2=Button(root,text="Back",command=lambda : stop(root)).place(x=600,y=100)
 b=Button(root,text="ENTER",command=lambda : grid1(e.get())).place(x=500,y=100)
 root.mainloop()

def stop(root):
 root.destroy()

 root.mainloop()
