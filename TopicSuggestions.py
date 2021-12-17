import tkinter as tk
from tkinter import ttk
import timeit

import wikipedia


class TopicSuggestions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        # parent for this class is a TopicEntry instance
        self.parent = parent

        self.buttons_frame = None
        self.buttons = []

        self.num_of_suggestions = 5

        self.createDropdownList()
        self.update_buttons()

    def createButtons(self, suggestions):
        self.buttons_frame = tk.Frame(self)
        sep = ttk.Separator(self.buttons_frame).grid(row=0, column=0)
        for i, suggestion in enumerate(suggestions):
            def applySuggestion(phrase=suggestion):
                phrase = phrase.replace(' ', '_')
                self.parent.entry.delete(0, tk.END)
                self.parent.entry.insert(0, phrase)
                for buttons in self.buttons:
                    buttons.destroy()
                self.buttons = []
            btn = tk.Button(self.buttons_frame, text=suggestion, font=('Raleway', 12), wraplength=300,
                            width=23, command=applySuggestion)
            btn.grid(row=i + 1, column=0)
            self.buttons.append(btn)
        self.buttons_frame.grid(row=0, column=0)

    def getSuggestions(self):
        search_phrase = self.parent.entry.get()
        suggestions = wikipedia.search(search_phrase)
        if len(suggestions) < 5:
            self.num_of_suggestions = len(suggestions)
            return suggestions[:len(suggestions)]
        else:
            self.num_of_suggestions = 5
            return suggestions[:5]

    def createDropdownList(self):
        self.createButtons(self.getSuggestions())

    def update_buttons(self):
        start = timeit.default_timer()
        if len(self.buttons) != 0:
            for i, suggestion in enumerate(self.getSuggestions()):
                self.buttons[i].config(text=suggestion)
            end = timeit.default_timer()
            # print(end-start)
        self.parent.parent.parent.after(400, self.update_buttons)

