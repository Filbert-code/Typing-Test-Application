import tkinter as tk
from random import randrange
from time import sleep


class MovingText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='black', width=600, height=84)

        # widgets for the frame
        self.labels = []
        self.createLabelRows()

        # update
        self.update_self()

    def createLabelRows(self):
        f0 = tk.Frame(self)
        f1 = tk.Frame(self)
        frames = [f0, f1]

        for frame in frames:
            # max width for each frame is 600
            while frame.winfo_reqwidth() < 601:
                # need to call in order to get the correct winfo_reqwidth value
                self.update()
                label = tk.Label(frame, text=self.widgetModel.row_of_words.pop(), font=("Courier", 12))
                label.pack(side=tk.LEFT)
                self.labels.append(label)
            # the last label overreaches the boundary, remove it
            self.labels[-1].destroy()
            del self.labels[-1]

        for i, frame in enumerate(frames):
            frame.grid(row=i, column=0, sticky='w')


        #
        # for i in range(20):
        #     self.labels.append(tk.Label(self, text=self.parent.widgetModel.row_of_words[i], font=("Courier", 12)))
        # for label in self.labels:
        #     self.update()
        #     print(self.winfo_reqwidth())
        #     label.pack(side=tk.LEFT)

    # # create new row of labels if the user gets through the top row
    # def createLabelsUpdate(self):
    #



    def update_self(self):
        user_input = self.widgetModel.current_user_input
        if self.widgetModel.current_word_ind != 0:
            self.labels[self.widgetModel.current_word_ind - 1].config(bg='white')
        self.labels[self.widgetModel.current_word_ind].config(bg='grey')
        self.parent.parent.after(100, self.update_self)


