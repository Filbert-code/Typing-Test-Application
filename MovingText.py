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
        self.labelFrames = []
        self.labels = []
        self.endLabels = []
        self.createLabelRows()

        # update
        self.update_self()

    def createLabelRows(self):
        self.labelFrames = [self.createNextLabelRow(), self.createNextLabelRow()]
        for i, frame in enumerate(self.labelFrames):
            frame.grid(row=i, column=0, sticky='w')

    # returns a new frame with labels of words
    def createNextLabelRow(self):
        frame = tk.Frame(self)
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
        # end label is used to trigger adding a new row of words
        self.endLabels.append(self.labels[-1])
        self.widgetModel.active_labels = self.labels
        return frame


    # # create new row of labels if the user gets through the top row
    # def createLabelsUpdate(self):
    #

    def update_self(self):
        # get user input from WidgetModel
        user_input = self.widgetModel.current_user_input
        # update WidgetModel message properties
        self.widgetModel.current_label = self.labels[self.widgetModel.current_word_ind]
        self.widgetModel.current_frame = self.labelFrames[0]
        # change the color of the updated highlighted label/word
        if self.widgetModel.current_word_ind != 0 and self.labels[self.widgetModel.current_word_ind - 1] != self.endLabels[0]:
            self.labels[self.widgetModel.current_word_ind - 1].config(bg='white')
        self.labels[self.widgetModel.current_word_ind].config(bg='grey')

        # user has reached the end of the frame
        if self.widgetModel.at_frame_end:
            frame_to_destroy = self.labelFrames[1]
            del self.labelFrames[0]
            self.labelFrames[0].grid(row=0, column=0)
            self.widgetModel.at_frame_end = False
            new_frame = self.createNextLabelRow()
            new_frame.grid(row=1, column=0)
            self.labelFrames.append(new_frame)



        self.parent.parent.after(100, self.update_self)
