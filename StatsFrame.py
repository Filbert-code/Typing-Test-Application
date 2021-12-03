import tkinter as tk


class StatsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        # create stats elements
        self.wpmScoreLabel = None

        self.createLabels()
        self.update_self()

    def createLabels(self):
        self.wpmScoreLabel = tk.Label(self, text="WPM: ", font=("Courier", 16))
        self.wpmScoreLabel.grid(row=0, column=0)

    def update_self(self):
        print("(" + str(self.widgetModel.started) + ", " + str(self.widgetModel.ended) + ")")
        if self.widgetModel.started and self.widgetModel.ended:
            num_of_words = (self.widgetModel.char_count / 5.0)
            self.wpmScoreLabel.config(text="WPM: {}".format(str(round(num_of_words, 2))))
        self.parent.parent.after(100, self.update_self)


