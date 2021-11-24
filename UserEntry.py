import tkinter as tk


class UserEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='green', width=200, height=42)
        self.grid_propagate(0)

        self.entry = tk.Entry(self, font=("Courier", 12))
        self.entry.grid(row=0, column=0)

        # update
        self.update_self()

    def update_self(self):
        self.widgetModel.current_user_input = self.entry.get()
        if " " in self.entry.get():
            self.entry.delete(0, tk.END)
            self.widgetModel.current_word_ind += 1

        self.parent.parent.after(100, self.update_self)