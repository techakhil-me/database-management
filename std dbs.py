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
        self.d=0
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
            if self.d == 0 :
                self.root.config(bg='#202020')
                MainFrame.config(bg='#202020')
                TitleFrame.config(bg='#181818')
                self.lblTitle.config(bg='#181818', fg='#ABCDEF')
                ButtonFrame.config(bg='#181818')
                DataFrame.config(bg='#181818')
                DataFrameLEFT.config(bg='#181818', fg='ghost white')
                DataFrameRIGHT.config(bg='#181818',fg='ghost white')
                self.lblStdID.config(bg='#181818',fg='ghost white')
                self.txtStdID.config(bg='#505050', fg='ghost white')
                self.lblfna.config(bg='#181818',fg='ghost white')
                self.txtfna.config(bg='#505050', fg='ghost white')
                self.lblsna.config(bg='#181818',fg='ghost white')
                self.txtsna.config(bg='#505050', fg='ghost white')
                self.lblDoB.config(bg='#181818',fg='ghost white')
                self.txtDoB.config(bg='#505050', fg='ghost white')
                self.lblage.config(bg='#181818',fg='ghost white')
                self.txtage.config(bg='#505050', fg='ghost white')
                self.lblgen.config(bg='#181818',fg='ghost white')
                self.txtgen.config(bg='#505050', fg='ghost white')
                self.lbladr.config(bg='#181818',fg='ghost white')
                self.txtadr.config(bg='#505050', fg='ghost white')
                self.lblMobile.config(bg='#181818',fg='ghost white')
                self.txtMobile.config(bg='#505050', fg='ghost white')
                self.btndarktheme.config(text='Light theme',bg='#101010',fg='ghost white')
                self.btnAddData.config(bg='#101010',fg='ghost white')
                self.btnDisplayData.config(bg='#101010',fg='ghost white')
                self.btnClearData.config(bg='#101010',fg='ghost white')
                self.btnSearchData.config(bg='#101010',fg='ghost white')
                self.btnDeleteData.config(bg='#101010',fg='ghost white')
                self.btnUpdateData.config(bg='#101010',fg='ghost white')
                self.btnExit.config(bg='#101010',fg='ghost white')
                studentlist.config(bg='#505050', fg='ghost white')
                self.d += 1
            else:
                self.root.config(bg='cadet blue')
                MainFrame.config(bg='cadet blue')
                TitleFrame.config(bg='ghost white')
                self.lblTitle.config(bg='white', fg='black')
                ButtonFrame.config(bg='ghost white')
                DataFrame.config(bg='cadet blue')
                DataFrameLEFT.config(bg='ghost white', fg='black')
                DataFrameRIGHT.config(bg='ghost white', fg='black')
                self.lblStdID.config(bg='ghost white', fg='black')
                self.txtStdID.config(bg='white', fg='black')
                self.lblfna.config(bg='ghost white', fg='black')
                self.txtfna.config(bg='white', fg='black')
                self.lblsna.config(bg='ghost white', fg='black')
                self.txtsna.config(bg='white', fg='black')
                self.lblDoB.config(bg='ghost white', fg='black')
                self.txtDoB.config(bg='white', fg='black')
                self.lblage.config(bg='ghost white', fg='black')
                self.txtage.config(bg='white', fg='black')
                self.lblgen.config(bg='ghost white', fg='black')
                self.txtgen.config(bg='white', fg='black')
                self.lbladr.config(bg='ghost white', fg='black')
                self.txtadr.config(bg='white', fg='black')
                self.lblMobile.config(bg='ghost white', fg='black')
                self.txtMobile.config(bg='white', fg='black')
                self.btndarktheme.config(text='Dark theme',bg='ghost white',fg='black')
                self.btnAddData.config(bg='ghost white',fg='black')
                self.btnDisplayData.config(bg='ghost white',fg='black')
                self.btnClearData.config(bg='ghost white',fg='black')
                self.btnSearchData.config(bg='ghost white',fg='black')
                self.btnDeleteData.config(bg='ghost white',fg='black')
                self.btnUpdateData.config(bg='ghost white',fg='black')
                self.btnExit.config(bg='ghost white',fg='black')
                studentlist.config(bg='white', fg='black')
                self.d -= 1


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
            DisplayData()
        def addData():
            if (len(StdID.get())!=0):
                std_dbs.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address_.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(), Gender.get(),Address_.get(),Mobile.get()))
            DisplayData()
            
        def entered(event, btn):
            if self.d == 0:
                exec(str(btn)+".config(bg='#a6a6a6', fg='ghost white')")
            if self.d == 1:
                exec(str(btn)+".config(bg='#a6a6a6', fg='black')")

        def left(event, btn):
            if self.d==1:
                exec(str(btn)+".config(bg='#101010', fg='ghost white')")
            if self.d == 0:
                exec(str(btn)+".config(bg='ghost white', fg='black')")



        #===================================MainFrame================================#
        
        MainFrame = Frame(self.root, bg='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=20, pady=8, bg='ghost white', relief = RIDGE)
        TitleFrame.pack(side=TOP)


        self.lblTitle = Label(TitleFrame, font=('arial',47,'bold'),text='Student Database Management System')
        self.lblTitle.grid(sticky=W)

        ButtonFrame =Frame(MainFrame, bd=1, width=1350, height=70, padx=40, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=2, width=1350, height=40, padx=40, pady=10, bg='cadet blue', relief=RIDGE)
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
        self.btnAddData.bind('<Enter>', lambda event :entered(event, 'self.btnAddData'))
        self.btnAddData.bind('<Leave>', lambda event :left(event, 'self.btnAddData'))
     
        self.btnDisplayData = Button(ButtonFrame, text="Display",font=('arial',20,'bold'),height=1,width=10, bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        self.btnDisplayData.bind('<Enter>', lambda event: entered(event, 'self.btnDisplayData'))
        self.btnDisplayData.bind('<Leave>', lambda event: left(event, 'self.btnDisplayData'))

        self.btnClearData = Button(ButtonFrame, text="Clear ",font=('arial',20,'bold'),height=1,width=10, bd=4, command= clearData)
        self.btnClearData.grid(row=0,column=2)
        self.btnClearData.bind('<Enter>', lambda event: entered(event, 'self.btnClearData'))
        self.btnClearData.bind('<Leave>', lambda event: left(event, 'self.btnClearData'))

        self.btnSearchData = Button(ButtonFrame, text="Search",font=('arial',20,'bold'),height=1,width=10, bd=4, command= searchDatabase)
        self.btnSearchData.grid(row=0,column=3)
        self.btnSearchData.bind('<Enter>', lambda event: entered(event, 'self.btnSearchData'))
        self.btnSearchData.bind('<Leave>', lambda event: left(event, 'self.btnSearchData'))

        
        self.btnDeleteData = Button(ButtonFrame, text="Delete",font=('arial',20,'bold'),height=1,width=10, bd=4,command= DeleteData)
        self.btnDeleteData.grid(row=0,column=4)
        self.btnDeleteData.bind('<Enter>', lambda event: entered(event, 'self.btnDeleteData'))
        self.btnDeleteData.bind('<Leave>', lambda event: left(event, 'self.btnDeleteData'))

        self.btnUpdateData= Button(ButtonFrame, text="Update",font=('arial',20,'bold'),height=1,width=10, bd=4,command= update)
        self.btnUpdateData.grid(row=0,column=5)
        self.btnUpdateData.bind('<Enter>', lambda event: entered(event, 'self.btnUpdateData'))
        self.btnUpdateData.bind('<Leave>', lambda event: left(event, 'self.btnUpdateData'))

        self.btnExit = Button(ButtonFrame, text="Exit",font=('arial',20,'bold'),height=1,width=10, bd=4, command = iExit)
        self.btnExit.grid(row=0,column=6)
        self.btnExit.bind('<Enter>', lambda event: entered(event, 'self.btnExit'))
        self.btnExit.bind('<Leave>', lambda event: left(event, 'self.btnExit'))

        self.btndarktheme = Button(MainFrame, text="Dark Theme",font=('arial',20,'bold'), command = darktheme)
        self.btndarktheme.pack()
        self.btndarktheme.bind('<Enter>', lambda event: entered(event, 'self.btndarktheme'))
        self.btndarktheme.bind('<Leave>', lambda event: left(event, 'self.btndarktheme'))

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
