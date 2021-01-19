from tkinter import *
import tkinter.ttk as ttk
import os
import login
from data import Super_data

class supermarket:
def __init__(self, master=None):
    ttk.Frame.__init__(self, master)

        self.build_GUI()
