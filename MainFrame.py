import tkinter as tk

from MovingText import MovingText
from UserEntry import UserEntry


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.parent.title("Metro-2 Text Replacement Tool")
        # self.parent.maxsize(800, 600)
        # self.parent.minsize(800, 600)
        self.config(bg='lightseagreen', width=800, height=600)
        self.grid(row=0, column=0)
        # self.grid_propagate(0)

        # get the data and create an instance of WidgetModel (that holds all persistent data)
        self.text = open("1000MostCommonWords.txt").readlines()

        # configure the subframes
        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER, padx=20, pady=40)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(1, weight=1)




if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
