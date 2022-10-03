from tkinter import *
from db_back_end import Database
from account_back_end import Account

class Windows():

    def __init__(self, windows):
        windows.title('Books Inventory App')

        self.list1 = Listbox(windows, width=60, height=20)
        self.list1.grid(row=1, column=0, rowspan=12, columnspan=12)
        sb1 = Scrollbar(windows)
        sb1.grid(row=0, column=12, rowspan=12)
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        l1 = Label(windows, text="Title")
        l1.grid(row=1, column=15, columnspan=2)
        l2 = Label(windows, text="Author")
        l2.grid(row=4, column=15, columnspan=2)
        l3 = Label(windows, text="Year")
        l3.grid(row=7, column=15, columnspan=2)
        l4 = Label(windows, text="ISBN")
        l4.grid(row=10, column=15, columnspan=2)
        l5 = Label(windows, text="Q\nu\ne\nr\ny\n \nI\nn\nf\no\n \nR\ni\ng\nh\nt\n \nS\ni\nd\ne")
        l5.grid(row=2, column=14, rowspan=9)
        l6 = Label(windows, text="")
        l6.grid(row=3, column=15, columnspan=2)
        l7 = Label(windows, text="")
        l7.grid(row=6, column=15, columnspan=2)
        l8 = Label(windows, text="")
        l8.grid(row=9, column=15, columnspan=2)
        l9 = Label(windows, text="")
        l9.grid(row=12, column=15, columnspan=2)

        self.title_text = StringVar()
        self.e1 = Entry(windows, textvariable=self.title_text)
        self.e1.grid(row=2, column=15, columnspan=2)
        self.author_text = StringVar()
        self.e2 = Entry(windows, textvariable=self.author_text)
        self.e2.grid(row=5, column=15, columnspan=2)
        self.year_text = StringVar()
        self.e3 = Entry(windows, textvariable=self.year_text)
        self.e3.grid(row=8, column=15, columnspan=2)
        self.ISBN_text = StringVar()
        self.e4 = Entry(windows, textvariable=self.ISBN_text)
        self.e4.grid(row=11, column=15, columnspan=2)

        b1 = Button(windows, text="View all", width=10, command=lambda: self.view_command())  # 需要lambda:做间隔，否则command就会自动运行，根本等不到你去按这个按钮
        b1.grid(row=12, column=0, columnspan=2)
        b2 = Button(windows, text="Search", width=10, command=lambda: self.search_command())
        b2.grid(row=12, column=2, columnspan=2)
        b3 = Button(windows, text="Add", width=10, command=lambda: self.add_command())
        b3.grid(row=12, column=4, columnspan=2)
        b4 = Button(windows, text="Update", width=10, command=lambda: self.uppdate_command())
        b4.grid(row=12, column=6, columnspan=2)
        b5 = Button(windows, text="Delete", width=10, command=lambda: self.delete_command())
        b5.grid(row=12, column=8, columnspan=2)
        b6 = Button(windows, text="Close", width=10, command=lambda: self.close_command())
        b6.grid(row=12, column=10, columnspan=2)

        l10 = Label(windows, text="Book Inventory Database", width=60)
        l10.grid(row=1, column=0, columnspan=12)

        l11 = Label(windows, text="")
        l11.grid(row=13, column=0)

        windows.mainloop()


    def view_command(self):
        global selected_tuple
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)
        selected_tuple = ()


    def search_command(self):
        global selected_tuple
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
            self.list1.insert(END, row)
        selected_tuple = ()


    def add_command(self):
        global selected_tuple
        self.list1.delete(0, END)
        database.insert_table(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.list1.insert(END, "New Added Book Information:")
        self.list1.insert(END, self.title_text.get() + ' ' + self.author_text.get() + ' ' + self.year_text.get() + ' ' + self.ISBN_text.get())
        self.list1.insert(END, "Operation Succeeded!")
        selected_tuple = ()


    def get_selected_row(self, event):
        global selected_tuple
        index = self.list1.curselection()
        # print(index)
        if index != ():
            selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        else:
            selected_tuple = ()


    def delete_command(self):
        global selected_tuple
        if selected_tuple != ():
            database.delete(selected_tuple[0])
            self.list1.delete(0, END)
            self.list1.insert(END, "Deleted Book Information:")
            self.list1.insert(END, selected_tuple)
            self.list1.insert(END, "Operation Succeeded!")
        else:
            self.list1.delete(0, END)
            self.list1.insert(END, "Please Select a Book First")
        selected_tuple = ()


    def uppdate_command(self):
        global selected_tuple
        if selected_tuple != ():
            database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
            self.list1.delete(0, END)
            self.list1.insert(END, "Updated Book Information:")
            self.list1.insert(END, self.title_text.get() + ' ' + self.author_text.get() + ' ' + self.year_text.get() + ' ' + self.ISBN_text.get())
            self.list1.insert(END, "Operation Succeeded!")
        else:
            self.list1.delete(0, END)
            self.list1.insert(END, "Please Select a Book First")
        selected_tuple = ()


    def close_command(self):
        global database
        del database
        windows.destroy()


def create():
    global account
    global flag
    row = account.search(account_text.get(), password_text.get())
    if row != []:
        del account
        account_log_in.destroy()
        flag = 1
    else:
        l1_2 = Label(account_log_in, text="Information Error!")
        l1_2.grid(row=2, column=1)


flag = 0

account_log_in = Tk()
account_log_in.title('Account Log In Window')

account = Account("account.db")

l1_1 = Label(account_log_in, text="Account")
l1_1.grid(row=0, column=0)
l1_2 = Label(account_log_in, text="Password")
l1_2.grid(row=1, column=0)

account_text = StringVar()
e1_1 = Entry(account_log_in, textvariable=account_text)
e1_1.grid(row=0, column=1)
password_text = StringVar()
e1_2 = Entry(account_log_in, textvariable=password_text, show='*')
e1_2.grid(row=1, column=1)

b1_1 = Button(account_log_in, text="Log In", command=lambda: create())
b1_1.grid(row=2, column=0)

account_log_in.mainloop()

if flag == 1:
    database = Database("books.db")
    windows = Tk()
    Windows(windows)

