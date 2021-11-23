import tkinter as tk

class UserEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent

        self.config(bg='green', width=200, height=42)
        self.grid_propagate(0)

        self.entry = tk.Entry(self, font=("Courier", 12))
        self.entry.grid(row=0, column=0)