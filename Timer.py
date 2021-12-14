import tkinter as tk


class Timer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.one_minute = 60
        self.time = tk.IntVar()
        self.time.set(self.one_minute)
        self.timerLabel = None
        self.createTimer()

        # update timer state
        self.updateTime()

    def createTimer(self):
        self.timerLabel = tk.Label(self, text=str(self.time.get()), font=("TkDefaultFont", 24), bg='black', fg='white')
        self.timerLabel.pack(side=tk.LEFT)

    def updateTime(self):
        if self.time.get() == 0:
            self.widgetModel.ended = True
        if self.widgetModel.started and not self.widgetModel.ended:
            self.time.set(self.time.get() - 1)
            self.timerLabel.config(text=self.time.get())
        self.parent.parent.after(1000, self.updateTime)

    def reset(self):
        self.time.set(self.one_minute)
        self.timerLabel.config(text=self.time.get())
