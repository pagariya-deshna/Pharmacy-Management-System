from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1300x800")

        # addMed variable
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        # main variable
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        self.lbltitle = Label(self.root, text="    PHARMACY MANAGEMENT SYSTEM", bd=10, relief=RIDGE, bg='white', fg="darkblue", font=("times new roman", 48, "bold"), padx=2, pady=4)
        self.lbltitle.pack(side=TOP, fill=X)

        img1=Image.open("C:\\pharmacyManagement\\logo.png")
        img1=img1.resize((75,75),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=10,y=10)

        DataFrame = Frame(self.root, bd=10, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=105, width=1275, height=365)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=750,height=340)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=760,y=5,width=450,height=340)

	#buttonFrame
        ButtonFrame=Frame(self.root,bd=10,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=460,width=1275,height=55)

	#Main button
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),width=11,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)
        btnUpdateData=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",13,"bold"),width=11,bg="darkgreen",fg="white")
        btnUpdateData.grid(row=0,column=1)
        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",13,"bold"),width=11,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)
        btnRestMed=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",13,"bold"),width=11,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)
        btnExitMed=Button(ButtonFrame,command=self.close,text="EXIT",font=("arial",13,"bold"),width=11,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

	#searchBy
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        # variable
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",13,"bold"),state="readonly")
        search_combo["values"]=("refno","medname","lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        textSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textSearch.grid(row=0,column=7)

        searchButton=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),width=9,bg="darkgreen",fg="white")
        searchButton.grid(row=0,column=8)
        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),width=9,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
    
        # label and entry
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=10,font=("arial",17,"bold"),state="readonly")
        ref_combo["values"]=row
        if row:
            ref_combo.current(0)
        ref_combo.grid(row=0,column=1)

        lblCompanyName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name",padx=2,pady=6)
        lblCompanyName.grid(row=1,column=0,sticky=W) 
        textCompanyName=Entry(DataFrameLeft,textvariable=self.cmpName_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textCompanyName.grid(row=1,column=1)

        lblTypeOfMed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine",padx=2)
        lblTypeOfMed.grid(row=2,column=0,sticky=W)

        comTypeOfMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=10,font=("arial",17,"bold"),state="readonly")
        comTypeOfMedicine["value"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injections")
        comTypeOfMedicine.grid(row=2,column=1)
        comTypeOfMedicine.current(0)
       
        #AddMedicine
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=15,font=("arial",12,"bold"),state="readonly")
        comMedicineName["values"]=med
        if med:
            comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No.",padx=2)
        lblLotNo.grid(row=4,column=0,sticky=W)
        textLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        textIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2)
        lblExDate.grid(row=6,column=0,sticky=W)
        textExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textExDate.grid(row=6,column=1)
        
        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2)
        lblUses.grid(row=7,column=0,sticky=W)
        textUses=Entry(DataFrameLeft,textvariable=self.uses_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textUses.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        textSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,bd=2,relief=RIDGE,width=12,font=("arial",17,"bold"))
        textSideEffect.grid(row=8,column=1)
       
        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=2)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        textPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,bd=2,relief=RIDGE,width=29,font=("arial",12,"bold"))
        textPrecWarning.grid(row=0,column=3)
        
        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        textDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,bd=2,relief=RIDGE,width=29,font=("arial",12,"bold"),bg="white")
        textDosage.grid(row=1,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        textPrice=Entry(DataFrameLeft,textvariable=self.price_var,bd=2,relief=RIDGE,width=29,font=("arial",12,"bold"))
        textPrice.grid(row=2,column=3)
        
        lblProductQT=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQT.grid(row=3,column=2,sticky=W)
        textProductQT=Entry(DataFrameLeft,textvariable=self.product_var,bd=2,relief=RIDGE,width=29,font=("arial",12,"bold"))
        textProductQT.grid(row=3,column=3,sticky=W)
       
                #Images 
        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Safe Stay Healthy",padx=2,pady=6,bg="white",fg="red",width=39)
        lblhome.place(x=314,y=140)
       
        img2=Image.open("C:\\pharmacyManagement\\research.jpeg")
        img2=img2.resize((150,125),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=620,y=316)

        img3=Image.open("C:\\pharmacyManagement\\photo.jpg")
        img3=img3.resize((150,125),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=500,y=316)

        img4=Image.open("C:\\pharmacyManagement\\test.jpeg")
        img4=img4.resize((150,125),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=380,y=316)

                #dataFrameRight
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=760,y=5,width=450,height=340)

        img5=Image.open("C:\\pharmacyManagement\\medicine1.jpg")
        img5=img5.resize((200,75),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=810,y=140)

        img6=Image.open("C:\\pharmacyManagement\\medicine1.jpg")
        img6=img6.resize((150,75),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1000,y=140)

        img7=Image.open("C:\\pharmacyManagement\\tab.png")
        img7=img7.resize((145,145),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=1085,y=140)
        
        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No.:")
        lblrefno.place(x=0,y=80)
        textrefno=Entry(DataFrameRight,textvariable=self.refMed_var,bd=2,relief=RIDGE,width=11,font=("arial",15,"bold"))
        textrefno.place(x=125,y=80)
            
        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblmedName.place(x=0,y=110)
        textmedName=Entry(DataFrameRight,textvariable=self.addmed_var,bd=2,relief=RIDGE,width=11,font=("arial",15,"bold"))
        textmedName.place(x=125,y=110)
        
            #side frame
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=261,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
    
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=80)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #Medicine Add Button
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=270,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",12,"bold"),width=12,bg="lime",fg="white",pady=4,command=self.AddMed)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",12,"bold"),width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",12,"bold"),width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",12,"bold"),width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)

         #Frame details
        Framedetails=Frame(self.root,bd=10,relief=RIDGE)
        Framedetails.place(x=0,y=505,width=1275,height=210)

        #Main table and scroll bar
        Table_frame=Frame(Framedetails,bd=10,relief=RIDGE)
        Table_frame.place(x=0,y=1,width=1250,height=145)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)        
        scroll_y.pack(side=RIGHT,fill=Y)  

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=92)
        self.pharmacy_table.column("companyname",width=92)
        self.pharmacy_table.column("type",width=93)
        self.pharmacy_table.column("tabletname",width=92)
        self.pharmacy_table.column("lotno",width=92)
        self.pharmacy_table.column("issuedate",width=92)
        self.pharmacy_table.column("expdate",width=92)
        self.pharmacy_table.column("uses",width=92)
        self.pharmacy_table.column("sideeffect",width=92)
        self.pharmacy_table.column("warning",width=92)
        self.pharmacy_table.column("dosage",width=92)
        self.pharmacy_table.column("price",width=92)
        self.pharmacy_table.column("productqt",width=92)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

        # Add Medicine functionality declaration

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(self.refMed_var.get(),self.addmed_var.get()))
        
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor
        conn.close()
        messagebox.showinfo("Success","Medicine Added")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #MedGetCursor
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(self.addmed_var.get(),self.refMed_var.get()))

        conn.commit()
        self.fetch_dataMed()
        conn.close()

        messagebox.showinfo("Success","Medicine has been Updated")

    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        
        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        self.refMed_var.set("")
        self.addmed_var.set("")
        
        messagebox.showinfo("Success","Medicine has been Deleted")

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

        # Main table
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are reqired")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref_var.get(),self.cmpName_var.get(),self.typeMed_var.get(),self.medName_var.get(),self.lot_var.get(),self.issuedate_var.get(),self.expdate_var.get(),self.uses_var.get(),self.sideEffect_var.get(),self.warning_var.get(),self.dosage_var.get(),self.price_var.get(),self.product_var.get()))


        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","data has been inserted")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        if row:
            self.ref_var.set(row[0])
            self.cmpName_var.set(row[1])
            self.typeMed_var.set(row[2])
            self.medName_var.set(row[3])
            self.lot_var.set(row[4])
            self.issuedate_var.set(row[5])
            self.expdate_var.set(row[6])
            self.uses_var.set(row[7])
            self.sideEffect_var.set(row[8])
            self.warning_var.set(row[9])
            self.dosage_var.set(row[10])
            self.price_var.set(row[11])
            self.product_var.set(row[12])
        else:
            pass

    def update_data(self):
        if self.ref_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where refno=%s",(self.cmpName_var.get(),self.typeMed_var.get(),self.medName_var.get(),self.lot_var.get(),self.issuedate_var.get(),self.expdate_var.get(),self.uses_var.get(),self.sideEffect_var.get(),self.warning_var.get(),self.dosage_var.get(),self.price_var.get(),self.product_var.get(),self.ref_var.get()))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("UPDATE","Record has been Updated successfully")

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("DELETE","Record Deleted successfully")

    def reset(self):
        #self.ref_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
        #self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set(r"")
        self.price_var.set(r"")
        self.product_var.set(r"")

    def search_data(self):   
        conn=mysql.connector.connect(host="localhost",username="root",password="deshna_123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM pharmacy WHERE " + self.search_var.get() + " LIKE '%" + self.searchTxt_var.get() + "%'")
        #my_cursor.execute("select * from pharmacy where "+ self.search_var.get() + " LIKE " +(self.searchTxt_var.get())+"%")
        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def close(self):
        exit()

if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
