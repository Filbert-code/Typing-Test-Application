import tkinter as tk


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



