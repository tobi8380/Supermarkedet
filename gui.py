import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage
import os

from data import Super_data
super_data = Super_data()
super_data.register_user("1", "a")

class supermarket_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        logged_in = False

        if logged_in == True:
            self.build_GUI()
        else:
            self.login_gui()

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
        if super_data.login_success(username, password):
            self.build_GUI()
        else:
            print("incorrect credentials")

        self.username_login_entry.delete(0, "end")
        self.password_login_entry.delete(0, "end")


    def build_GUI(self):
        self.tabs = ttk.Notebook(self)
        admin_fane = ttk.Frame(self.tabs)
        sim_fane = ttk.Frame(self.tabs)
        stock_fane = ttk.Frame(self.tabs)

        self.tabs.add(admin_fane, text='Administrator')
        self.tabs.add(sim_fane, text='Simulering')
        self.tabs.add(stock_fane, text='Lager')

        right_frame = ttk.Frame(admin_fane)
        top_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)
        knap_frame = ttk.Frame(admin_fane)


        self.edit_button = ttk.Button(knap_frame, text="Rediger vare", command=self.do_nothing)
        self.edit_button.pack(side=tk.TOP)

        self.del_button = ttk.Button(knap_frame, text="Slet vare", command=self.do_nothing)
        self.del_button.pack(side=tk.TOP)

        self.add_button = ttk.Button(knap_frame, text="Tilføj ny vare", command=self.do_nothing)
        self.add_button.pack(side=tk.TOP)

        self.buy_button = ttk.Button(knap_frame, text="Bestil varer", command=self.do_nothing)
        self.buy_button.pack(side=tk.TOP)

        self.kurv_text = ScrolledText(knap_frame, state='disabled', width=20,height=5)
        self.kurv_text.pack(side=tk.TOP)
        self.kurv_text.configure(font='TkFixedFont')

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

        self.db_view = ttk.Treeview(data_frame, column=("column1", "column2", "column3", "column4"), selectmode='none', height=7)
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
        ysb = ttk.Scrollbar(data_frame, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)
        # Insert image to #0

        self._img = tk.PhotoImage(file="Kim.png") #change to your file path
        self.db_view.insert('', 'end', image=self._img, value=("Kim", "Slave", "1 krone", "1"))

        self._img = tk.PhotoImage(file="Tobais.png") #change to your file path
        self.db_view.insert('', 'end', image=self._img, value=("Tobais", "Slave", "1 krone", "1"))

        self.trans_view = ttk.Treeview(knap_frame, column=("column1", "column2", "column3"), show='headings')
        self.trans_view.bind("<ButtonRelease-1>", self.do_nothing)
        self.trans_view.heading("#1", text="id")
        self.trans_view.column("#1",minwidth=0,width=20, stretch=tk.NO)
        self.trans_view.heading("#2", text="Pris")
        self.trans_view.column("#2",minwidth=0,width=30, stretch=tk.NO)
        self.trans_view.heading("#3", text="Status")
        self.trans_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.trans_view["displaycolumns"]=("column1", "column2", "column3")
        ysb = ttk.Scrollbar(data_frame, command=self.trans_view.yview, orient=tk.VERTICAL)
        self.trans_view.configure(yscrollcommand=ysb.set)
        self.trans_view.pack(side = tk.TOP, fill=tk.BOTH)

        #Top Frame
        self.can = tk.Canvas(top_frame, width=200, height=200)
        self.can.grid(column=1, row=0, rowspan=2)

        self.lbl_titel = ttk.Label(top_frame, text='Titel')
        self.lbl_forfatter = ttk.Label(top_frame, text='Forfatter')
        self.lbl_titel.grid(column=0, row=0)
        self.lbl_forfatter.grid(column=0, row=1)

        top_frame.pack(side=tk.TOP)
        data_frame.pack(side = tk.TOP)
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
