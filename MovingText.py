import tkinter as tk
from random import randrange
from time import sleep


class MovingText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.debugNum = 0

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='white', width=700, height=75)

        # widgets for the frame
        self.labelFrames = []
        self.labels = []
        self.endLabels = []
        self.createLabelRows()

        # waiting for player to start
        self.waitingForStart()

        # update
        self.update_self()

    def createLabelRows(self):
        self.labelFrames = [self.createNextLabelRow(), self.createNextLabelRow()]
        for i, frame in enumerate(self.labelFrames):
            frame.grid(row=i, column=0, sticky='w')
            # frame.pack(anchor=tk.CENTER)

    # returns a new frame with labels of words
    def createNextLabelRow(self):
        frame = tk.Frame(self)
        # max width for each frame is 600
        while frame.winfo_reqwidth() < 601:
            # need to call in order to get the correct winfo_reqwidth value
            self.update()
            label = tk.Label(frame, text=self.widgetModel.row_of_words.pop(), font=("TkDefaultFont", 20), padx=8)
            label.pack(side=tk.LEFT)
            self.labels.append(label)
        # the last label overreaches the boundary, remove it
        self.labels[-1].destroy()
        del self.labels[-1]
        # end label is used to trigger adding a new row of words
        self.endLabels.append(self.labels[-1])
        self.widgetModel.active_labels = self.labels
        return frame

    def waitingForStart(self):
        if not self.widgetModel.started and not self.widgetModel.ended:
            if self.widgetModel.current_user_input:
                self.widgetModel.started = True
        self.parent.parent.after(100, self.waitingForStart)

    def update_self(self):
        # print("wm.started: {}".format(self.widgetModel.started))
        # print("wm.ended: {}".format(self.widgetModel.ended))
        if self.widgetModel.started and not self.widgetModel.ended:
            # update WidgetModel message properties
            self.widgetModel.current_label = self.labels[self.widgetModel.current_word_ind]
            self.widgetModel.current_frame = self.labelFrames[0]

            # user has reached the end of the frame
            if self.widgetModel.at_frame_end:
                self.destroyAndCreateRowOfWords()
            else:
                self.highlightFocusedWord()
        self.parent.parent.after(25, self.update_self)

    def destroyAndCreateRowOfWords(self):
        frame_to_destroy = self.labelFrames[0]
        # destroy the row of words!
        del self.labelFrames[0]
        frame_to_destroy.destroy()
        self.labelFrames[0].grid(row=0, column=0, sticky='w')
        self.widgetModel.at_frame_end = False
        # create new row of words
        new_frame = self.createNextLabelRow()
        new_frame.grid(row=1, column=0, sticky='w')
        self.labelFrames.append(new_frame)

    def highlightFocusedWord(self):
        # change the color of the updated highlighted label/word
        if not self.widgetModel.atFrameBeginning():
            if self.widgetModel.previousWordIncorrect:
                self.labels[self.widgetModel.current_word_ind - 1].config(bg='red')
            else:
                self.labels[self.widgetModel.current_word_ind - 1].config(bg='white')
        self.labels[self.widgetModel.current_word_ind].config(bg='grey')

    def deleteAllRows(self):
        for frame in self.labelFrames:
            frame.destroy()

    def reset(self):
        self.deleteAllRows()
        self.labelFrames = []
        self.labels = []
        self.endLabels = []
        self.createLabelRows()

