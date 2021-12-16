import tkinter as tk
import wikipedia


def getRidOfReturnsAndSpaces(list):
    for i, s in enumerate(list):
        if s == " ":
            del list[i]
            continue
        if '\n' in s:
            words = s.split('\n')
            list[i] = words[0]
            list.insert(i + 1, words[1])
    return list


class TopicEntry(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel
        self.config(bg='black', bd=2, relief=tk.RAISED)

        self.label = tk.Label(self, text="ENTER A TOPIC:", font=(self.parent.typingFont, 20), bg='black', fg='white')
        self.label.grid(row=0, column=0, columnspan=2)

        self.entry = tk.Entry(self, font=(self.parent.typingFont, 14), bg='black', fg='white', insertbackground='white')
        self.entry.grid(row=1, column=0)

        self.button = tk.Button(self, font=(self.parent.typingFont, 10), text='CHANGE TOPIC!')
        self.button.grid(row=1, column=1)

        self.update_self()
        self.button.bind("<Button-1>", self.buttonClicked)

    def buttonClicked(self, key):
        self.entry.delete(0, tk.END)
        self.label.config(text='loading...')
        self.update()
        try:
            page = wikipedia.page(self.entry.get())
        except wikipedia.exceptions.PageError:
            self.label.config(text='Page Not Found.')
            return
        except wikipedia.exceptions.WikipediaException:
            self.label.config(text='An Error Occurred.')
            return
        title = page.title
        new_words = wikipedia.summary(self.entry.get()).split(' ')
        new_words = getRidOfReturnsAndSpaces(new_words)
        self.parent.newTopicReset(new_words)
        self.label.config(text=title)

    def update_self(self):
        self.widgetModel.current_topic_input = self.entry.get()
        self.parent.parent.after(100, self.update_self)


