from random import randrange


class WidgetModel:
    def __init__(self):
        self.word_bank = open("1000MostCommonWords.txt").readlines()
        self.current_user_input = ""
        self.current_word_ind = 0
        self.current_label = None
        self.current_frame = None
        self.at_frame_end = False
        # main row of words
        self.row_of_words = [self.word_bank[randrange(1000)] for num in range(0, 500)]
        self.row_of_words = [word[:-1] for word in self.row_of_words]
        self.active_labels = []

        self.score = 0

    def userInputMatchWordCheck(self):
        print("User input: " + self.current_user_input[:-1] +
              ", Word: " + self.active_labels[self.current_word_ind].cget('text'))
        if self.userHasReachedFrameEnd():
            self.at_frame_end = True
        if self.current_user_input[:-1] == self.active_labels[self.current_word_ind].cget('text'):
            self.score += 1
            return True
        return False

    def userHasReachedFrameEnd(self):
        if self.current_label == self.current_frame.winfo_children()[-1]:
            return True
        return False


