import tkinter as tk
from tkinter import ttk


class StatsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='black', relief=tk.RAISED, bd=4)

        # create stats elements
        self.lastRunLabel, self.lastRunDivider = None, None
        self.wpmScoreLabel = None
        self.accuracyScoreLabel = None
        self.highscoreLabel = None
        self.hs1, self.hs2, self.hs3 = None, None, None
        self.divider, self.divider2 = None, None
        self.highscores = self.getHighscoresFromFile()
        self.updated_highscores = False

        self.createLabels()
        self.createHighscoreLabels()
        self.update_self()

    def createLabels(self):
        self.lastRunLabel = tk.Label(self, text="Last Run", font=(self.parent.typingFont, 14), bg="black",
                                       fg='white')
        self.lastRunLabel.grid(row=0, column=0, pady=(2, 0))
        self.lastRunDivider = ttk.Separator(self, orient='horizontal')
        self.lastRunDivider.grid(row=1, column=0, ipadx=65)
        self.wpmScoreLabel = tk.Label(self, text="Wpm: 0", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.wpmScoreLabel.grid(row=2, column=0)
        self.accuracyScoreLabel = tk.Label(self, text="Acc: 0%", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.accuracyScoreLabel.grid(row=3, column=0)

    def createHighscoreLabels(self):
        self.divider = ttk.Separator(self, orient='vertical')
        self.divider.grid(row=0, column=1, rowspan=5, sticky='e', ipady=75)
        self.highscoreLabel = tk.Label(self, text="Highscores", font=(self.parent.typingFont, 14), bg="black",
                                       fg='white')
        self.highscoreLabel.grid(row=0, column=2, pady=(2, 0), padx=12)

        self.divider2 = ttk.Separator(self, orient='horizontal')
        self.divider2.grid(row=1, column=2, sticky='e', ipadx=65)

        self.hs1 = tk.Label(self, text=str(self.highscores[0]), font=(self.parent.typingFont, 14), bg="black",
                                       fg='white')

        self.hs1.grid(row=2, column=2)
        self.hs2 = tk.Label(self, text=str(self.highscores[1]), font=(self.parent.typingFont, 14), bg="black",
                            fg='white')
        self.hs2.grid(row=3, column=2)
        self.hs3 = tk.Label(self, text=str(self.highscores[2]), font=(self.parent.typingFont, 14), bg="black",
                            fg='white')
        self.hs3.grid(row=4, column=2)

    def calculateWpm(self):
        num_of_words = (self.widgetModel.char_count / 5.0)
        wpm = round(num_of_words - self.widgetModel.mistyped_word_count, 2)
        if wpm < 0:
            wpm = 0
        return wpm

    def calculateAccuracy(self):
        total_correct_char = self.widgetModel.char_count
        total_char = (self.widgetModel.char_count + self.widgetModel.mistyped_char_count)
        return round((total_correct_char / float(total_char)) * 100.0, 2)

    def getHighscoresFromFile(self):
        # only want to call this once at the beginning of the app
        with open('highscores.txt') as f:
            lines = [float(line.rstrip()) for line in f]
        lines.sort(reverse=True)
        return lines

    def updateHighscoresFile(self, new_scores):
        for i, hs in enumerate([self.hs1, self.hs2, self.hs3]):
            if float(hs.cget('text')) != self.highscores[i]:
                hs.config(text=str(self.highscores[i]))

        textfile = open("highscores.txt", "w")
        for element in self.highscores:
            textfile.write(str(element) + "\n")
        textfile.close()
        pass

    def updateHighscoresArray(self, new_wpm):
        for i, num in enumerate(self.highscores):
            if new_wpm > num:
                print(i)
                self.highscores.insert(i, new_wpm)
                self.highscores.pop()
                print(self.highscores)
                return True
        return False

    def reset(self):
        self.updated_highscores = False

    def update_self(self):
        if self.widgetModel.started and self.widgetModel.ended:
            # update the words per minute stat
            new_wpm = self.calculateWpm()
            self.wpmScoreLabel.config(text="Wpm: {}".format(str(new_wpm)))
            self.accuracyScoreLabel.config(text="Acc: {}%".format(str(self.calculateAccuracy())))
            if not self.updated_highscores and self.updateHighscoresArray(new_wpm):
                self.updateHighscoresFile(self.highscores)
                self.updated_highscores = True
        self.parent.parent.after(100, self.update_self)



