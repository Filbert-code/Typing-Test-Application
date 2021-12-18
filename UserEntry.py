import tkinter as tk


class UserEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='lightseagreen')

        self.current_word = None

        self.entry = tk.Entry(self, font=(self.parent.typingFont, 20), bg='black', fg='white', insertbackground='white',
                              justify=tk.CENTER, width=14)
        self.entry.grid(row=0, column=0)
        self.entry.focus_set()
        # self.entry.bind("<Key>", self.userPressedKey)

        # update
        self.update_self()

    def update_self(self):
        # disable the entry once the test has ended
        if self.widgetModel.ended:
            self.entry.config(state='disabled')
            return
        self.widgetModel.current_user_input = self.entry.get()
        if " " in self.entry.get() and self.widgetModel.started:
            self.entry.delete(0, tk.END)
            # check in the widgetModel if the current entry text matches the word and update the score
            self.widgetModel.previousWordIncorrect = False
            self.widgetModel.userInputMatchWordCheck()
        self.parent.parent.after(100, self.update_self)

    # def userPressedKey(self, key):
    #     if key.char.isalpha() or (key.char and key.char in string.punctuation) and not self.widgetModel.ended:
    #         self.widgetModel.char_count += 1
    #         print(self.widgetModel.char_count)

    def reset(self):
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.update_self()
