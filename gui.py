import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage
import os
from data import Super_data, Item, Employee, Item_id, Barcode, Item_code

super_data = Super_data()
super_data.register_user("1", "a", 1, "1234")

class supermarket_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        # logged_in = False
        #
        # if logged_in == True:
        #     self.build_GUI()
        # else:
        self.login_gui()


    def opdater_tabel(self):
        l = super_data.get_item_list()
        # self.db_view.delete(*self.db_view.get_children())
        # for i in l:
        #     self.db_view.insert("", tk.END, values=(i.item_id.id, i.name, i.stock, i.price, i.discount_price, i.discount))
        self.trans_view.delete(*self.trans_view.get_children())
        for i in l:
            print(i.item_id.id, i.name, i.stock, i.price, i.discount_price, i.discount)
            self.trans_view.insert("", tk.END, values=(i.item_id.id, i.name, i.stock, i.price, i.discount_price, i.discount))

    def login_gui(self):
        login_screen = tk.Toplevel(self.master)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        # login_gui.main_account_screen()

        self.password_verify = tk.StringVar()
        self.username_verify = tk.StringVar()

        tk.Label(login_screen, text="Brugernavn * ").pack()
        self.username_login_entry = tk.Entry(login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        tk.Label(login_screen, text="").pack()
        tk.Label(login_screen, text="Kode * ").pack()
        self.password_login_entry = tk.Entry(login_screen, textvariable=self.password_verify, show= '*')
        self.password_login_entry.pack()
        tk.Label(login_screen, text="").pack()
        tk.Button(login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()

    def login_verify(self):
        username = self.username_verify.get()
        password = self.password_verify.get()
        self.current_user_position = super_data.login_success(username, password)
        if self.current_user_position != None:
            self.build_GUI()
            self.opdater_tabel()
        else:
            print("incorrect credentials")

        self.username_login_entry.delete(0, "end")
        self.password_login_entry.delete(0, "end")

    def new_item(self):
        print('new item')
        self.new_item_name = tk.StringVar()
        self.new_item_id = tk.StringVar()
        self.new_item_price = tk.StringVar()
        self.item_discount_price = tk.StringVar()

        new_item_screen = tk.Toplevel(self.master)
        new_item_screen.title("Ny vare")
        new_item_screen.geometry("300x250")

        tk.Label(new_item_screen, text="Varenavn * ").pack()
        self.new_item_entry = tk.Entry(new_item_screen, textvariable=self.new_item_name)
        self.new_item_entry.pack()

        tk.Label(new_item_screen, text="VareID * ").pack()
        self.new_item_id_entry = tk.Entry(new_item_screen, textvariable=self.new_item_id)
        self.new_item_id_entry.pack()

        tk.Label(new_item_screen, text="Varens pris * ").pack()
        self.new_item_price_entry = tk.Entry(new_item_screen, textvariable=self.new_item_price)
        self.new_item_price_entry.pack()

        tk.Label(new_item_screen, text="Varens udsalgspris * ").pack()
        self.item_discount_entry = tk.Entry(new_item_screen, textvariable=self.item_discount_price)
        self.item_discount_entry.pack()

        tk.Button(new_item_screen, text="Opret vare", width=10, height=1, command=self.new_item_add).pack()

    def new_item_add(self):
            item_name = self.new_item_name.get()
            item_price = int(self.new_item_price.get())
            item_id = self.new_item_id.get()
            item_discount_price = int(self.item_discount_price.get())

            new_item = Item(item_name, item_id, item_price, item_discount_price)
            super_data.register_item(new_item)
            print(item_name, item_id, item_price, item_discount_price)
            self.opdater_tabel()

    def new_shipment(self):
            print('new shipment')
            self.new_item_name = tk.StringVar()
            self.new_item_id = tk.StringVar()
            self.new_item_price = tk.StringVar()
            self.item_discount_price = tk.StringVar()

            new_item_screen = tk.Toplevel(self.master)
            new_item_screen.title("Ny vare")
            new_item_screen.geometry("300x250")

            tk.Label(new_item_screen, text="Varenavn * ").pack()
            self.new_item_entry = tk.Entry(new_item_screen, textvariable=self.new_item_name)
            self.new_item_entry.pack()

            tk.Label(new_item_screen, text="VareID * ").pack()
            self.new_item_id_entry = tk.Entry(new_item_screen, textvariable=self.new_item_id)
            self.new_item_id_entry.pack()

            tk.Label(new_item_screen, text="Varens pris * ").pack()
            self.new_item_price_entry = tk.Entry(new_item_screen, textvariable=self.new_item_price)
            self.new_item_price_entry.pack()

            tk.Label(new_item_screen, text="Varens udsalgspris * ").pack()
            self.item_discount_entry = tk.Entry(new_item_screen, textvariable=self.item_discount_price)
            self.item_discount_entry.pack()

            tk.Button(new_item_screen, text="Opret vare", width=10, height=1, command=self.new_item_add).pack()


    def build_GUI(self):
        self.tabs = ttk.Notebook(self)
        admin_fane = ttk.Frame(self.tabs)
        sim_fane = ttk.Frame(self.tabs)
        stock_fane = ttk.Frame(self.tabs)

        self.tabs.add(admin_fane, text='Administrator')
        #self.tabs.add(sim_fane, text='Økonomi')
        self.tabs.add(stock_fane, text='Lager')

        right_frame = ttk.Frame(admin_fane)
        righttop_frame = ttk.Frame(right_frame)
        rightbot_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)

        knap_frame = ttk.Frame(admin_fane)
        stock_dat_frame = ttk.Frame(stock_fane)



        self.buy_button = ttk.Button(rightbot_frame, text="Fyre knappen", command=self.do_nothing)
        self.buy_button.pack(side=tk.TOP)


        self.cons = ScrolledText(sim_fane, state='disabled', height=12)
        self.cons.pack(side = tk.TOP)
        self.cons.configure(font='TkFixedFont')
        self.after(1000, self.do_nothing)

        butAnsaet = ttk.Button(sim_fane, text="Ansæt en person", command=self.do_nothing)
        butAnsaet.pack(side=tk.TOP)
        butFyr = ttk.Button(sim_fane, text="Fyr en person", command=self.do_nothing)
        butFyr.pack(side=tk.TOP)
        self.after(3000, self.do_nothing)
        self.lblMoney = ttk.Label(sim_fane, text="Pengebeholdning: {}".format(self.do_nothing))
        self.lblMoney.pack(side=tk.TOP)
        self.lblAnsatte = ttk.Label(sim_fane, text="Antal ansatte: {}".format(self.do_nothing))
        self.lblAnsatte.pack(side=tk.TOP)
        self.sc_tilbud = ttk.LabeledScale (sim_fane,from_=50,to=110)
        self.sc_tilbud.pack(side=tk.TOP)

        self.db_view = ttk.Treeview(righttop_frame, column=("column1", "column2", "column3", "column4"), selectmode='none', height=7)
        self.db_view.grid(row=0, column=0, sticky='nsew')
        self.db_view.bind("<ButtonRelease-1>")
        self.db_view.heading("#1", text="Navn", anchor='center')
        self.db_view.column("#1",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#2", text="Rolle", anchor='center')
        self.db_view.column("#2",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#3", text="Løn", anchor='center')
        self.db_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#4", text="id", anchor='center')
        self.db_view.column("#4",minwidth=0,width=80, stretch=tk.NO)
        #Læg mærke til at kolonne 5 ikke bliver vist.
        #Vi kan stadig finde id på den admin der er valgt,
        #men brugeren kan ikke se id.
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(righttop_frame, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)
        # Insert image to #0

        self._img = tk.PhotoImage(file="Kim.png") #change to your file path
        self.db_view.insert('', 'end', image=self._img, value=("Kim", "Slave", "1 krone", "1"))

        self._img = tk.PhotoImage(file="Tobais.png") #change to your file path
        self.db_view.insert('', 'end', image=self._img, value=("Tobais", "Slave", "1 krone", "1"))

        self.trans_view = ttk.Treeview(stock_dat_frame, column=("column1", "column2", "column3", "column4", "column5", "column6"), selectmode='none', height=10)
        self.trans_view.bind("<ButtonRelease-1>")
        self.trans_view.heading("#1", text="Vare_ID", anchor='center')
        self.trans_view.column("#1",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view.heading("#2", text="Vare", anchor='center')
        self.trans_view.column("#2",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view.heading("#3", text="Antal", anchor='center')
        self.trans_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view.heading("#4", text="Pris", anchor='center')
        self.trans_view.column("#4",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view.heading("#5", text="Discount pris", anchor='center')
        self.trans_view.column("#5",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view.heading("#6", text="Udsalg?", anchor='center')
        self.trans_view["displaycolumns"]=("column1", "column2", "column3", "column4", "column5", "column6")
        self.trans_view.column("#6",minwidth=0,width=80, stretch=tk.NO)
        ysb = ttk.Scrollbar(stock_dat_frame, command=self.trans_view.yview, orient=tk.VERTICAL)
        self.trans_view.configure(yscrollcommand=ysb.set)
        self.trans_view.pack(side = tk.TOP, fill=tk.BOTH)

        #Top Frame


        #Lager-fane
        self.new_item_button = ttk.Button(stock_fane, text="Ny vare", command=self.new_item)
        self.new_item_button.pack(side=tk.LEFT)

        # self.buy_button = ttk.Button(knap_frame, text="Bestil varer", command=self.do_nothing)
        # self.buy_button.pack(side=tk.TOP)


        righttop_frame.pack(side=tk.TOP)
        rightbot_frame.pack(side=tk.BOTTOM)
        data_frame.pack(side = tk.TOP)
        stock_dat_frame.pack(side = tk.BOTTOM)
        knap_frame.pack(side = tk.LEFT, fill=tk.Y)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabs.pack(expand=1, fill="both")


        self.pack()

    #     self.after(10000, self.do_nothing)
    #     self.after(1000, self.do_nothing)
    #
    def do_nothing(self):
        pass

root = tk.Tk()
root.geometry("800x600")

app = supermarket_gui(root)
app.master.title('Supermarked program')
app.mainloop()
