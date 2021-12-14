import tkinter as tk
import wikipedia


class TopicEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.entry = tk.Entry(self, font=(self.parent.typingFont, 14), bg='black', fg='white', insertbackground='white')
        self.entry.grid(row=0, column=0)

        self.button = tk.Button(self, font=(self.parent.typingFont, 10), text='Change Topic!')
        self.button.grid(row=0, column=1)

        self.update_self()
        self.button.bind("<Button-1>", self.buttonClicked)

    def buttonClicked(self, key):
        phrase = self.entry.get()
        new_words = wikipedia.summary(phrase).split(' ')
        self.parent.newTopicReset(new_words)

    def update_self(self):
        self.widgetModel.current_topic_input = self.entry.get()
        self.parent.parent.after(100, self.update_self)


