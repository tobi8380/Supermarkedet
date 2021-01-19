import tkinter as tk
import tkinter.ttk as ttk
import os
import login
from data import Super_data

class supermarket_gui(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.build_GUI()

    def build_GUI():
        print('test')

root = tk.Tk()
root.geometry("800x600")

app = supermarket_gui(root)
app.master.title('Supermarked program')
app.mainloop()
