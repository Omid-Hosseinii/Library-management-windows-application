from tkinter import *


# def reset_values():
#     ent1.delete(0, 'end')
#     ent2.delete(0, 'end')
 
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


# ent1=Entry(root)
# ent1.place(x=10, y=120)
# ent2=Entry(root)
# ent2.place(x=10, y=100)
# reset = Button(text="Reset Values!", command=reset_values)
# reset.place(x=10, y=165)
root.mainloop()




