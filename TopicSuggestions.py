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

        self.suggestion_btn = tk.Button(self.parent.parent, font=('Raleway', 10), text='Suggest!', command=self.createDropdownList)
        self.suggestion_btn.place(relx=1.0, rely=0.0, x=-50, y=72, anchor="ne")

    def createButtons(self, suggestions):
        for i, suggestion in enumerate(suggestions):
            def applySuggestion(phrase=suggestion):
                self.parent.entry.delete(0, tk.END)
                self.parent.entry.insert(0, phrase)
            btn = tk.Button(self, text=suggestion, font=('Raleway', 12), wraplength=300,
                            width=23, command=applySuggestion)
            btn.grid(row=i, column=0)
            self.buttons.append(btn)



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

    def update_self(self):
        pass

