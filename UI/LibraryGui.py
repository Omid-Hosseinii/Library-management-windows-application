import sys
sys.path.insert(0, 'C:/Users/Omid/Desktop/library app')
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter as tk
#________________________________________________________________________________________


class Library_Gui:
    def open_form_size(self,master,width,height):
        w=width
        h=height
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        master.geometry("%dx%d+%d+%d" %(w,h,x,y))

    def __init__(self):
        self.root=Tk()
        self.open_form_size(self.root,825,550)
        self.root.title('نرم افزار کتابداری')   
        self.root.iconbitmap('UI//images//ico//libraryicon.ico')
        self.root.resizable(0,0)

        bg = PhotoImage(file = "UI//images//png//library.png")
        canvas1 = Canvas( self.root, width = 825,height = 550)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0,image=bg,anchor="nw")

        self.welcomeLabel=Label(self.root,text='به نرم افزار مدیریت کتابخانه خوش آمدید',bg='#E97611',fg='white',font=('tahoma',17))
        self.welcomeLabel.place(x=232,y=45)  

        self.btn1=Button(self.root,text='ثبت کتاب جدید',relief=RAISED)
        self.btn1.place(x=150,y=300)   
        self.btn1.bind('<Button>',lambda event : self.addBook(event))

        self.root.mainloop()  


    #------------------------------------------------------------------------------------------
    def addBook(self,event):
        pass       

#____________________________________________________________________________________________
