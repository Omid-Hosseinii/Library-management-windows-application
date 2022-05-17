### defined module and library
import sys
sys.path.insert(0, 'C:/Users/Omid/Desktop/library app')
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import tkinter as tk
import pyglet
from DatabaseLayer.dbManager import *
from DatabaseLayer.BookModel import *
from ProcessLayer.WeatherApi import *
#-------------------------------------------------------------
###defined custom font
pyglet.font.add_file('font/IRANYekanBlack.ttf')
pyglet.font.add_file('font/IRANYekanBold.ttf')
#________________________________________________________________________________________

class Library_Gui:
### form size function
    def open_form_size(self,master,width,height):
        w=width
        h=height
        ws=self.root.winfo_screenwidth()
        hs=self.root.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        master.geometry("%dx%d+%d+%d" %(w,h,x,y))
### main window ( initial function)
    def __init__(self):
        self.root=Tk()
        self.open_form_size(self.root,825,550)
        self.root.title('نرم افزار کتابداری')   
        self.root.iconbitmap('UI//images//ico//libraryicon.ico')
        self.root.resizable(0,0)


        bg = PhotoImage(file = "UI//images//png//library2.png")
        canvas1 = Canvas( self.root, width = 825,height = 550)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0,image=bg,anchor="nw")



        imgbtn3 = PhotoImage(file = "UI//images//png//btn3.png")
        self.btn3=Button(self.root,image=imgbtn3,relief=RAISED,cursor='hand2')
        self.btn3.place(x=130,y=290)   
        self.btn3.bind('<Button>',lambda event : self.searchBook(event)) 


        imgbtn4 = PhotoImage(file = "UI//images//png//btn4.png")
        self.btn4=Button(self.root,image=imgbtn4,relief=RAISED,cursor='hand2')
        self.btn4.place(x=280,y=290)    
        self.btn4.bind('<Button>',lambda event : self.searchBooks(event))

        imgbtn2 = PhotoImage(file = "UI//images//png//btn2.png")
        self.btn2=Button(self.root,image=imgbtn2,relief=RAISED,cursor='hand2')
        self.btn2.place(x=430,y=290)  
        self.btn2.bind('<Button>',lambda event : self.deleteBook(event))

        imgbtn1 = PhotoImage(file = "UI//images//png//btn1.png")
        self.btn1=Button(self.root,image=imgbtn1,relief=RAISED,cursor='hand2')
        self.btn1.place(x=600,y=290)   
        self.btn1.bind('<Button>',lambda event : self.addBook(event))



        tempTime=get_temperatureTime()        
        l1=Label(self.root,text=tempTime['time'],font=('tahoma',15),bg='#2d2927',fg='white')
        l1.place(x=610,y=514)

        l1=Label(self.root,text=str(tempTime['temp'])+'°',font=('tahoma',15),bg='#2d2927',fg='white')
        l1.place(x=73,y=516)

        self.root.mainloop()  


    #------------------------------------------------------------------------------------------
### add book to database     
    def addBook(self,event):
        win=Toplevel(self.root)
        win.title('درج کتاب')
        win.iconbitmap('UI//images//ico//adddb.ico')      
        self.open_form_size(win,340,230)
        win.resizable(0,0)
        win.configure(background='#527048')



        guideid=Label(win,text='شماره راهنما :',font=('IRANYekanBold',15),bg='#527048',fg='white')
        guideid.grid(row=0,column=0,pady=5)
        guideidEntry=Entry(master=win,width=28)
        guideidEntry.grid(row=0,column=1)

        title=Label(win,text='عنوان :',width=14,font=('IRANYekanBold',15),bg='#527048',fg='white')
        title.grid(row=1,column=0,pady=5)
        titleEntry=Entry(master=win,width=28)
        titleEntry.grid(row=1,column=1)

        creator=Label(win,text='پدیدآور :',width=14,font=('IRANYekanBold',15),bg='#527048',fg='white')
        creator.grid(row=2,column=0,pady=5)
        creatorEntry=Entry(master=win,width=28)
        creatorEntry.grid(row=2,column=1)

        publicationdetail=Label(win,text='مشخصات نشر :',width=14,font=('IRANYekanBold',15),bg='#527048',fg='white')
        publicationdetail.grid(row=3,column=0,pady=5)
        publicationdetailEntry=Entry(master=win,width=28)
        publicationdetailEntry.grid(row=3,column=1)


        addimg=PhotoImage(file = "UI//images//png//adddb2.png")
        btnadd=Button(win,image=addimg,bg='#527048',cursor='hand2')
        btnadd.grid(row=5,column=1,pady=17)
        btnadd.bind('<Button>',lambda event : self.insertDb(event,guideidEntry.get(),titleEntry.get(),creatorEntry.get(),publicationdetailEntry.get()))

        cEntimg=PhotoImage(file = "UI//images//png//clearent.png")
        btnclear=Button(win,image=cEntimg,bg='#527048',cursor='hand2')
        btnclear.grid(row=5,column=0,pady=17)
        btnclear.bind('<Button>',lambda event : self.reset_values(event,guideidEntry,titleEntry,creatorEntry,publicationdetailEntry))

        win.mainloop()     

    #-------------------------------------------------------------------------------------
### delete book from database    
    def deleteBook(self,event):
        win=Toplevel(self.root)
        win.title('حذف کتاب')
        self.open_form_size(win,420,210)
        win.iconbitmap('UI//images//ico//deletedb.ico')      
        win.resizable(0,0)
        win.configure(background='#527048')


        deletee=Label(win,text='شماره آیدی :',font=('IRANYekanBold',12),bg='#527048',fg='white')
        deletee.grid(row=0,column=0,padx=20,pady=8)
        deleteeEntry=Entry(master=win)
        deleteeEntry.grid(row=0,column=1,padx=20,pady=4)   


        deletebtnimg= PhotoImage(file = "UI//images//png//deletebtn2.png")
        btndelete=Button(win,image=deletebtnimg,cursor='hand2')
        btndelete.grid(row=0,column=3,padx=5,pady=9)
        btndelete.bind('<Button>',lambda event : self.deleteDB(event,deleteeEntry.get()))

        #________________________________________________________
### delete period books
        first=Label(win,text='از آیدی :',font=('IRANYekanBold',12),bg='#527048',fg='white')
        first.grid(row=1,column=0,padx=20)
        firstEntry=Entry(master=win)
        firstEntry.grid(row=1,column=1,padx=20,pady=30)

        end=Label(win,text='تا آیدی :',font=('IRANYekanBold',12),bg='#527048',fg='white')
        end.grid(row=2,column=0,padx=20,)        
        endEntry=Entry(master=win)
        endEntry.grid(row=2,column=1,padx=20)


        btndelete2=Button(win,image=deletebtnimg,cursor='hand2')
        btndelete2.grid(row=2,column=3,padx=5,pady=9)
        btndelete2.bind('<Button>',lambda event : self.deleteDBperiod(event,firstEntry.get(),endEntry.get()))        

        win.mainloop()
    #------------------------------------------------------------------------------------------------
### search one book from the database    
    def searchBook(self,event):
        win=Toplevel(self.root)
        win.title('جست و جوی کتاب')
        self.open_form_size(win,800,300)
        win.iconbitmap('UI//images//ico//searchdb.ico')      
        win.resizable(0,0)
        win.configure(background='#527048')

        searchLabel=Label(win,text='لطفا شماره رکورد کتاب را در باکس زیر وارد کنید',font=('IRANYekanBold',20),bg='#527048')
        searchLabel.grid(row=0,column=0,padx=165,pady=40)

        searchImg=PhotoImage(file="UI//images//png//search.png")
        Label(win,image=searchImg,bg='#527048').place(x=155,y=95)
        entrySearch=Entry(win,width=17,bd=0,font=("poppins",25,"bold"),bg="#1e251c",fg="white",justify="center")
        entrySearch.place(x=200,y=115)
        entrySearch.focus()
        SearchPhoto=PhotoImage(file="UI//images//png//search_icon.png")
        searchButton=Button(win,image=SearchPhoto,borderwidth=0,relief=SOLID,cursor="hand2",bg="#1e251c")
        searchButton.bind('<Button>',lambda event : searchOneBook(event,entrySearch.get()))
        searchButton.place(x=533,y=107)

        tree=ttk.Treeview(win , column=("record","guideid","title","creator","publicationdetail"),show='headings',height=1)
        tree.grid(row=3,columnspan=1,pady=95)

        tree.column("# 1", anchor=CENTER,width=80)
        tree.heading("# 1",text='رکورد')
        tree.column("# 2", anchor=CENTER,width=150)
        tree.heading("# 2",text='شماره راهنما')
        tree.column("# 3", anchor=CENTER,width=180)
        tree.heading("# 3",text='عنوان')
        tree.column("# 4", anchor=CENTER,width=210)
        tree.heading("# 4",text='پدیدآور')
        tree.column("# 5", anchor=CENTER,width=100)
        tree.heading("# 5",text='مشخصات نشر')                

        def searchOneBook(event,record):
            try:
                db=Database()
                listbook=db.getBook(record)
                tree.insert('','end',text='1',values=(listbook[0][0],listbook[0][1],listbook[0][2],listbook[0][3],listbook[0][4]))       
            except:
                messagebox.showerror('خطا','رکوردی یافت نشد') 

        win.mainloop()

    #----------------------------------------------------------------------------------------------------
### get all books from the database    
    def searchBooks(self,event):
        win=Toplevel(self.root)
        win.title('لیست کتاب ها')
        self.open_form_size(win,742,400)
        win.iconbitmap('UI//images//ico//searchdb2.ico')      
        win.resizable(0,0)
        win.configure(background='#527048')

        txtLabel=Label(win,text='لیست کتابهای کتابخانه',font=('IRANYekanBold',20),bg='#527048')
        txtLabel.grid(row=0,column=0,padx=175,pady=30)


        tree2=ttk.Treeview(win , column=("record","guideid","title","creator","publicationdetail"),show='headings',height=10)
        tree2.grid(row=1,column=0,pady=65)

        tree2.column("# 1", anchor=CENTER,width=80)
        tree2.heading("# 1",text='رکورد')
        tree2.column("# 2", anchor=CENTER,width=150)
        tree2.heading("# 2",text='شماره راهنما')
        tree2.column("# 3", anchor=CENTER,width=180)
        tree2.heading("# 3",text='عنوان')
        tree2.column("# 4", anchor=CENTER,width=210)
        tree2.heading("# 4",text='پدیدآور')
        tree2.column("# 5", anchor=CENTER,width=100)
        tree2.heading("# 5",text='مشخصات نشر')     

        db=Database()
        books=db.getBooks()

        i=1
        for book in books:
            tree2.insert('','end',text=str(i),values=(book[0],book[1],book[2],book[3],book[4]))
            i+=1     

        scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree2.yview)
        tree2.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1,column=1 ,sticky='ns',pady=65)

        tree2.columnconfigure(0, weight=1)                          

        win.mainloop()

#____________________________________________________________________________________________
### defined functions for buttons
    def reset_values(self,event,guideid,title,creator,publicationdetail):
        guideid.delete(0, 'end')
        title.delete(0, 'end')
        creator.delete(0, 'end')
        publicationdetail.delete(0, 'end')

    def insertDb(self,event,guideid,title,creator,publicationdetail):
        book=Book(guideid,title,creator,publicationdetail)
        try:
            db=Database()
            db.insertBook(book)
            messagebox.showinfo('درج','درج با موفیقت انجام شد')
        except:
            messagebox.showerror('خطا','درج با موفیقت انجام نشد')


    def deleteDB(self,event,id):
        try:
            db=Database()
            db.deleteBook(id)
            messagebox.showinfo('حذف','حذف با موفقیت انحام شد')
        except:
            messagebox.showerror('خطا','مشکلی در حذف کردن پیش آمده است') 
        

    def deleteDBperiod(self,event,firstid,endid):
        try:
            db=Database()
            db.deleteBooks(firstid,endid)
            messagebox.showinfo('حذف','حذف با موفقیت انحام شد')
        except:
            messagebox.showerror('خطا','مشکلی در حذف کردن پیش آمده است')            