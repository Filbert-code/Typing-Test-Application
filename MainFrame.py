import tkinter as tk

from MovingText import MovingText


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.parent.title("Metro-2 Text Replacement Tool")
        self.parent.maxsize(800, 600)
        self.parent.minsize(800, 600)
        self.config(bg='lightseagreen', width=800, height=600)
        self.grid(row=0, column=0)
        self.grid_propagate(0)

        self.text = open("1000MostCommonWords.txt").readlines()

        self.movingText = MovingText(self)
        self.movingText.grid(row=0, column=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)




if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
