from random import randrange


class WidgetModel:
    def __init__(self):
        self.word_bank = open("1000MostCommonWords.txt").readlines()
        self.current_user_input = ""
        self.current_word_ind = 0
        # main row of words
        self.row_of_words = [self.word_bank[randrange(1000)] for num in range(0, 100)]




