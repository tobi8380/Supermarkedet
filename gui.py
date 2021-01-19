import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import os
import login
from data import Super_data

class supermarket_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.build_GUI()

    def build_GUI(self):
        self.tabs = ttk.Notebook(self)
        bog_fane = ttk.Frame(self.tabs)
        sim_fane = ttk.Frame(self.tabs)

        self.tabs.add(bog_fane, text='Bøger')
        self.tabs.add(sim_fane, text='Simulering')

        right_frame = ttk.Frame(bog_fane)
        top_frame = ttk.Frame(right_frame)
        data_frame = ttk.Frame(right_frame)
        knap_frame = ttk.Frame(bog_fane)


        self.edit_button = ttk.Button(knap_frame, text="Rediger bog", command=self.do_nothing)
        self.edit_button.pack(side=tk.TOP)

        self.del_button = ttk.Button(knap_frame, text="Slet bog", command=self.do_nothing)
        self.del_button.pack(side=tk.TOP)

        self.add_button = ttk.Button(knap_frame, text="Tilføj til kurv", command=self.do_nothing)
        self.add_button.pack(side=tk.TOP)

        self.buy_button = ttk.Button(knap_frame, text="Køb", command=self.do_nothing)
        self.buy_button.pack(side=tk.TOP)

        self.kurv_text = ScrolledText(knap_frame, state='disabled', width=20,height=5)
        self.kurv_text.pack(side=tk.TOP)
        self.kurv_text.configure(font='TkFixedFont')

        self.cons = ScrolledText(sim_fane, state='disabled', height=12)
        self.cons.pack(side = tk.TOP)
        self.cons.configure(font='TkFixedFont')
        self.after(1000, self.simulate_customer)

        butAnsaet = ttk.Button(sim_fane, text="Ansæt en person", command=self.ansaet)
        butAnsaet.pack(side=tk.TOP)
        butFyr = ttk.Button(sim_fane, text="Fyr en person", command=self.fyr)
        butFyr.pack(side=tk.TOP)
        self.after(3000, self.udbetal_loen)
        self.lblMoney = ttk.Label(sim_fane, text="Pengebeholdning: {}".format(self.data.money))
        self.lblMoney.pack(side=tk.TOP)
        self.lblAnsatte = ttk.Label(sim_fane, text="Antal ansatte: {}".format(len(self.data.ansatte)))
        self.lblAnsatte.pack(side=tk.TOP)
        self.sc_tilbud = ttk.LabeledScale (sim_fane,from_=50,to=110)
        self.sc_tilbud.pack(side=tk.TOP)

        self.db_view = ttk.Treeview(data_frame, column=("column1", "column2", "column3", "column4", "column5"), show='headings')
        self.db_view.bind("<ButtonRelease-1>", self.on_book_selected)
        self.db_view.heading("#1", text="Titel", command=self.sorterTitel)
        self.db_view.column("#1",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#2", text="Forfatter", command=self.sorterForfatter)
        self.db_view.column("#2",minwidth=0,width=150, stretch=tk.NO)
        self.db_view.heading("#3", text="Årstal", command=self.sorterAarstal)
        self.db_view.column("#3",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#4", text="Rating", command=self.sorterRating)
        self.db_view.column("#4",minwidth=0,width=80, stretch=tk.NO)
        self.db_view.heading("#5", text="id")
        #Læg mærke til at kolonne 5 ikke bliver vist.
        #Vi kan stadig finde id på den bog der er valgt,
        #men brugeren kan ikke se id.
        self.db_view["displaycolumns"]=("column1", "column2", "column3", "column4")
        ysb = ttk.Scrollbar(data_frame, command=self.db_view.yview, orient=tk.VERTICAL)
        self.db_view.configure(yscrollcommand=ysb.set)
        self.db_view.pack(side = tk.TOP, fill=tk.BOTH)

        self.trans_view = ttk.Treeview(knap_frame, column=("column1", "column2", "column3"), show='headings')
        self.trans_view.bind("<ButtonRelease-1>", self.on_trans_selected)
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

        self.after(10000, self.udbetal_loen)
        self.after(1000, self.simulate_customer)

    def do_nothing():
        pass

root = tk.Tk()
root.geometry("800x600")

app = supermarket_gui(root)
app.master.title('Supermarked program')
app.mainloop()
