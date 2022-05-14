from sre_constants import GROUPREF_EXISTS
from tkinter import *
import pyglet
pyglet.font.add_file('font/IRANYekanBlack.ttf')
pyglet.font.add_file('font/IRANYekanBold.ttf')
pyglet.font.add_file('font/IRANYekanLight.ttf')
pyglet.font.add_file('font/IRANYekanRegular.ttf')

import os
print(os.getcwd())

def reset_values():

    pass
    # ent1.delete(0, 'end')
    # ent2.delete(0, 'end')
 
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("825x550")
root.resizable(0,0)
  
# Add image file
bg = PhotoImage(file = "UI//images//png//library.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 825,height = 550)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

l1=Label(root,text='سلام به برنامه خوش آمدید')
l1.place(x=100,y=200)
l1=Label(root,text='سلام به برنامه خوش آمدید',font=('IRANYekanBlack',13))
l1.place(x=100,y=250)
l1=Label(root,text='سلام به برنامه خوش آمدید',font=('IRANYekanLight',20))
l1.place(x=100,y=300)
l1=Label(root,text='سلام به برنامه خوش آمدید',font=('IRANYekanRegular',15))
l1.place(x=100,y=350)
# ent1=Entry(root)
# ent1.place(x=10, y=120)
# ent2=Entry(root)
# ent2.place(x=10, y=100)
img=PhotoImage(file="UI//images//png//button2.png")
reset = Button(image=img, command=reset_values,relief=SOLID)
reset.place(x=400, y=165)


# Add Text
canvas1.create_text( 200, 250, text = "Welcome")
  
# Create Buttons
button1 = Button( root, text = "Exit")
button3 = Button( root, text = "Start")
button2 = Button( root, text = "Reset")
  
# Display Buttons
button1_canvas = canvas1.create_window( 100, 10, 
                                       anchor = "nw",
                                       window = button1)
  
button2_canvas = canvas1.create_window( 100, 40,
                                       anchor = "nw",
                                       window = button2)
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
                                       window = button3)

root.mainloop()




