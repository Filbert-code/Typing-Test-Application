import tkinter as tk


class TextRowFrame(tk.Frame):
    def __init__(self, parent, text_array, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        # text is an array of 10 random strings
        self.text_array = text_array




        for i in range(len(self.text)):
            tk.Label(self, text=self.text[i] + " ", font=("Courier", 12), bg='grey').grid(row=0, column=i)