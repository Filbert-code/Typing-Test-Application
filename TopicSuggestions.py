import tkinter as tk
import wikipedia


class TopicSuggestions(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        # parent for this class is a TopicEntry instance
        self.parent = parent

        self.buttons = []

        self.num_of_suggestions = 5
        self.createButtons()

    def createButtons(self):
        for i in range(self.num_of_suggestions):
            btn = tk.Button(self, text='Example Button', font=('Raleway', 12), wraplength=300, width=23, command=self.getSuggestions)
            btn.grid(row=i, column=0)
            self.buttons.append(btn)

    def getSuggestions(self):
        search_phrase = self.parent.entry.get()
        print(wikipedia.search(search_phrase))


    def update_self(self):
        pass

