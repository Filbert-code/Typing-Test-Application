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
        self.labels = []
        self.createLabel()

        # update
        self.update_self()

    def createLabel(self):
        # self.textWidget =
        for i in range(20):
            self.labels.append(tk.Label(self, text=self.parent.widgetModel.row_of_words[i], font=("Courier", 12)))
        for label in self.labels:
            self.update()
            print(self.winfo_reqwidth())
            label.pack(side=tk.LEFT)

    # # set the background of the word that the user needs to type out next
    # def setHighlightedWord(self, index):
    #



    def update_self(self):

        self.parent.parent.after(100, self.update_self)


