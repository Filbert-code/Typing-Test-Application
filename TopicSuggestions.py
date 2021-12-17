import tkinter as tk
from tkinter import ttk
import timeit

import wikipedia
from wikipedia import WikipediaException


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

        self.update_buttons()

    def createButtons(self, suggestions):
        self.buttons_frame = tk.Frame(self)
        sep = ttk.Separator(self.buttons_frame).grid(row=0, column=0)
        for i, suggestion in enumerate(suggestions):
            def applySuggestion(phrase=suggestion):
                phrase = phrase.replace(' ', '_')
                self.parent.entry.delete(0, tk.END)
                self.parent.entry.insert(0, phrase)
                self.deleteSuggestions()
                self.parent.button.focus_set()
            btn = tk.Button(self.buttons_frame, text=suggestion, font=('Raleway', 12), wraplength=300,
                            width=23, command=applySuggestion)
            btn.grid(row=i + 1, column=0)
            self.buttons.append(btn)
        self.buttons_frame.grid(row=0, column=0)

    def getSuggestions(self):
        search_phrase = self.parent.entry.get()
        try:
            suggestions = wikipedia.search(search_phrase)
        except WikipediaException:
            print('Couldn\'t find that suggestion...')
            return []
        if len(suggestions) < 5:
            self.num_of_suggestions = len(suggestions)
            return suggestions[:len(suggestions)]
        else:
            self.num_of_suggestions = 5
            return suggestions[:5]

    def createDropdownList(self):
        self.createButtons(self.getSuggestions())

    def deleteSuggestions(self):
        for buttons in self.buttons:
            buttons.destroy()
        self.buttons = []

    def update_buttons(self):
        start = timeit.default_timer()
        if self.focus_get() == self.parent.entry:
            new_suggestions = self.getSuggestions()
            if len(new_suggestions) != 0:
                self.createDropdownList()
            else:
                self.deleteSuggestions()
            end = timeit.default_timer()
            # print(end-start)
        self.parent.parent.parent.after(1000, self.update_buttons)

