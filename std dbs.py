# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:43:07 2020

@author: admin
"""

# Frontend
from tkinter import *
import tkinter.messagebox
import inspect
import std_dbs

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.iconbitmap('Student.ico') 
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='cadet blue')
        
        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address_ = StringVar()
        Mobile = StringVar()
        #===================================Function Declaration==================================
        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            
            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtsna.delete(0,END)
            self.txtsna.insert(END,sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END,sd[4])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[5])      
            self.txtgen.delete(0,END)
            self.txtgen.insert(END,sd[6])
            self.txtadr.delete(0,END)
            self.txtadr.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])

        def darktheme():
            global xs
            xs = inspect.sys._getframe(1)
            print(xs)
            pass



        def iExit():
            iExit= tkinter.messagebox.askyesno("Students Database Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
            
        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtage.delete(0,END)
            self.txtgen.delete(0,END)
            self.txtadr.delete(0,END)
            self.txtMobile.delete(0,END)
        
       
        def DisplayData():
            studentlist.delete(0,END)
            for row in std_dbs.viewData():
                studentlist.insert(END,row,str(""))

            
        def DeleteData():
            if(len(StdID.get())!=0):
                std_dbs.deleteRec(sd[0])
                clearData()
                DisplayData()
                
        def searchDatabase():
            studentlist.delete(0,END)
            for row in std_dbs.searchData(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(), Address_.get(),Mobile.get()):
                studentlist.insert(END,row,str(""))
            
        def update():
            if(len(StdID.get())!=0):
                std_dbs.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                std_dbs.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address_.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get() , Firstname.get() , Surname.get(),DoB.get(),Age.get(),Gender.get(),Address_.get(),Mobile.get()))
       
        def addData():
            if (len(StdID.get())!=0):
                std_dbs.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address_.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(), Gender.get(),Address_.get(),Mobile.get()))
                    
            
        def entered(event):
            self.btnAddData.config(bg='#343434', fg='#ffffff')

        def left(event):
            self.btnAddData.config(bg='#ffffff', fg='#000000')



        #===================================MainFrame================================#
        
        MainFrame = Frame(self.root, bg='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=20, pady=8, bg='ghost white', relief = RIDGE)
        TitleFrame.pack(side=TOP)


        self.lblTitle = Label(TitleFrame, font=('arial',47,'bold'),text='Student Database Management System')
        self.lblTitle.grid(sticky=W)

        ButtonFrame =Frame(MainFrame, bd=2, width=1350, height=70, padx=18,pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=1, width=1350, height=400, padx=40, pady=20, bg='cadet blue', relief=RIDGE )
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE , font=('arial',20,'bold'), text='Student Information', bg='Ghost White')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady=3, relief=RIDGE ,bg='Ghost White', font=('arial',20,'bold'), text='Student Details')
        DataFrameRIGHT.pack(side=RIGHT)
         
        #__________________________________________________________Labels and Entries_______________________________________________________-
        
        self.lblStdID = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Student ID:', padx=2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=StdID,width=39)
        self.txtStdID.grid(row=0,column=1)
        
        self.lblfna = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Firstname:', padx=2,pady=2,bg="Ghost White")
        self.lblfna.grid(row=1,column=0,sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Firstname,width=39)
        self.txtfna.grid(row=1,column=1)
        
        self.lblsna = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Surname:', padx=2,pady=2,bg="Ghost White")
        self.lblsna.grid(row=2,column=0,sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Surname,width=39)
        self.txtsna.grid(row=2,column=1)
        
        self.lblDoB = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Date of Birth:', padx=2,pady=3,bg="Ghost White")
        self.lblDoB.grid(row=3,column=0,sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=DoB,width=39)
        self.txtDoB.grid(row=3,column=1)
        
        self.lblage = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Age:', padx=2,pady=3,bg="Ghost White")
        self.lblage.grid(row=4,column=0,sticky=W)
        self.txtage = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Age ,width=39)
        self.txtage.grid(row=4,column=1)
        
        self.lblgen = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Gender:', padx=2,pady=3,bg="Ghost White")
        self.lblgen.grid(row=5,column=0,sticky=W)
        self.txtgen = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable= Gender ,width=39)
        self.txtgen.grid(row=5,column=1)
        
        self.lbladr = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Address_:', padx=2,pady=3,bg="Ghost White")
        self.lbladr.grid(row=6,column=0,sticky=W)
        self.txtadr = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Address_ ,width=39)
        self.txtadr.grid(row=6,column=1)
        
        self.lblMobile = Label(DataFrameLEFT, font=('arial',20,'bold'),text='Mobile:', padx=2,pady=3,bg="Ghost White")
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial',20,'bold'),textvariable=Mobile,width=39)
        self.txtMobile.grid(row=7,column=1)


        #===================================List and scroll bar widget================================#
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        studentlist= Listbox(DataFrameRIGHT, width=41, height=16, font=('arial',12,'bold'), yscrollcommand =scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0,column=0, padx=8)
        scrollbar.config(command= studentlist.yview)
        
        #===================================Button Widget===================================#===================================
        self.btnAddData = Button(ButtonFrame, text="Add new",font=('arial',20,'bold'),height=1,width=10, bd=4, command= addData)
        self.btnAddData.grid(row=0,column=0)
        self.btnAddData.bind('<Enter>', entered)
        self.btnAddData.bind("<Leave>", left)
     
        self.btnDisplayData = Button(ButtonFrame, text="Display",font=('arial',20,'bold'),height=1,width=10, bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        
        self.btnClearData = Button(ButtonFrame, text="Clear ",font=('arial',20,'bold'),height=1,width=10, bd=4, command= clearData)
        self.btnClearData.grid(row=0,column=2)
        
        self.btnSearchData = Button(ButtonFrame, text="Search",font=('arial',20,'bold'),height=1,width=10, bd=4, command= searchDatabase)
        self.btnSearchData.grid(row=0,column=3)
        
        self.btnDeleteData = Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),height=1,width=10, bd=4,command= DeleteData)
        self.btnDeleteData.grid(row=0,column=4)
        
        self.btnUpdateData= Button(ButtonFrame, text="Update",font=('arial',20,'bold'),height=1,width=10, bd=4,command= update)
        self.btnUpdateData.grid(row=0,column=5)
        
        self.btnExit = Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),height=1,width=10, bd=4, command = iExit)
        self.btnExit.grid(row=0,column=6)

        self.btndarktheme = Button(MainFrame, text="Dark Theme",font=('arial',20,'bold'), command = darktheme)
        self.btndarktheme.pack()
        

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()