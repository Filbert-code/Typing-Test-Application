from random import randrange
import wikipedia


class WidgetModel:
    def __init__(self):
        self.word_bank = open("1000MostCommonWords.txt").readlines()
        self.current_user_input = ""
        self.current_topic_input = ""
        self.current_word_ind = 0
        self.label_ind = 0
        self.current_label = None
        self.current_frame = None
        self.at_frame_end = False
        # main row of words
        self.row_of_words = [self.word_bank[randrange(1000)] for num in range(0, 500)]
        self.row_of_words = [word[:-1] for word in self.row_of_words]
        self.active_labels = []

        self.started = False
        self.ended = False

        self.char_count = 0
        self.mistyped_word_count = 0
        self.mistyped_char_count = 0
        self.previousWordIncorrect = False

    def userInputMatchWordCheck(self):
        if self.userHasReachedFrameEnd():
            self.at_frame_end = True

        correct_word = self.active_labels[self.current_word_ind].cget('text')
        if self.current_user_input[:-1] != correct_word:
            # used in MovingText to highlight incorrect word in red
            self.previousWordIncorrect = True
            self.mistyped_word_count += 1
            self.mistyped_char_count += len(self.current_user_input) - 1
            print(self.mistyped_char_count)

        self.char_count += len(correct_word) + 1
        self.current_word_ind += 1

    def userHasReachedFrameEnd(self):
        if not self.current_frame:
            return False
        if self.current_label == self.current_frame.winfo_children()[-2]:
            return True
        return False

    def atFrameBeginning(self):
        if self.current_label == self.current_frame.winfo_children()[0]:
            return True
        return False

    def reset(self, new_row_of_words=None):
        self.current_user_input = ""
        self.current_word_ind = 0
        self.current_label = None
        self.current_frame = None
        self.at_frame_end = False
        self.char_count = 0
        self.mistyped_word_count = 0
        self.mistyped_char_count = 0
        self.previousWordIncorrect = False
        self.started = False
        self.ended = False
        if not new_row_of_words:
            self.row_of_words = [self.word_bank[randrange(1000)] for num in range(0, 500)]
            self.row_of_words = [word[:-1] for word in self.row_of_words]
        else:
            self.row_of_words = new_row_of_words
        self.active_labels = []
        self.label_ind = 0

