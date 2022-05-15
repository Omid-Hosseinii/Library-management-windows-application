import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()





























# import tkinter as tk
# from tkinter import *
# class Gui():
#     def __init__(self, root):
#         self.root=root
#         self.entry = tk.Entry(root)
#         stvar=tk.StringVar()
#         stvar.set("one")

#         self.canvas=tk.Canvas(root, width=300, height=200, background='white')
#         self.canvas.grid(row=0,column=1)

#         frame = Frame(self.root)
#         frame.grid(row=0,column=0, sticky="n")

#         self.option=tk.OptionMenu(frame, stvar, "one", "two", "three")
#         label1=Label(frame, text="Figure").grid(row=0,column=0, sticky="nw")
#         label2=Label(frame, text="X").grid(row=1,column=0, sticky="w")
#         label3=Label(frame, text="Y").grid(row=2,column=0, sticky="w")
#         self.option.grid(row=0,column=1,sticky="nwe")
#         entry = Entry(frame).grid(row = 1,column = 1,sticky = E+ W)
#         entry1 = Entry(frame).grid(row = 2,column = 1, sticky = E)
#         Button1=Button(frame,text="Draw").grid(row = 3,column = 1, sticky = "we")
#         figure1=self.canvas.create_rectangle(80, 80, 120, 120, fill="blue")

#         #Grid.columnconfigure(self.root,1,weight=1, size=200)
# if __name__== '__main__':
#     root=tk.Tk()
#     gui=Gui(root)
#     root.mainloop()