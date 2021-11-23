import tkinter as tk
from random import randrange
from TextRowFrame import TextRowFrame

class MovingText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent

        self.config(bg='blue', width=600, height=84)
        self.grid_propagate(0)

        # widgets for the frame
        self.createLabel()

    def createLabel(self):

        self.textWidgetTop = TextRowFrame(self, self.get10RandomStrings())
        self.textWidgetTop.grid(row=0, column=0, sticky='w')
        self.textWidgetBottom = TextRowFrame(self, self.get10RandomStrings())
        self.textWidgetBottom.grid(row=1, column=0, sticky='w')


    def get10RandomStrings(self):
        strArr = []
        for i in range(10):
            strArr.append(self.parent.text[randrange(1000)])
        return strArr