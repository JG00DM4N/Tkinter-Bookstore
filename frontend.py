from tkinter import *
from backend import Database

database = Database()

class Bookstore:

    def __init__(self,store_name):
        self.window=Tk()
        self.window.title(store_name)
        
        l1=Label(self.window,text="Title")
        l1.grid(row=0,column=0)

        l2=Label(self.window,text="Author")
        l2.grid(row=0,column=2)

        l3=Label(self.window,text="Year")
        l3.grid(row=1,column=0)

        l4=Label(self.window,text="ISBN")
        l4.grid(row=1,column=2)

        self.title_text=StringVar()
        self.e1=Entry(self.window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.author_text=StringVar()
        self.e2=Entry(self.window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(self.window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(self.window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        self.b1=Button(self.window,text="View All",height=1,width=12,command=self.view_command)
        self.b1.grid(row=2,column=3)

        self.b2=Button(self.window,text="Search Entry",height=1,width=12,command=self.search_command)
        self.b2.grid(row=3,column=3)

        self.b3=Button(self.window,text="Add Entry",height=1,width=12,command=self.insert_command)
        self.b3.grid(row=4,column=3)

        self.b4=Button(self.window,text="Update Selected",height=1,width=12, command=self.update_command)
        self.b4.grid(row=5,column=3)

        self.b5=Button(self.window,text="Delete Selected",height=1,width=12,command=self.delete_command)
        self.b5.grid(row=6,column=3)

        self.b6=Button(self.window,text="Close",height=1,width=12,command=exit)
        self.b6.grid(row=7,column=3)

        self.list1=Listbox(self.window,height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(self.window)
        sb1.grid(row=2,column=2,rowspan=6,columnspan=1)

        self.list1.bind('<<ListboxSelect>>', self.line_select)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

    def line_select(self,event):
        global selection
        try:
            current_index=self.list1.curselection()[0]
            selection=self.list1.get(current_index)
            self.e1.delete(0,END)
            self.e1.insert(END,selection[1])
            self.e2.delete(0,END)
            self.e2.insert(END,selection[2])
            self.e3.delete(0,END)
            self.e3.insert(END,selection[3])
            self.e4.delete(0,END)
            self.e4.insert(END,selection[4])
        except IndexError:
            pass
        
    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        rows=database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        for row in rows:
            self.list1.insert(END,row)

    def insert_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        rows=database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.insert(END,rows[-1])

    def update_command(self):
        #current_index=list1.curselection()
        #selection=list1.get(current_index)
        database.update(selection[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.view_command()

    def delete_command(self):
        current_index=self.list1.curselection()[0]
        selection=self.list1.get(current_index)
        database.delete(selection[0])
        self.view_command()


store = Bookstore("The Book Store!")
store.window.mainloop()
#store=Tk()
#store.title("Book Inventory")





