    def __init__(self):
        self.root=Tk()
        self.open_form_size(self.root,825,550)
        self.root.title('نرم افزار کتابداری')   
        self.root.iconbitmap('UI//images//ico//libraryicon2.ico')
        self.root.resizable(0,0)

        bg = PhotoImage(file = "UI//images//png//library.png")
        canvas1 = Canvas( self.root, width = 825,height = 550)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image(0,0,image=bg,anchor="nw")



        # self.welcomeLabel=Label(self.root,text='به نرم افزار مدیریت کتابخانه خوش آمدید',bg='#E97611',fg='white',font=('IRANYekanBlack',17))
        imglabel1 = PhotoImage(file = "UI//images//png//test2.png")
        self.welcomeLabel=Label(self.root,image=imglabel1)
        self.welcomeLabel.place(x=223,y=55)  
        # self.welcomeLabel=Label(self.root,text='لطفا عملیات خود را انتخاب کنید',bg='#E97611',fg='white',font=('IRANYekanBlack',20))
        # self.welcomeLabel.place(x=240,y=77)  

        self.btn1=Button(self.root,text='ثبت کتاب',relief=RAISED,font=('IRANYekanBlack',17),width=8,bg='#A67143',fg='white')
        self.btn1.place(x=130,y=270)   
        self.btn1.bind('<Button>',lambda event : self.addBook(event))

        self.btn2=Button(self.root,text='حذف کتاب',relief=RAISED,font=('IRANYekanBlack',17),width=8,bg='#A67143',fg='white')
        self.btn2.place(x=280,y=270)   
        self.btn2.bind('<Button>',lambda event : self.deleteBook(event))

        self.btn3=Button(self.root,text='جستجوی کتاب',relief=RAISED,font=('IRANYekanBlack',17),width=8,bg='#A67143',fg='white')
        self.btn3.place(x=430,y=270)   
        self.btn3.bind('<Button>',lambda event : self.searchBook(event))

        self.btn4=Button(self.root,text='نمایش کتابها',relief=RAISED,font=('IRANYekanBlack',17),width=8,bg='#A67143',fg='white')
        self.btn4.place(x=600,y=270)   
        self.btn4.bind('<Button>',lambda event : self.searchBooks(event))


        self.root.mainloop()  

