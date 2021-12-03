import tkinter as tk
from tkinter import font

from MovingText import MovingText
from UserEntry import UserEntry
from Timer import Timer
from RetryButton import RetryButton
from StatsFrame import StatsFrame
from WidgetModel import WidgetModel


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.parent.title("The Ultimate Typing Test")
        self.config(bg='lightseagreen')
        self.grid(row=0, column=0)
        self.parent.minsize(668, 170)
        # self.grid_propagate(0)
        print(font.names())

        # get the data and create an instance of WidgetModel (that holds all persistent data)
        self.widgetModel = WidgetModel()

        # configure the subframes
        self.timer = Timer(self)
        self.timer.pack(anchor=tk.CENTER)
        
        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER, padx=20, pady=(40, 0))
        self.movingText.grid_propagate(0)

        self.statsFrame = StatsFrame(self)
        self.statsFrame.pack(anchor=tk.CENTER, pady=40)

        self.retryButton = RetryButton(self)
        self.retryButton.pack(anchor=tk.CENTER)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER)


    def totalReset(self):
        self.widgetModel.reset()
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
