import tkinter as tk
from tkinter import font

from MovingText import MovingText
from UserEntry import UserEntry
from Timer import Timer
from RetryButton import RetryButton
from StatsFrame import StatsFrame
from WidgetModel import WidgetModel
from TopicEntry import TopicEntry
import pyglet


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.parent.title("The Ultimate Typing Test")
        self.bg = tk.PhotoImage(file="background.png")
        self.bgLabel = tk.Label(self, image=self.bg)
        self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.pack(anchor=tk.CENTER)
        self.parent.config(bg='lightseagreen')
        self.parent.minsize(960, 300)
        # self.grid_propagate(0)

        # get the data and create an instance of WidgetModel (that holds all persistent data)
        self.widgetModel = WidgetModel()

        self.typingFont = "Raleway"
        pyglet.font.add_file("Raleway-Medium.ttf")

        # configure the subframes
        self.timer = Timer(self)
        self.timer.pack(anchor=tk.CENTER, pady=(10, 10))
        
        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER)
        self.movingText.grid_propagate(0)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER, pady=(30, 0))

        self.retryButton = RetryButton(self)
        self.retryButton.pack(anchor=tk.CENTER, pady=(10, 70))

        self.topicEntry = TopicEntry(self)
        self.topicEntry.place(relx=1.0, rely=0.0, x=-91, y=20, anchor="ne")

        self.statsFrame = StatsFrame(self)
        self.statsFrame.place(relx=1.0, rely=1.0, x=0, y=-159, anchor="ne")


    def totalReset(self):
        self.widgetModel.reset()
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()
        self.topicEntry.reset()
        self.statsFrame.reset()

    def newTopicReset(self, new_words):
        self.widgetModel.reset(new_words)
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()
        self.topicEntry.reset()
        self.statsFrame.reset()



if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
