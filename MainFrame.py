import tkinter as tk

from MovingText import MovingText
from UserEntry import UserEntry
from WidgetModel import WidgetModel


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.parent.title("The Ultimate Typing Test")
        self.config(bg='lightseagreen', width=800, height=600)
        self.grid(row=0, column=0)
        # self.grid_propagate(0)

        # get the data and create an instance of WidgetModel (that holds all persistent data)
        self.widgetModel = WidgetModel()

        # configure the subframes
        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER, padx=20, pady=40)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER)


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
